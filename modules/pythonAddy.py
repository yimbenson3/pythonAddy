from modules.visitor import *
from db.functions import *
import uuid


def jsonItem():
    id = uuid.uuid4()
    item = {'id': '', 'ipAddress': '', 'firstVisit': '', 'lastVisit': '', 'counter': '', 'browserInfo': ''}
    item['id'] = str(id)
    return item

def visitorFirstTime():
    ipAddress = getIpAddress()
    if len(queryIpAddress(ipAddress)) == 0:
        return True
    else:
        return False

def pythonAddy():
    ipAddress = getIpAddress()
    currentTimeStamp = getCurrentTimestamp()
    browserInfo = getUserAgent()

    if visitorFirstTime() == True:
        item = jsonItem()
        item['ipAddress'] = ipAddress
        item['firstVisit'] = currentTimeStamp
        item['lastVisit'] = currentTimeStamp
        item['counter'] = 1
        item['browserInfo'] = browserInfo
        # Add item into CosmosDB
        addItemIntoCosmos(item)

        return "Hello, IP: " + ipAddress + ", Time of visit: " + currentTimeStamp + ", Browser: " + browserInfo

    else:
        item = queryIpAddress(getIpAddress())
        readItem = readItemFromCosmos(item[0])
        firstVisitTime = readItem['firstVisit']
        readItem['lastVisit'] = currentTimeStamp
        readItem['counter'] = readItem['counter'] + 1
        readItem['browserInfo'] = browserInfo
        # Replace item in CosmosDB
        replaceItemInCosmos(readItem)

        return "Hello again, IP: " + ipAddress + ", First Visit at: " + str(firstVisitTime) + ", Browser: " + browserInfo