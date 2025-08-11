from flask import Flask, render_template
# from user_routes import user_routes
# from course_routes import course_routes

app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# app.register_blueprint(user_routes)
# app.register_blueprint(course_routes)

@app.get("/hello")
def hello():
    return "Hello world!"

@app.get("/")
def index():
    return render_template('index.html')

@app.get("/users/")
def list_users():

    # TODO: get user data using your API (directly or with a client)
    # TODO: pass data to render_template
    us = []

    return render_template('users.html', users=us)

@app.get('/users/<username>')
def view_user(username):

    # TODO: get user data
    # TODO: verify that user has been found and return appropriate
    # (probably better to flash a message then just give a 404 page)
    u = None

    return render_template('user.html',user=u)