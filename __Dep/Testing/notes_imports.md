# Note on imports

* There are two scenarios:
    - running unit tests from a subdirectory (e.g., /accounts/data)
    - running the app from your project root (/)
    
## Top-level imports

* importing in tests
    - test_user_manager can import directly since it will be run from the /accounts/data/ directory.

test_user_manager.py
```python
from db_manager import DBManager
from user_manager import UserManager
```

* importing in app
    - app needs to import with a path, since it will be run from the root directory.

app.py
```python
from accounts.data.db_manager import DBManager
from accounts.data.user_manager import UserManager
```

## Imports from imports


