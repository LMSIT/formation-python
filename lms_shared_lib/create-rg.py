from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
# from azure.common.credentials import ServicePrincipalCredentials

# Variables
RESOURCE_GROUP_NAME = "RG-EMAZ-2022"

# Configuration credention connexion
AZURE_TENANT_ID = "Replace with your azure tenant id"
AZURE_CLIENT_ID = "Replace with your azure client id service principal"
AZURE_CLIENT_SECRET = "Replace with your client secret id"
AZURE_SUBSCRIPTION_ID = "Your subscription Id"

# Function pour se connecter à la subscription

def login():
    
    credential = ServicePrincipalCredentials(
        client_id=AZURE_CLIENT_ID,
        secret=AZURE_CLIENT_SECRET,
        tenant=AZURE_TENANT_ID
    )

    return credential

# Function qui vérifier, créer et supprime un resource group 
def create_resource_group():

    # Create client 
    resource_client = ResourceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=AZURE_SUBSCRIPTION_ID
    )

    # Vérifier si le resource group exist 
    result_check = resource_client.resource_groups.check_existence(
        RESOURCE_GROUP_NAME
    )

    print("Wheter resource group exists:\n{}".format(result_check))

    if result_check == FALSE:
        # Créer le resource group 
        resource_rg = resource_client.resource_groups.create_or_update(
            RESOURCE_GROUP_NAME,
            {"location": "westeurope"}
        )
        print("Create resource group:\n{}".format(resource_rg))
    else:
        # Get resource group
        resource_rg = resource_client.resource_groups.get(
            RESOURCE_GROUP_NAME
        )
        print("Get resource group:\n{}".format(resource_rg))

# Function update resource groupe 
def update_resource_group():
    # Create client 
    resource_client = ResourceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=AZURE_SUBSCRIPTION_ID
    )

    # Vérifier si le resource group exit 
     # Vérifier si le resource group exist 
    result_check = resource_client.resource_groups.check_existence(
        RESOURCE_GROUP_NAME
    )

    if result_check == FALSE:
        print("Resource group non existant")
    else:
        # Add tag 
        resource_rg = resource_client.resource_groups.update(
            RESOURCE_GROUP_NAME,
            {
                "tags":{
                    "tag1": "valueA",
                    "tag2": "valueB"
                }
            }
        )
        print("Update resource group:\n{}".format(resource_rg))

# Function delete resource group 
def delete_resource_group():
    # Create client 
    resource_client = ResourceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=AZURE_SUBSCRIPTION_ID
    )

    delete = resource_client.resource_groups.begin_delete(
        RESOURCE_GROUP_NAME
    ).result()

    print("Delete Resource Groupe.\n")

if __name__ == "__main__":
    create_resource_group()
    update_resource_group()