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

        #return "Welcome, IP: " + ipAddress + ", You first visit!, Browser: " + browserInfo
        return item
    else: 
        readItem = readItemFromCosmos(item[0])
        if str(readItem['browserInfo']) != browserInfo:
            firstVisitTime = readItem['firstVisit']
            readItem['lastVisit'] = currentTimeStamp
            readItem['counter'] = readItem['counter'] + 1
            readItem['browserInfo'] = browserInfo
            replaceItemInCosmos(readItem)

            #return "Hello again, IP: " + ipAddress + ", Visit Count: " + str(readItem['counter']) + ", Your are visiting from different Browswer than last, Browser: " + browserInfo
            return readItem

        else:
            firstVisitTime = readItem['firstVisit']
            readItem['lastVisit'] = currentTimeStamp
            readItem['counter'] = readItem['counter'] + 1
            replaceItemInCosmos(readItem)

            #return "Hello again, IP: " + ipAddress + ", Visit Count: " + str(readItem['counter']) + ", Browser: " + browserInfo
            return readItem