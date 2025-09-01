from flask_login import UserMixin

from accounts.data.user_api import UserAPI
um = UserAPI()

class UserLogin(UserMixin):
   
    def __init__(self,user_id,username, admin=None):
        self.id = user_id
        self.username = username
        self.admin=admin

    @staticmethod
    def get(user_id):
        ''' get user by id; construct and return User object'''

        u = None
        # TODO: read user by id

        if u:
            # TODO: get id, username, admin fields
            return UserLogin(None, None, None)
