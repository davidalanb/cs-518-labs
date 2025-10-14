# Implementing an API

## Directory structure:

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

## Development

Viewing the API specification:
* your API spec is defined by your server code.
* open user_manager directory in your terminal
* start the server
```fastapi dev main.py```
* open your browser and go to: http://127.0.0.1:8000/docs 

Your job:
* Your job is to implement the endpoints in server.py
* You also need to develop tests
* Make sure to use unittest assertions.

## Testing and submission:

* Thoroughly test with the provided tests before you attempt a submission on Gradescope
  - you may have to install additional libraries to run the tests
* Submit to Gradescope
  * Submit a zip file containing the contents of api_project (not the folder, just the contents)

## Notes 

### UserAuth

* The authenticate route requires a UserAuth model.
* See rationale here:  [Auth bug](https://mycourses.unh.edu/courses/138902/discussion_topics/1218884)
* Add this to user_models.py in api_project/src/data:

```python
class UserAuth(BaseModel):
    username: str
    password: str
```


