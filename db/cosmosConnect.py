from azure.cosmos import exceptions, CosmosClient, PartitionKey
from db.keyVault import getKey

# Initialize the Cosmos client
# Need to secure the below endpoint and key!
endpoint = "https://barry-azure-cosmo-account.documents.azure.com:443/"
key = getKey('cosmosDbKey')

client = CosmosClient(endpoint, key)

# May want to place this somewhere else as well! 
database_name = 'databaseAzure'
container_name = 'container3'

database = client.create_database_if_not_exists(id=database_name)
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/ipAddress"),
    offer_throughput=400
)

def addItem():
    testItem =  {'id': '1', 'ipAddress': '127.0.0.1', 'firstVisit': '2021-11-24 06:08:45.576513+00:00'}
    container.create_item(body=testItem)

