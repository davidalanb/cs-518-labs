# Continuous integration / continuous deployment

## Automated regression testing

* Create a 'tests' directory parallel to your 'src' directory

```
* project/
    * src/
        - blueprints/accounts/      <-- we've been just calling this 'accounts' 
            - data/
        - templates/
        - app.py
        - config.py                 <-- config file for running app
    * tests/
        - test_accounts/
            - test_data/
                - config.json       <-- config file for testing
                - test_dbm.py       <-- test file for DB lab
            - test_users.py         <-- test file for App lab
            - test_auth.py          <-- test file for Auth lab
    * run_tests.py                  <-- test runner (given in lab files)
```

## Fixing your imports

* At first, you won't be able to run your tests individually due to import issues.
* The hacky way to solve this is to use a relative path:

```python
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(FILE_PATH, '..','..','..','src')
sys.path.append(SRC_DIR)
```

* A better way is to install your project with pip.
* At the top level (adjacent to 'src'), create a file pyproject.toml 

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-project"
version = "0.1.0"
dependencies = []

[tool.setuptools.packages.find]
where = ["src"]
```

* from the root, run this (don't miss the dot):

```
pip install -e .
```

## Loading config files

* If you're loading variables from a config file into your tests, you'll need to set the file path relative to the test file's location.
    - this will ensure that it still works even when you run all tests from the root directory.

```python
script_dir = os.path.dirname(__file__)
config_path = os.path.join(script_dir, 'config.json')

with open(config_path) as f:
    config = json.load(f)

# etc.
```

## Running your tests

* try running the run_tests.py file.
* You should see test results in the terminal.








