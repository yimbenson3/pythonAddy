from azure.cosmos import exceptions, CosmosClient, PartitionKey
from dotenv import load_dotenv
from config.loadConfig import *
import os

def cosmosClient():

    load_dotenv()
    config = loadConfigurations()

    # Initialize the Cosmos client
    endpoint = config['db']['cosmos']['endpoint']
    key = os.environ.get('cosmosDbKey')

    client = CosmosClient(endpoint, key)

    database_name = config['db']['cosmos']['databaseName']
    container_name = config['db']['cosmos']['containerName']

    database = client.create_database_if_not_exists(id=database_name)
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path=config['db']['cosmos']['partitionKey']),
        offer_throughput=400
    )

    return container