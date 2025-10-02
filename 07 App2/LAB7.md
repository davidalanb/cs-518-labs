# App 2 - Profiles

## Recommended steps

* Setup blueprints in profiles/routes.py and app.py

## Setup for app

### profiles/routes.py

create the blueprint:

```python 
profiles = Blueprint('profiles', __name__,
                        template_folder='templates')
```

Add a method to access a typed profile API:

```python
from typing import cast

def get_pm() -> ProfileAPI:
    """A type-hinted getter for the ProfileAPI."""
    return cast(ProfileAPI, current_app.pm)
```

Using typed pm (e.g. to create a profile):

```python
# # instead of this
# current_app.pm.create(..)

# do this
get_pm().create(..)
```

### app.py

Register blueprint:
    
```python
app.register_blueprint(profiles)
```

setup ProfileManager:
* db_url can be the same one you used for users
* profile_db and profile_col should be different than what you used for user_db and user_col. 

```python
# set these up in your config file
dbm = DBManager(db_url, profile_db, profile_col)
pmngr = ProfileManager(dbm)
app.pm = ProfileAPI(pmngr)
```

### Implementing routes and templates

Required routes:

```
Creating profiles:

* GET /profiles/create          get profile create page
* POST /profiles/create         create profile

Viewing profiles:

* GET /profiles/                 list profiles
* GET /profiles/<profile_name>   view profile by profile name

Viewing user profiles:

* GET /users/<username>/profiles list profiles by username 

```
