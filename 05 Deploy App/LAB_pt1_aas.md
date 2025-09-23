# Deploy app with AAS

## Prelab

* create a free Azure student account
    - https://azure.microsoft.com/en-us/free/students
* install Azure CLI
    - https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest 

## Lab

* Ref:
    * https://learn.microsoft.com/en-us/azure/app-service/quickstart-python 

* submit:
    - submit URL for your deployed app to Canvas

### Instructions

* steps:
    - make sure that your app is connecting to Atlas DB, not localhost
    - setup requirements.txt (goes in src, adjacent to app.py)

```
pydantic
pymongo
flask
flask-login
```

* run commands (run from src, directory containing app.py):
    - ```az login```
    - ```az webapp up --runtime PYTHON:3.11 --sku F1 --logs```


## FAQ

If you encounter a regions error:

```
az provider register --namespace Microsoft.Web
az webapp up --runtime PYTHON:3.11 --sku F1 --logs --location eastus2
```