import importlib
import sys
from flask import Flask, render_template

print(sys.path[0])

from accounts.routes import accounts

from accounts.data.user_api import UserAPI
from accounts.data.user_manager import UserManager
import config
from utils.db_manager import DBManager

app = Flask(__name__, template_folder="main/templates")
app.register_blueprint(accounts)
app.secret_key = '<YOUR SECRET KEY>'

cfg = config.USER_CONFIG
dbm = DBManager(cfg.DB_URL_LOCL, cfg.USER_DB, cfg.USER_COL)
umngr = UserManager(dbm)
app.uapi = UserAPI(umngr)

app.teardown_appcontext(dbm.close)

@app.route('/')
def hello():
    ''' serve index.html '''

    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)