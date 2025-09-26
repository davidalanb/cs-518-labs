# App 2 - Profiles

## Recommended steps

* Setup blueprints in profiles/routes.py and app.py

### Setup for app

* Create file profiles/routes.py
* in routes.py, create the blueprint:
```
profiles = Blueprint('profiles', __name__,
                        template_folder='templates')
```
* in app.py: 
    - Register blueprint 
    - setup ProfileManager
    
```python
app.register_blueprint(profiles)
```

```python
# be sure to use different values for profile_db and profile_col
# you can set these up in your config file
dbm = DBManager(db_url, profile_db, profile_col)
pmngr = ProfileManager(dbm)
app.pm = pmngr
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
