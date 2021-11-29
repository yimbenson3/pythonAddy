# pythonAddy - Who is visiting? 

## Python Web Application (Flask, Azure Cosmos, Javascript)

This web application creates and/or updates vistor's information (IP Address, time of visit, visit count and browser info) into Azure Cosmos DB. It display on the webpage the visitor's IP Address, browser information, and the number of times they have visited. If the visitor switches browswer and re-visits the site, the page notifies the visitor they are visiting from a different browswer than last time. 

The webpage also shows the virtual machine serving the requests.

![pythonAddy](https://raw.githubusercontent.com/bbarryyim/pythonAddy/main/pythonAddy.png)

## How to run locally

1) Clone this repository
2) Create Azure Cosmos Database (We will need the database endpoint database name, container name, and partitionKey)
3) Create SendGrid Account (We will need the Sender Email Address registered)
4) Fill in your configurations (Refer to config/sampleConfig.yml)
4) Amend the following :

 ```python
def loadConfigurations():
    os.chdir('[PATH_TO_YOUR_CONFIG_FILE')
    with open("[CONFIG_FILE_IN_YML]","r") as file:
```
5) Inside your root folder, create a file named “.env.” Add the your Azure Cosmos Secret Key and Send Grid API Key inside the file

```sh
$ cd pythonAddy
$ vi .env
cosmosDbKey = [YOUR COSMOS DB KEY]
sendGridApiKey = [YOU SEND GRID API KEY]
```

6) Run the following 
```sh
$ cd pythonAddy
$ chmod +x dockerRun.sh
$ ./dockerRun.sh
```

Open your browser and enter localhost to view the webpage :) 



