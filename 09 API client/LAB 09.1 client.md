# Client

* app_project_root <-- or whatever, where your flask app is
    - src/
        - clients/
            - exceptions.py
            - user_client.py
            
* The user_client will have the same interface as user_api (from earlier labs)
* The key difference between them is that user_client will raise exceptions 
    - e.g. raise ResourceNotFound rather than return None