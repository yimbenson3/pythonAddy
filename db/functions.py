from db.connect import cosmosClient

container = cosmosClient()

def addItemIntoCosmos(item):
    #testItem =  {'id': '1', 'ipAddress': '127.0.0.1', 'firstVisit': '2021-11-24 06:08:45.576513+00:00'}
    #container.create_item(body=testItem)
    container.create_item(body=item)

def queryIpAddress(ipAddress):
    query = "SELECT TOP 1 * FROM c WHERE c.ipAddress IN ('" + ipAddress + "')"
    item = list(container.query_items(query=query,enable_cross_partition_query=True))
    return item

def readItemFromCosmos(item):
    read_item = container.read_item(item=item['id'], partition_key=item['ipAddress'])
    return read_item

def replaceItemInCosmos(item):
    response = container.replace_item(item=item, body=item)
    #print('Replaced Item\'s Id is {0}, new subtotal={1}'.format(response['id'], response['subtotal']))