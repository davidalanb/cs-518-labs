# already implemented in earlier labs
from utils.db_manager import DBManager
from accounts.data.user_models import *

# should inherit from DB manager
class UserManager:
    def __init__(self,dbm: DBManager):
        pass

    def authenticate(self, credentials) -> User:
        # 1. Fetch the user from the database.
        # The db_manager method is called with a simple query.
        username = credentials.get('username')
        password = credentials.get('password')

        user_in_db = self.dbm.read_one({'username': username,
                                        'password':password})
        return User(**user_in_db)