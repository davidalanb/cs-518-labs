## Lab 3 - Data management

Goal:
* Develop UserManager for User DB management

Submission:
* This is an individual assignment
* Submit your work to your individual repo on Gitlab

### Part 1

Part 1: 
* Implement these methods of UserManager:
    * __init__
    * reset
    * create_user
    * read_user
    * read_users
    * update_user
    * delete_user
* Implement tests that execute each method at least once

Submission part 1:
* user_manager/
    - UserManager.py 
    - user_models.py
    - user_tests.py

### Connect to MongoDB Atlas

Login to mongoDB Atlas in your browser:
* Database > Clusters > Create / Connect > Drivers
    - Copy URI (starts with mongodb+srv)
* Security > DB Access > Users
    - Get username and password
    - update <password> in your URI

### Configure Atlas for access from Functions App

* Sign into MongoDB Atlas
* Security > Network Access > Add IP Address
* Add this Entry: 0.0.0.0/0