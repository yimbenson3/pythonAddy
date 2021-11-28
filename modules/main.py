from modules.visitorFunctions import *
from integrations.cosmosFunctions import *
import uuid

def jsonItem():
    id = uuid.uuid4()
    item = {'id': '', 'ipAddress': '', 'firstVisit': '', 'lastVisit': '', 'counter': '', 'browserInfo': ''}
    item['id'] = str(id)
    return item

def main():
    ipAddress = getIpAddress()
    currentTimeStamp = getCurrentTimestamp()
    browserInfo = getUserAgent()

    item = queryUniqueFromId("ipAddress", ipAddress)
    
    if len(item) == 0:
        item = jsonItem()
        item['ipAddress'] = ipAddress
        item['firstVisit'] = currentTimeStamp
        item['lastVisit'] = currentTimeStamp
        item['counter'] = 1
        item['browserInfo'] = browserInfo
        addItemIntoCosmos(item)
        return item

    else: 
        readItem = readItemFromCosmos(item[0])
        readItem['lastVisit'] = currentTimeStamp
        readItem['counter'] = readItem['counter'] + 1
        readItem['browserInfo'] = browserInfo
        replaceItemInCosmos(readItem)
        return readItem

        