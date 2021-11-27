from db.connect import cosmosClient

container = cosmosClient()

def queryTopRow(id_name, id):
    return "SELECT TOP 1 * FROM c WHERE c." + id_name + " IN ('" + id + "')"

def addItemIntoCosmos(item):
    container.create_item(body=item)

def queryUniqueFromId(id_name, id):
    query = queryTopRow(id_name, id)
    item = list(container.query_items(query=query,enable_cross_partition_query=True))
    request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
    print('Query returned {0} items. Operation consumed {1} request units'.format(len(item), request_charge))
    return item

def readItemFromCosmos(item):
    read_item = container.read_item(item=item['id'], partition_key=item['ipAddress'])
    print('Found Item\'s Id is {0}'.format(item['id']))
    return read_item

def replaceItemInCosmos(item):
    response = container.replace_item(item=item, body=item)
    print('Replaced Item\'s Id is {0}'.format(response['id']))