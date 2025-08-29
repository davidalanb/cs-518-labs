# Lab 3 - Data management

Goal:

* Develop UserManager for User DB management

Submission:

* Sign up for the course on Gradescope using this code: 7X7RNJ
* Submit this files to assignment "Database 1":
    - db_manager.py

## Setup

Setup:

* Create the initial directory structure for your project.  In this example, demo-project is the root of my repo:
    - demo-project/app/users/data
* Copy the files from the "starter_code" directory into this directory.

Notes:

* The class will be building a project week-by-week and organization is essential.  
* The professor and TAs will also be reviewing your repos and enforce good organization!

## User models

Explore the user models:

* See "user_models.py" in the starter_code folder
    - these models are implemented for you
* See "validate_users.py" 
    * Describe the three users / cases here
    * What result do you get in each case?  why?

## User DB management

Init:

* open "user_manager.py" and "db_manager.py"
* review the __init__ functions in both of these.
    - these are both implemented for you
* what is going on here?

Tests:

* now open "test_users.py".
* review the first 2 tests - basic and unique.
* make sure you understand each line.

Delete_all

* Review "delete_all" in db_manager.py

Create and read:

* in "db_manager.py" implement create and read_by_id
* when you create, you should set the new User's id to a unique string like this:

```python
d['_id']=str(ObjectId())
```

Reads, update, and delete:

* review the remaining tests in "test_users.py"
* implement the remaining methods in db_manager.py, testing as you go

Tips:

* be sure to use "_id" when querying by id 
* when you are returning many, you should cast the Cursor to a list, like this (pseudocode):

```
docs = find()
return list(docs)
```

## Notes

* You may notice this line in "user_models.py":

``` python
id: str = Field(alias='_id',default=None)
```

* mongoDB uses _id for a unique id.  However, pydantic ignores fields that start with underscore.  
    - using an alias is a workaround for this






