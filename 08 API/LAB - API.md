## Implementing an API

* CS_518/
  - app_project/  <-- everything before this week
    - src/
      - accounts/
        - data/
      - app.py
    - tests/
  - api_project/  <-- new this week
    - src/
      - data/     <-- copy files from app/src/accounts/data
      - main.py
    - tests/
      - test_api.py   <-- need to install api_project, or move this next to main.py

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


