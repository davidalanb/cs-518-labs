# Database 2


## Planning / design

Personas and stories:

* Dave - guide
    - "As Dave, I want to create a profile for my guide service, so that I can attract clients and grow my business."
    - "As Dave, I want to add my skills to my profile, so that potential clients can see my qualifications."
    - "As Dave, I want to be able to create adventures and associate them with my business."
* Jane - adventurer
    - "As Jane, I want to create a personal profile, so that I can join adventures and find adventure partners."
    - "As Jane, I want to browse adventures and see the skills required, so I can find an adventure that's right for me."
    - "As Jane, I want to sign up for an adventure, so that I can get updates and prepare."

Features:

- Setting up a profile
    - creating a profile
    - adding my skills
- Working with adventures
    - creating an adventure
    - browsing adventures 
        - (all adventures)
        - by guide / service
    - joining adventures

Data relationships:

* **User-profile**.  At first, we might want each user to have just one profile (*one-to-one*).  This simplifies things.  Later, we might want users to be able to have multiple profiles.  

* **Profile-adventure**.  A profile can be associated with many adventures (and vice-versa - *many-to-many*).
    
ERD:

* [Entity-Relationship Diagram](https://drive.google.com/file/d/1oRwl-XNePkP6AP9sSHcjhZ6qG9vKPEDu/view?usp=sharing)


## Recommended steps

1. Setup directory structure
2. Create data models
3. Implement data management
4. 

### Setup

* This module will carry your Profile and Adventure capabilities
* Create the directory structure:
    * You can refactor to have a "blueprints" or "modules" directory which contains your "accounts" and "guides" modules, but this is not strictly necessary
    * When you move db_manager.py to "utils," you'll need to update some imports in accounts/data.

```
* blueprints/
    * accounts/
    * guides/       <-- new for this week
        * data/
            - adventure_manager.py
            - adventure_api.py
            - models.py
            - profile_manager.py
            - profile_api.py
        * templates/
        * routes.py
* templates/
* utils/
    - db_manager.py     <-- new location for db_manager
* app.py
```

### Create data models

* See samples in repo

### Implement adventure_manager and profile_manager

* These will add methods to the generic DBManager
* You can also add convenience methods, for example methods for common queries.
* test thoroughly

```
* ProfileManager methods:
    - CRUD methods
    - add / remove skill(s)
    - convenience methods:
        - get profile(s) by user_id

* AdventureManager methods:
    - CRUD methods
    - add / remove guide(s) - profile_id
    - add / remove adventurer(s) - by profile_id
    - convenience methods:
        - get adventure(s) by profile_id
```

### Setup for app

* Create file blueprints/guides/routes.py
* in routes.py, create the blueprint:
```
guides = Blueprint('guides', __name__,
                        template_folder='templates')
```
* In app.py:
    - Register blueprint 
    - setup ProfileManager and AdventureManager
```
app.register_blueprint(guides)
```
```
pmngr = ProfileManager(db_url, guide_db, profile_col)
amngr = AdventureManager(db_url, guide_db, adv_col)
app.pm = pmngr
app.am = amngr
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
