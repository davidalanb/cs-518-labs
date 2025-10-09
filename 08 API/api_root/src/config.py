class USER_API_CONFIG:
    API_URL = "http://localhost:8000"

class TEST_CONFIG:

    # DB_URL = "<YOUR ATLAS URL>"
    DB_URL = "mongodb://localhost:27017"

    TEST_DB = "test_db"
    TEST_COL = "items"  

class USER_CONFIG(TEST_CONFIG):

    USER_DB = "user_db"
    USER_COL = "users"



     
