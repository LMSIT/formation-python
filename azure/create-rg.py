from pickle import FALSE, TRUE
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
from azure.common.credentials import ServicePrincipalCredentials
from datetime import datetime
import json
import os

from pip import main

# Variables
LOCATION = "westeurope"
RESOURCE_GROUP_NAME = "RG-EMAZ-2022"

# Configuration credention connexion
AZURE_TENANT_ID = "2397b885-afe4-4bc7-9e1e-e4899ef44d1a"
AZURE_CLIENT_ID = "6348cb5f-fa1e-45bc-906c-3dd3c4b0f0c0"
AZURE_CLIENT_SECRET = "6skw1VISJ.-.M3cSbsq5ltQBTwja0E89K~"
AZURE_SUBSCRIPTION_ID = "0847fb06-cbca-406f-9649-81b141d8c299"

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


# {
#   "appId": "6348cb5f-fa1e-45bc-906c-3dd3c4b0f0c0",
#   "displayName": "myEmazServicePrincipalName",
#   "name": "6348cb5f-fa1e-45bc-906c-3dd3c4b0f0c0",
#   "password": "6skw1VISJ.-.M3cSbsq5ltQBTwja0E89K~",
#   "tenant": "2397b885-afe4-4bc7-9e1e-e4899ef44d1a"
# }