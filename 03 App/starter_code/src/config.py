class DB_CONFIG:

    DB_URL_DEPL = "<YOUR MONGODB ATLAS URL"
    DB_URL_LOCL = "mongodb://localhost:27017"

class DB_TEST_CONFIG(DB_CONFIG):
    ''' for testing generic DBManager '''

    TEST_DB = "test_db"
    TEST_COL = "items"  

class USER_CONFIG(DB_CONFIG):

    USER_DB = "user_db"
    USER_COL = "users"
    X = "X"


     
