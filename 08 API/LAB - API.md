## Implementing an API

Task:
* Your task is to develop an API for the guide features of the app.  
  - this includes profiles and adventures

Submission:
* Work with your individual repo
<!-- * Add your API server (server.py) and your tests (api_tests.py) to the directory with your UserManager
* Directory structure:
  * user_manager/
    * user_models.py
    * UserManager.py
    * unit_tests.py (i.e., user_tests.py)
    * server.py
    * api_tests.py
* Push your changes to your repo when you're done -->

### Development

Viewing the API specification:
* your API spec is defined by your server code.
* open user_manager directory in your terminal
* start the server
```fastapi dev server.py```
* open your browser and go to: http://127.0.0.1:8000/docs 

Your job:
* Your job is to implement the endpoints in server.py
* You also need to develop tests
* Make sure to use unittest assertions.

---

### Notes

* A route is a URI
* Methods are, e.g.: {GET, POST, PUT, DELETE}
* An endpoint is a route + a method
* API spec includes endpoints plus:
  * request parameters (path and/or query)
  * request body
  * responses (response codes and body)
* request / response bodies are defined by your data model


