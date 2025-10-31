# Client

## Submission

* Test thoroughly on your machine before submitting to Gradescope
* Submit client code to Gradescope
    * Submit a zip file that contains the "clients" directory 

## Structure

* app_project_root <-- or whatever, where your flask app is
    - src/
        - clients/
            - exceptions.py
            - user_client.py
            - \_\_init\_\_.py       <-- add this for module recognition
        - app.py                <-- your flask app
        - (etc...)              <-- other files and folders

    - tests/
        - test_clients/
            - test_user_client.py - your API needs to be running 
            - test_user_client_mock.py - this is the test that GS will use
        - (etc...)
            
## Interface / integration

* The user_client will have the same interface as user_api (from earlier labs)
* The key difference between them is that user_client will raise exceptions 
    - e.g. raise ResourceNotFound rather than return None