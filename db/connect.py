from azure.cosmos import exceptions, CosmosClient, PartitionKey
#from db.keyVault import getKey

def cosmosClient():
    # Initialize the Cosmos client
    # Need to secure the below endpoint and key!
    endpoint = "https://barry-azure-cosmo-account.documents.azure.com:443/"
    key = 'jvMbkdOpS60FsYe1ps89DeMcumBihLQ3NFe8MGIyy24oc3szryAassUYcys2wFrKGTz8KgIc2X9r6Ul4x853yg=='
    #key = getKey('cosmosDbKey')

    client = CosmosClient(endpoint, key)

    # May want to place this somewhere else as well! 
    database_name = 'databaseAzure'
    container_name = 'container4'

    database = client.create_database_if_not_exists(id=database_name)
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path="/ipAddress"),
        offer_throughput=400
    )

    return container