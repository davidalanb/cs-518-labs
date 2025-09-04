from flask import Flask
from accounts.routes import accounts

app = Flask(__name__)
app.register_blueprint(accounts)

@app.route('/')
def hello():
    ''' serve index.html '''

    return 'Hello, World!'