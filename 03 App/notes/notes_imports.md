# Note on imports

* There are two scenarios:
    - running unit tests from a subdirectory (e.g., /accounts/data)
    - running the app from your project root (/)
    
## Importing

### Importing from adjacent files

* test_user_manager can import directly since it will be run from the /accounts/data/ directory.
* this is also true when you're importing, e.g. db_manager into user_manager.

test_user_manager.py
```python
from db_manager import DBManager
from user_manager import UserManager
```

### Importing from subdirectories

* When you import in app.py you need to specify a path.
* But now, the imports won't work when you run the test

app.py
```python
from accounts.data.db_manager import DBManager
from accounts.data.user_manager import UserManager
```

## Solutions

## Run your tests from a test runner

* you can write a script that will run your tests

## Installing local project

* install your project with pip.
* At the project root (adjacent to 'src'), create a file pyproject.toml. 
* from the root, run this (don't miss the dot):
```
pip install -e .
```


