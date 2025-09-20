import json
from flask import Flask, render_template
from flask_login import LoginManager

from accounts.data import user_api, user_manager
from accounts.user_login import UserLogin
from accounts.routes import accounts

#-------------------setup-----------------------

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#------------------ databases -------------------------

with open('config.json') as f:
    config = json.load(f)

db_url = config.get('DATABASE_URL')
db_db = config.get('DATABASE_DB')
db_col = config.get('DATABASE_COL')

umngr = user_manager.UserManager(db_url, db_db, db_col)
app.um = user_api.UserAPI(umngr)

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