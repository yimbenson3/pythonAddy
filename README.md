# pythonAddy - Who is visiting? Python Web Application (Flask, Azure Cosmos, Javascript)

This web application creates and/or updates vistor's information (IP Address, time of visit, visit count and browser info) into Azure Cosmos DB. It display on the webpage the visitor's IP Address, browser information, and the number of times they have visited. If the visitor switches browswer and re-visits the site, the page notifies the visitor they are visiting from a different browswer than last time. 

The webpage also shows the virtual machine serving the requests.

![pythonAddy](https://raw.githubusercontent.com/bbarryyim/pythonAddy/main/pythonAddy.png)

## How to run locally

Clone this repository 

```sh
$ cd pythonAddy
$ chmod +x dockerRun.sh
$ ./dockerRun.sh
```

Open your browser and enter localhost to view the webpage

