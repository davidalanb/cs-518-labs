# Sprint planning

## Outline & submission:

Sprint planning document:

* sprint planning
    * Sprint goals / features
    * Stories grouped by feature
* story decomposition
    * stories are decomposed into work items
    * contract / designs:
        - data model and API / adapter template
* Responsibilities for team members
    - 4 team members for feature1 / feature2, frontend / backend

Submission:

* Submit document that summarizes the items below.
* Add your data model and API files to your group repository and provide a link to those files in your submitted document.

## Gitlab setup

* Create iteration (done for you) 
* Setup issue board
    - plan > issue boards
    - [create list]
    - iteration > select iteration
    - move iteration in between "Open" and "Closed"

## Sprint planning

* Identify sprint goal(s).
    - feature 1:
    - feature 2:
* Select stories that contribute to that goal.
    - group stories by feature

* **GITLAB**: Move selected stories into current iteration.

## Story decomposition

* For the selected issues, identify the "definition of done"
* Identify the work required to complete the story.

Examples of tasks:

Work items / Gitlab issues: 

* Contract:
    * Data models
    * API specification
* Frontend:
    * UI
    * routing
    * API access
* Backend: 
    * API (internal or external)
    * Business logic
    * Database operations
* Integration testing and deployment
    * Testing
    * Deployment

Notes:

* Unit testing is expected for all stories, so it doesn't need to be a separate issue.
* Backend can test independently
* Frontend can test independently of backend by using mocking 
    - For example, you can create a mock API client that will allow you to build UI elements without relying on a real API.

* **GITLAB** create new issues for the work tasks you've identified.
    - you can use labels for related tasks

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

* Identify team member responsibilities using the matrix below.

|               | Feature 1 | Feature 2 |
|---            |-----------|-----------|
|**Frontend**   | Person A  | Person B  |
|**Backend**    | Person C  | Person D  |

* **GITLAB**: 
    - team members should self-assign issues appropriate to them.
    - you may add issues as needed.