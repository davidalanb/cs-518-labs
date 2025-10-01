class TEST_CONFIG:

    #DB_URL = "<ATLAS CLOUD DB URL>"
    DB_URL = "mongodb://localhost:27017"

    TEST_DB = "test_db"
    TEST_COL = "items"  

class USER_CONFIG(TEST_CONFIG):

    USER_DB = "user_db"
    USER_COL = "users"

class GUIDE_CONFIG(TEST_CONFIG):
    
    GUIDE_DB = "guide_db"
    PROFILE_COL = "profiles"
    ADV_COL = "adventures" 

     
