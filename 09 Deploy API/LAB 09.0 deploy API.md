# Deploy User API

references:

* https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python 
* https://learn.microsoft.com/en-us/samples/azure-samples/fastapi-on-azure-functions/fastapi-on-azure-functions/

We will connect our FastAPI app to an Azure function app

## Initialize azure functions app

steps:

Install the azure-functions package for Python

* open a terminal in the src directory of your service (i.e., where main.py is located)
* run this command:
  * ```func init --python```

### Setup requirements

generate requirements.txt

* install pipreqs
  * ```pip install pipreqs```
* navigate in terminal to api src directory
* (optional) backup your requirements.txt
  * the command below will overwrite requirements.txt
* run pipreqs
  * ```pipreqs . --force```

add azure-functions

* **make sure to add azure-functions to requirements.txt**

### Setup host.json and function_app.py

host.json:

* add to host.json, inside of the top-level dict:
```
  "extensions": {
    "http": {
        "routePrefix": ""
    }
  }
```

function_app.py:

* REPLACE the contents of function_app.py with the code below.
  * (assumes that your fastapi app is defined in main.py)
```python
import azure.functions as func

from main import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
```

try it out:
* in your API project root, run ```func start```
* go to localhost:7071/docs

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

Notes fa25:
* You should aleady have a resource group (GROUP_NAME) from deploying your app.
* You can go to portal.azure.com
  - app services OR
  - storage groups  


### Command quick-ref:

Commands:

```
az login

<!-- Not necessary: you can use the group created when deploying the app -->
<!-- az group create --name <GROUP_NAME> --location <REGION> -->

az storage account create --name <STORAGE_NAME> --resource-group <GROUP_NAME> --sku Standard_LRS

az functionapp create --resource-group <GROUP_NAME> --consumption-plan-location westeurope --runtime python --runtime-version <PYTHON_VERSION> --functions-version 4 --name <APP_NAME> --os-type linux --storage-account <STORAGE_NAME>

func azure functionapp publish <APP_NAME>
```

Example:

```
az storage account create --name CS518-RG --resource-group cs518fa25storage --sku Standard_LRS

az functionapp create --resource-group CS518-RG --consumption-plan-location eastus --runtime python --runtime-version 3.11 --functions-version 4 --name userAPIfa25 --os-type linux --storage-account cs518fa25storage

func azure functionapp publish userAPIfa25
```

### Testing with deployed API

* Successfull deployment should give you a URL, like: myservice.azurewebsites.net
* Update your API tests to use this URL.

### Deployment tips and gotchas

Tips:
* The last two commands need to be run in your API project root (e.g. same directory as function_app.py)
* Keep track of your deploy commands in a README.md file
* Especially the last one, which you will need to redeploy

Gotchas:

* "Remote build succeeded!" But no functions shown
  * make sure that you are connecting to your Atlas cloud DB, not your local
  * make sure that all of your imports are included in requirements.txt

* Can't create Azure Storage Account: SubscriptionNotFound
  * https://stackoverflow.com/questions/78912586/cant-create-azure-storage-account-subscriptionnotfound 
  * Azure portal > Subscriptions > Settings > Resource Providers
  * search "Microsoft.Storage" and change status to Registered
* Azure functions referenced bundle microsoft.azure.functions.extensionbundle [..] doe snot meet required minimum version
  * https://learn.microsoft.com/en-us/answers/questions/1109340/1-8-1-does-not-meet-required-minimum-version-where 

