# App 2 - Profiles

## Setup blueprints

### profiles/routes.py

* create the blueprint:

```python 
profiles = Blueprint('profiles', __name__,
                        template_folder='templates')
```

* Add a method to access a typed profile API:

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

## Implement routes and templates

### Profile routes

* you can see the required routes in project_root/src/profiles/routes.py
* blank template files in profiles/templates

### Updates to accounts

* note that there is one new endpoint to add to accounts/routes.py

``` python
@accounts.get('/users/{username}/profiles/)
def get_user_profiles(username):
   ''' get profiles by username 
   show a listing in a table
   THIS ENDPOINT GOES IN accounts.routes'''
```

* You will also need to implement a template in accounts/templates for listing profiles by username.