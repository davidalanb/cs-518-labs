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
My profile:

* GET /profile - view profile page.  if the user doesn't have a profile, this should automatically create one
* POST /profile - update profile

Viewing profiles:

* GET /profiles/
* GET /profile/<profile> - view another user's profile

Creating adventures:

* GET /adventures/create - get form to create adventure
* POST /adventures/create 

Browsing adventures:

* GET /adventures/ - get a listing for all adventures
* GET /adventures/<profile> - see adventures by profile 
* GET /adventures/<profile>/<adventure> - see a specific adventure
```
