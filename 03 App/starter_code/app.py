from flask import Flask
from accounts.routes import accounts

from accounts.data.user_api import UserAPI
um = UserAPI()

app = Flask(__name__)
app.register_blueprint(accounts)

@app.route('/')
def hello():
    ''' serve index.html '''

    return 'Hello, World!'