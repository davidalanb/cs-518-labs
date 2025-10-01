import json
from flask import Flask, render_template
from flask_login import LoginManager

import config

from utils.db_manager import DBManager
from accounts.data.user_api import UserAPI
from accounts.data.user_manager import UserManager
from accounts.user_login import UserLogin
from accounts.routes import accounts

#-------------------setup-----------------------

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#------------------ databases -------------------------

cfg = config.USER_CONFIG
dbm = DBManager(cfg.DB_URL_LOCL, cfg.USER_DB, cfg.USER_COL)
umngr = UserManager(dbm)
app.uapi = UserAPI(umngr)

#------------------------------------------

# register accounts after app.um has been defined
app.register_blueprint(accounts)

#-------------------Login stuff --------------------------

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    print(f'loading user {user_id}')
    u = UserLogin.get(user_id)
    return u

#------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)