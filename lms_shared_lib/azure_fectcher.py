import os
import logging
import json

import requests
from decouple import config 

from azure.mgmt.resource.resources import ResourceManagementClient
from azure.common.credentials import UserPassCredentials, ServicePrincipalCredentials

logger = logging.getLogger(__name__)

CURRENT = os.path.abspath(os.path.dirname(__file__))
PROVIDERS_FILEPATH = config(
    'PROVIDERS_FILEPATH', default=os.path.join(CURRENT, 'providers.json')
)

PROVIDERS = None

def get_ratelimit_header(headers):
    for k, v in headers.items():
        if k.startswith("x-ms-ratelimit-remaining"):
            return k, v

    return None, None

class AuthenticationError(Exception):
    pass

def download_providers(
    session, subscription_id=None, is_china=False, api_version="2020-06-01"
):
    """Get list of services providers
    
    @see: https://docs.microsoft.com/en-us/rest/api/resources/providers/list
    """
    base_url = get_azure_base_url(is_china=is_china)
    providers_url = f"{base_url}/subscriptions/{subscription_id}/providers?api-version={api_version}"

    resp = session.get(providers_url)
    resp.raise_for_status()

    return resp.json()


# Transform providers
def transform_providers(providers):

    result = {}
    for provider in providers['value']:
        namespace = provider['namespace']
        resourceTypes = provider.get('resourceTypes')
        if resourceTypes:
            for r in resourceTypes:
                if r.get('apiVersion'):
                    r_type = "%s/%s" % (namespace, r['resourceType'])
                    result[r_type] = r['apiVersions'][0]
    
    return result

# load providers 
def load_providers(filepath=PROVIDERS_FILEPATH):
    global PROVIDERS

    if not os.path.exists(filepath):
        raise RuntimeError(f"{filepath} not found")

    with open(filepath) as fp:
        _providers = json.load(fp)
        PROVIDERS = {k.lower(): v for k, v in _providers.items()}
    if not PROVIDERS:
        raise Exception("PROVIDERS empty")

    logger.info(f"user provider filepath: {filepath}")

    return PROVIDERS

load_providers()

def get_azure_base_url(is_china=False):
    if is_china:
        return "https://management.chinacloudapi.cn"
    return "https://management.azure.com"

def get_api_version(resource_id):
    asset_split = resource_id.split('/')
    asset_type = f"{asset_split[6]}/{asset_split[7]}"
    api_version = PROVIDERS.get(asset_type.lower())

    if not api_version:
        raise Exception(f"api_version not found for type {asset_type}")

    return api_version

def get_session(token:str):
    session = requests.Session()
    session.headers['authorization'] = 'Bearer %s' % token
    return session

# Get access token 
def get_access_token(
    subscription_id=None,
    user=None,
    password=None,
    tenant=None,
    is_china=None,
    timeout=None):
    """
    Open Azure API session using AzureSDK and return Token 

    :param subscription_id: Azure Subscription ID
    :type subscription_id: str
    :param user: UserName or Client ID
    :type user: str
    :param password: Password or Secret ID
    :type password: str
    :param tenant: Tenant ID
    :type tenant: str
    :param is_china: China Option
    :type is_china: bool

    :return: Token
    :rtype: dict
    """

    for field_name in ['subscription_id', 'user', 'password']:
        if locals().get(field_name, None) is None:
            raise AttributeError("field [%s] is required")

    try:
        if not tenant:
            credentials = UserPassCredentials(user, password, china=is_china)
        else:
            credentials = ServicePrincipalCredentials(
                client_id=user, secret=password, tenant=tenant, china=is_china, timeout=timeout
            )
    except Exception as e:
        msg = 'Login Azure FAILED with message : %s' % str(e)
        logger.error(msg)
        raise AuthenticationError(msg)

    rm = ResourceManagementClient(credentials, subscription_id)
    if rm.config.generate_client_request_id:
        return credentials.token
    else:
        msg = 'login azure failed'
        logger.error(msg)
        raise AuthenticationError(msg)

def get_resource_by_id(resource_id, session=None, token=None, is_china=False, timeout=None):
    """Get Resource by ID

    # TODO: doc args 

    @see: https://docs.microsoft.com/en-us/rest/api/resources/resources/getbyid
    """

    # TODO: voir si valable partout : &$expand=resourceTypes/aliases

    base_url = get_azure_base_url(is_china=is_china)
    api_version = get_api_version(resource_id)
    resource_id = resource_id.lstrip('/') # lstrip: supprime les espaces à gauche de la chaîne

    url = f"{base_url}/{resource_id}?api-version={api_version}"
    session = session or get_session(token=token)

    resp = session.get(url, timeout=timeout)

    rate_header, rate_value = get_ratelimit_header(resp.headers)
    msg = f"ratelimit : {rate_header}={rate_value} - {resource_id}"
    logger.debug(msg)

    resp.raise_for_status()

    return resp.json()

