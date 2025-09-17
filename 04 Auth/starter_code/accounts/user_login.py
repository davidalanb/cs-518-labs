# from accounts.data.user_api import UserAPI
# um = UserAPI()

'''
Works statically - UserLogin.setup_db, UserLogin.get
But also used to create instances of users for login purposes (current_user)
'''

from flask_login import UserMixin

class UserLogin(UserMixin):

    def __init__(self,user_id,username, admin=None):
        self.id = user_id
        self.username = username
        self.admin=admin

    # @staticmethod
    # def setup_db(um):
    #     UserLogin.um = um

    @staticmethod
    def get(user_id):
        ''' get user by id; construct and return User object
        use current_app.um to access UserAPI / UserManager'''

        u = None
        # TODO: read user by id

        if u:
            # TODO: get id, username, admin fields
            return UserLogin(None, None, None)
