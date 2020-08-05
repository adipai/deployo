# deployo
A simple framework for azure queue storage based asynchronous processing of requests by a deployed ML model. Multiple instances of the model server are deployed using WSGI server
which take input from the queue to handle requests.
## Requirements
* Microsoft azure account
* Storage account with access to all networks
```
python 3.5+
azure-storage-queue v2.1
```

## Implementation
### server - deploy multiple instances on cloud
```
$cd server
$python runserver.py
```
### admin.py 
Utility script to manage the azure queue storage, can be executed by anyone with storage account access.
### client.py
Script that is invoked by the request generator to push request into the queue.

## Upcoming
* SAS based protection(currencty uses public endpoint with access for all networks)
* tensorflowing serving plug-in