# get resources list 
def get_resources_list(subscription_id, session=None, token=None, is_china=False, includes=PROVIDERS, timeout=None):
    """Get Resources List

    @see: https://docs.microsoft.com/en-us/rest/api/resources/resources/list
    """

    base_url = get_azure_base_url(is_china=is_china)
    api_version = includes.get("Microsoft.Resources/resources".lower())
    url = f"{base_url}/subscriptions/{subscription_id}/resources?api-version={api_version}"
    session = session or get_session(token=token)

    resp = session.get(url, timeout=timeout)

    rate_header, rate_value = get_ratelimit_header(resp.headers)
    msg = f"ratelimit : {rate_header}={rate_value} - {subscription_id}"
    logger.debug(msg)

    resp.raise_for_status()

    for item in resp.json()['value']:
        if item['type'].lower() in includes:
            yield item
        else:
            logger.info("exclude type : %s" % item['type'].lower())

# Get tenant
def get_tenants(session=None, token=None, is_china=False, timeout=None):
    """
    voir: https://docs.microsoft.com/en-us/rest/api/resources/tenants/list
    """
    base_url = get_azure_base_url(is_china=is_china)

    api_version = PROVIDERS.get("Microsoft.Resources/tenants".lower())

    url = f"{base_url}/tenants?api-version={api_version}"
    session = session or get_session(token=token)

    resp = session.get(url, timeout=timeout)
    resp.raise_for_status()

    return resp.json()['value']

# Get subscription list 
def get_subscriptions_list(session=None, token=None, is_china=False, timeout=None):
    """Get Subscriptions List

    voir: https://docs.microsoft.com/en-us/rest/api/resources/subscriptions/list

    [{
      "id": "/subscriptions/291bba3f-e0a5-47bc-a099-3bdcb2a50a05",
      "subscriptionId": "291bba3f-e0a5-47bc-a099-3bdcb2a50a05",
      "tenantId": "31c75423-32d6-4322-88b7-c478bdde4858",
      "displayName": "Example Subscription",
      "state": "Enabled",
      "subscriptionPolicies": {
        "locationPlacementId": "Internal_2014-09-01",
        "quotaId": "Internal_2014-09-01",
        "spendingLimit": "Off"
      },
      "authorizationSource": "RoleBased",
      "managedByTenants": [
        {
          "tenantId": "8f70baf1-1f6e-46a2-a1ff-238dac1ebfb7"
        }
      ],
      "tags": {
        "tagKey1": "tagValue1",
        "tagKey2": "tagValue2"
      }
    }]

    """

    base_url = get_azure_base_url(is_china=is_china)

    api_version = PROVIDERS.get("Microsoft.Resources/subscriptions".lower())

    url = f"{base_url}/subscriptions?api-version={api_version}"
    session = session or get_session(token=token)

    resp = session.get(url, timeout=timeout)
    resp.raise_for_status()

    return resp.json()['value']

def get_regions_list(subscription_id, session=None, token=None, is_china=False, timeout=None):

    """
    # https://docs.microsoft.com/en-us/rest/api/resources/subscriptions/listlocations

    [{
        "id": "/subscriptions/291bba3f-e0a5-47bc-a099-3bdcb2a50a05/locations/centralus",
        "name": "centralus",
        "displayName": "Central US",
        "regionalDisplayName": "(US) Central US",
        "metadata": {
          "regionType": "Physical",
          "regionCategory": "Recommended",
          "geographyGroup": "US",
          "longitude": "-93.6208",
          "latitude": "41.5908",
          "physicalLocation": "Iowa",
          "pairedRegion": [
            {
              "name": "eastus2",
              "id": "/subscriptions/291bba3f-e0a5-47bc-a099-3bdcb2a50a05/locations/eastus2"
            }
          ]
        }
    }]
    """
    base_url = get_azure_base_url(is_china=is_china)

    #api_version = PROVIDERS.get("Microsoft.Resources/subscriptions/locations".lower())
    api_version = PROVIDERS.get("Microsoft.Resources/locations".lower())

    url = f"{base_url}/subscriptions/{subscription_id}/locations?api-version={api_version}"
    session = session or get_session(token=token)

    resp = session.get(url, timeout=timeout)

    rate_header, rate_value = get_ratelimit_header(resp.headers)
    msg = f"ratelimit : {rate_header}={rate_value} - {subscription_id}"
    logger.debug(msg)

    resp.raise_for_status()

    global_region = {
        "id": f"/subscriptions/{subscription_id}/locations/global",
        "name": "global",
        "displayName": "Global",
        "longitude": "0.0",
        "latitude": "0.0"
    }

    return resp.json()['value'] + [global_region]

if __name__ == "__main__":

    subscription_id = "0847fb06-cbca-406f-9649-81b141d8c299"
    user = "6348cb5f-fa1e-45bc-906c-3dd3c4b0f0c0"
    password = "6skw1VISJ.-.M3cSbsq5ltQBTwja0E89K~"
    tenant = "2397b885-afe4-4bc7-9e1e-e4899ef44d1a"
    resource_id = "/subscriptions/0847fb06-cbca-406f-9649-81b141d8c299/resourceGroups/RG-EMAZ-2022/providers/Microsoft.Storage/storageAccounts/pocemaz/blobServices/default"

    token = get_access_token(
        subscription_id=subscription_id,
        user=user,
        password=password,
        tenant=tenant,
        is_china=False
    )

    session = get_session(token=token['access_token'])

    data = get_resource_by_id(resource_id, session=session)
    filepath = "export-resource-%s.json" % resource_id.replace("/", "@")
    with open(filepath, 'w') as fp:
        json.dump(data, fp)