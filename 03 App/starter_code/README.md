# Find a Guide

Name: 

Credits:

* any notes about collaboration, use of AI, etc.
* you can collaborate about ideas and even show code, but you shouldn't share code

## Repo structure

repo structure:
* project/
    * src/
        * accounts/
            * data/
                * user_api.py
                * user_manager.py
                * user_models.py
            * templates/
                * create.html
                * users.html
                * view.html
            * routes.py
        * main/
            * templates/
                * index.html 
        * utils/   
            * db_manager.py             <-- moved from accounts/data/
        * app.py
    * tests/
        * accounts/
            * data/
                * test_user_manager.py  <-- moved from accounts/data/
            * test_app_users.py
    * README.md

## Imports

* Imports have been changed so that they will work when you run app.py from the src/ directory
* e.g. in user_api.py

Old imports:
```
from user_manager import UserManager
from user_models import *
```
New imports:
```
from accounts.data.user_manager import UserManager
from accounts.data.user_models import *
```

## Imports in test_users

* Importing in test_users is tricky, because src/ and tests/ are adjacent.
* Here are a few ways to do this.
* The first is a hack but it will work "out of the box."

### Solution 1: Add directories to your path in test files (hack)

* You can see the hack in test_users.py
* test_users.py is in /tests/accounts/data, so we have to traverse up the ancestor tree to get to root
* after we get root, we can append root (/) and /src/.

```python
# get path for root_dir
# ancestors are: data, accounts, tests, and root
root_dir = Path(__file__).resolve().parent.parent.parent.parent

# add root and src to the path
sys.path.append(str(root_dir))
sys.path.append(str(root_dir/'src'))
```

### Solution 2: Install your local project in editable mode (better solution)

- install your project in editable mode:  https://pip.pypa.io/en/stable/topics/local-project-installs/ 
- run the command below from your src/ directory
```
python -m pip install -e path/to/SomeProject
```
- after this, the new imports (starting with accounts) should work anywhere

## Type hinting

* When you set configure your app you set app.uapi to an instance of your UserAPI
* This makes current_app.uapi available in your routes.
* However, you won't get type hints because it's dynamically loaded
* To get type hints, we can create a getter:

```python
from typing import cast

def get_uapi() -> UserAPI:
    """A type-hinted getter for the UserAPI."""
    return cast(UserAPI, current_app.uapi)
```

* we can use the getter like this:
```python
get_uapi().create(..)
get_uapi().read(..)
# etc.
```


