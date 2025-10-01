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

## Running your tests

* try running the run_tests.py file.
* You should see test results in the terminal.

## Running your tests in VS Code

* In the command pallette (the search bar at the top), type:
```
> Preferences: Open Workspace Settings (JSON)
```
* or you can create .vscode/settings.json in your workspace root
* configure this file (see starter_code/.vscode for contents)
* create .env in your workspace root
```
PYTHONPATH=src
```
* now click the lab flask on the left panel
* you can run all of your tests or individual tests from this








