from azure.cosmos import exceptions, CosmosClient, PartitionKey
from integrations.keyVault import getKey
from config.loadConfig import *

def cosmosClient():

    config = loadConfigurations()

    # Initialize the Cosmos client
    # Need to secure the below endpoint and key!
    endpoint = config['db']['cosmos']['endpoint']
    key = 'jvMbkdOpS60FsYe1ps89DeMcumBihLQ3NFe8MGIyy24oc3szryAassUYcys2wFrKGTz8KgIc2X9r6Ul4x853yg=='
    #key = getKey('cosmosDbKey')

    client = CosmosClient(endpoint, key)

    # May want to place this somewhere else as well! 
    database_name = config['db']['cosmos']['databaseName']
    container_name = config['db']['cosmos']['containerName']

    database = client.create_database_if_not_exists(id=database_name)
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path=config['db']['cosmos']['partitionKey']),
        offer_throughput=400
    )

    return container