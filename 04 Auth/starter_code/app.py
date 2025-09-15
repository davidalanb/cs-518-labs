# other imports

import json
from flask import Flask
from flask_login import FlaskLoginClient, LoginManager

from accounts.data import user_api, user_manager

from accounts.routes import accounts
from accounts.user_login import UserLogin

with open('config.json') as f:
    config = json.load(f)

#---------------------------------------

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#------------------ databases -------------------------

db_url = config.get('DATABASE_URL')
db_db = config.get('DATABASE_DB')
db_col = config.get('DATABASE_COL')

umngr = user_manager.UserManager(db_url, db_db, db_col)
app.um = user_api.UserAPI(umngr)

#-------------------blueprints--------------------

app.register_blueprint(accounts)

#------------------Login------------------------------

app.test_client_class = FlaskLoginClient 
UserLogin.setup_db(app.um)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    print('loading user')
    return UserLogin.get(user_id)

#---------------------------------------------

## routes 
# (code omitted)

if __name__=="__main__":
    app.run(debug=True)
