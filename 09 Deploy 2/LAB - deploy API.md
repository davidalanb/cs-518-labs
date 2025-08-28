## Deploy Guide Service

Task - deploy your Guide Service to Azure functions

<!-- Directory structure (something like this, names may vary):
* user_service/
  * user_models.py
  * UserManager.py
  * user_tests.py
  * server.py
  * api_tests.py
  * [azure functions files] (function_app.py, etc.)
  * README.md -->

<!-- 
### Test with deployed DB

Test with unit tests:
- Set the conn_str in your unit tests (user_tests.py) to the deployed cluster.
- rerun and verify.

Update your server.py
- Set conn_str in server.py to URI with username / password
- Rerun API tests and verify. -->

<!-- ### Configure Atlas for access from Functions App

* Sign into MongoDB Atlas
* Security > Network Access > Add IP Address
* Add this Entry: 0.0.0.0/0 -->

### Connect fastAPI app to Azure Functions app

references:
* https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python 
* https://learn.microsoft.com/en-us/samples/azure-samples/fastapi-on-azure-functions/fastapi-on-azure-functions/

steps:
* open a terminal in the root directory of your service (i.e., where server.py and UserManager.py are located)
* run this command:
```func init --python```
* add to requirements.txt
    - fastapi
    - pymongo
* add to host.json:
```
  "extensions": {
    "http": {
        "routePrefix": ""
    }
  }
```
* REPLACE the contents of function_app.py with the code below.
  * (assumes that your fastapi app is defined in server.py)
```
import azure.functions as func

from server import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
```

try it out:
* in your API project root, run "func start"

### Test with Azure Functions running locally

* update the URI in your API tests and rerun
  * you will probably just need to update the port from 8000 to 7071
  * 8000 is fastapi default, and 7071 is azure functions default

### Deploy Azure Functions

Ref:
* https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python

Steps:
* Go to "Create Supporting Azure Resources..."
* Complete all steps up to and including "Deploy the function project..."
  * For REGION you can use "EAST US"
  * For GROUP_NAME, STORAGE_NAME, and APP_NAME, you will come up with values.

### Command quick-ref:

```
az login

az group create --name <GROUP_NAME> --location <REGION>

az storage account create --name <STORAGE_NAME> --location <REGION> --resource-group <GROUP_NAME> --sku Standard_LRS

az functionapp create --resource-group <GROUP_NAME> --consumption-plan-location westeurope --runtime python --runtime-version <PYTHON_VERSION> --functions-version 4 --name <APP_NAME> --os-type linux --storage-account <STORAGE_NAME>

func azure functionapp publish <APP_NAME>
```

### Testing with deployed API

* Successfull deployment should give you a URL, like: <service-name>.azurewebsites.net
* Update your API tests to use this URL.

### Deployment tips and gotchas

Tips:
* The last two commands need to be run in your API project root (e.g. same directory as function_app.py)
* Keep track of your deploy commands in a README.md file
* Especially the last one, which you will need to redeploy

Gotchas:

* "Remote build succeeded!" But no functions shown
  * make sure that you are connecting to your Atlas cloud DB, not your local
  * make sure that you do not have any extra imports that are not included in requirements.txt

* Can't create Azure Storage Account: SubscriptionNotFound
  * https://stackoverflow.com/questions/78912586/cant-create-azure-storage-account-subscriptionnotfound 
  * Azure portal > Subscriptions > Settings > Resource Providers
  * search "Microsoft.Storage" and change status to Registered
* Azure functions referenced bundle microsoft.azure.functions.extensionbundle [..] doe snot meet required minimum version
  * https://learn.microsoft.com/en-us/answers/questions/1109340/1-8-1-does-not-meet-required-minimum-version-where 

