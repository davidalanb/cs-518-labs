# other imports

from flask import Flask
from flask_login import LoginManager, login_user, login_required, logout_user
from accounts.user_login import UserLogin

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    print('loading user')
    return UserLogin.get(user_id)

## routes 
# (code omitted)
