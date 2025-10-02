# Managing imports for complex projects

## Notes

### Project root and src

Project root and src directory:
    - Your project root (e.g. "my_project") that is the parent of "src"
    - 'src' contains your project's code.  (e.g. app.py, accounts, etc.)

### Relative and absolute imports

* When you're running a test file that is adjacent to the source files being tested (for example, when test_users is run from accounts/data), you can use relative import statements.  
    - For example, ```from db_manager import DBManager```
    - you can use relative imports in all of your source files (db_manager, user_manager, user_api), as well as your test file (test_users)

* However, when you run app.py from a parent directory, those imports won't work.  In that case, you need to use an absolute import, which specifies a path from 'src'.
    - For example, ```from accounts.data.db_manager import db_manager```
    - YOu need to update imports in all of the files.

* If you change from the imports from relative to absolute, the relative imports won't work when you run the test from 'accounts/data'

## First: the Hacks

### Try-except

* We've been getting around this by using try-except blocks:
    - this will try the relative import, and if that doesn't work, it will use the absolute.
```
try:
    from db_manager import DBManager
except ModuleNotFoundError:
    from accounts.data.db_manager import db_manager
```

* Some problems with this:
    - We'll need try-except blocks like this in all of the files, which can get messy.
    - If a different ModuleNotFound error occurs (for example, in an import that is in the db_manager file), the except block can be erroneously entered.  This can cause headaches while debugging.
    - Ultimately, using try-except with imports like this is better suited for working with external imports.
    
### Path hacks

* Another option is to use a path hack in the test file
    - get the current file directory
    - traverse up the ancestor tree to get the 'src' directory
    - add 'src' to the path

```python
import sys
from pathlib import Path

current_file_dir = Path(__file__).resolve().parent
src_dir = current_file_dir.parent.parent
sys.path.insert(0, str(project_root))
```

* Benefits
    - now we only need this hack in the test files
    - the source files can just use absolute imports (from src), which is cleaner
* Some problems with this:
    - Path hacks are fragile and make your project structure difficult to understand and maintain. 
    - They break standard Python tooling and deployment.

## Now: the Solution

* The best solution to this is to install your local project in editable mode.

## Installing local project

* At the project root (e.g. my_project), create a file pyproject.toml. 
```
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-project"
version = "0.1.0"
dependencies = ["pydantic","pymongo","flask","flask-login"]

[tool.setuptools.packages.find]
where = ["src"]
```
* open a terminal at the root and install with this command (don't miss the dot):
```
pip install -e .
```

* Now your absolute imports should work everywhere.  No try-except, no path hacks.
    - this will work whether you keep your tests in 'src', or move them to a parallel directory 'tests'

