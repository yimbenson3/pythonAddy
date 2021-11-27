from azure.cosmos import exceptions, CosmosClient, PartitionKey
from db.keyVault import getKey
import yaml

def cosmosClient():
    with open("db/dbConfig.yml","r") as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)

    # Initialize the Cosmos client
    # Need to secure the below endpoint and key!
    endpoint = config['db']['cosmos']['endpoint']
    key = getKey('cosmosDbKey')

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