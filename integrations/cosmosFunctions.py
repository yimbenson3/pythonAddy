from integrations.cosmosClient import cosmosClient
from integrations.sendEmail import *
import logging

container = cosmosClient()

loggerAzure = logging.getLogger("azure.core.pipeline.policies.http_logging_policy")
loggerAzure.setLevel(logging.WARNING)

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def queryTopRow(id_name, id):
    return "SELECT TOP 1 * FROM c WHERE c." + id_name + " IN ('" + id + "')"

def readChangeFeed(container):
    response = container.query_items_change_feed()
    docList = []
    for doc in response:
        docList.append(doc)
    emailSendGrid(docList[-1])

def addItemIntoCosmos(item):
    container.create_item(body=item)
    readChangeFeed(container)

def queryUniqueFromId(id_name, id):
    query = queryTopRow(id_name, id)
    item = list(container.query_items(query=query,enable_cross_partition_query=True))
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    logging.info('Query returned {0} items. Operation consumed {1} request units'.format(len(item), request_charge))
    return item

def readItemFromCosmos(item):
    read_item = container.read_item(item=item['id'], partition_key=item['ipAddress'])
    logging.info('Found Item\'s Id is {0}'.format(item['id']))
    return read_item

def replaceItemInCosmos(item):
    response = container.replace_item(item=item, body=item)
    logging.info('Replaced Item\'s Id is {0}'.format(response['id']))
