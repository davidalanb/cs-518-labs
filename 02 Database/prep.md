# Database 1 prep

Submission:

- You will submit code and notes for the concepts below.
- You can submit code and notes separately, or just well-commented code.
- There is nothing specific for you to implement - you should just get familiar with the concepts and DB operations below.
- Submit to Canvas, like a reading response.  
    - you should have about 400 words of code and other text, combined

## Setup

To work with MongoDB

* Setup a MongoDB Atlas account and create a free cluster
* [Optional] Install mongoDB locally
    * https://www.mongodb.com/docs/manual/administration/install-community/

### Connecting to MongoDB Atlas

Login to mongoDB Atlas in your browser:

* Database > Clusters > Create / Connect > Drivers
    - Copy URI (starts with mongodb+srv)
* Security > DB Access > Users
    - Get username and password
    - update <password> in your URI

### Configuring Atlas for access from anywhere

* Sign into MongoDB Atlas
* Security > Network Access > Add IP Address
* Add this Entry: 0.0.0.0/0

### Python libraries

Install pydantic and pymongo with the following terminal commands:

```
pip install pydantic
pip install pymongo
```

* Note: you may need to use "python -m pip" or "python3 -m pip" instead of just "pip"

## Review concepts

Review key python concepts (see references below):   
- dicts; classes and objects
- exceptions

Review pydantic
- basic model usage

Review pymongo tutorial(s) for key concepts:
* Connect to Db
* CRUD operations: 
    - Create: Adding new records to a database (insert)
    - Read: Retrieving data from a database (find)
    - Update: Modifying existing records in a database (update)
    - Delete: Removing existing records from a database (delete)

### References

Python references:
* https://www.w3schools.com/python/default.asp
* https://docs.python.org/3/tutorial/index.html 

Pydantic:
* https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage

Review pymongo tutorial(s):
- https://pymongo.readthedocs.io/en/stable/tutorial.html 
- https://www.w3schools.com/python/python_mongodb_getstarted.asp 