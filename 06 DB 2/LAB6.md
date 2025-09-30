# Database 2 - Profiles

* Implementing DB capabilities for Profile management

## Recommended steps

1. Setup directory structure
2. Create data models
3. Implement data management

## Setup

* This module will carry your Profile management capabilities
* Create the directory structure below.

```
* accounts/       <-- unchanged
* profiles/       <-- new for this week
    * data/
        - profile_models.py
        - profile_manager.py
        - profile_api.py
        - test_profiles.py
        - db_manager.py         <-- copied from accounts/data
    * templates/
    * routes.py
* templates/
* app.py
* config.json       <-- switch from this
* config.py         <-- to this
* etc.
```

## Add new methods to db_manager

create_index:

* creates an index. Defaults to unique.

```python
# put create_index after __init__

def create_index(self,ix, unique=True):
    self.col.create_index(ix, unique=unique) 
```

add_to_set:

* this will take an id and a fieldname, and add each item provided
* remember data_manager is generic
* Assumptions:
    - pid is a string representation of an ObjectId
    - field is a string field name.  The field itself should be a list type
    - add_these is a list of strings

```python
# Put add_to_set with update method(s).

def add_to_set(self,pid: str,field: str,add_these: list[str]):
    '''take an id and a set fieldname, and add each item provided'''

    r = self.col.update_one({'_id':pid},
            { "$addToSet": { field: {'$each': add_these } }}
    )

    return r.modified_count   
```

## Create data models

* Provided in repo.

## Component relationships

* Relationships:
    - profile_manager should have an association relationship with db_manager
        - in lab 2 we used inheritance (pm IS-A dbm), but...
        - now we are switching to association (pm HAS-A dbm)
    - profile_api has association relationship with profile_manager (api HAS-A pm)
        - this is the same as before
        - however - there are some differences in the implementation

* Responsibilities:
    - db_manager does DB operations with pymongo
    - profile_manager does business logic (methods specific to your domain / data model)
    - profile_api validates

* Carefully review the starter code.

## Implementation

### Profile Manager

### Profile API



