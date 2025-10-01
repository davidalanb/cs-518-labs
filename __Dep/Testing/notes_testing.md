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








