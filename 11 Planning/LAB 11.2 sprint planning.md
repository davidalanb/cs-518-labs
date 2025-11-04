# Sprint planning

### Outline:

* Sprint goal (work on two features)
* Stories (prioritize and select previously defined stories)
* Design: Design data model and API for each of the two features
* Work: determine responsibilities for team members
    - 4 team members for feature1 / feature2, frontend / backend

### Submission

* Submit document that summarizes the items below.
* Add your data model and API files to your group repository and provide a link to those files in your submitted document.

## Gitlab setup

* Create iteration (done for you) 
* Setup issue board

# Sprint planning

* Identify sprint goal.
* Select stories that contribute to that goal.

* **GITLAB**: Move selected stories into current iteration.

## Designs

* For each feature, design a data model and API.
* TODO:
    - data model: py files with pydantic model(s)
    - API: 
        - internal: py files with function signatures (akin to our user_api.py or user_client.py)
        - external: API endpoints (method, routes), parameters, and returns (akin to your fastAPI main.py)
        - you can produce skeleton files with just the function definitions.
        
* **GITLAB**: add your designs to your repo.

## Responsibilities

|               | Feature 1 | Feature 2 |
|---            |-----------|-----------|
|**Frontend**   | Person A  | Person B  |
|**Backend**    | Person C  | Person D  |

* Frontend:
    * UI
    * routing
    * API access
* Backend: 
    * API (internal or external)
    * Business logic
    * Database operations

* **GITLAB**: 
    - create new issues for the work required to develop the stories.
    - each story should have multiple associated issues.
    - you don't need to add "testing" as an issue - it is an inherent part of development.
    - assign issues to team members.