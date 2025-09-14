from flask import Flask
from accounts.routes import accounts

app = Flask(__name__)
app.register_blueprint(accounts)
app.secret_key = '<YOUR SECRET KEY>'

@app.route('/')
def hello():
    ''' serve index.html '''

    return 'Hello, World!'

if __name__=="__main__":
    app.run(debug=True)