from flask import Flask, render_template
from routes.user_routes import user_routes
# from course_routes import course_routes

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.register_blueprint(user_routes)
# app.register_blueprint(course_routes)

@app.get("/hello")
def hello():
    return "Hello world!"

@app.get("/")
def index():
    return render_template('index.html')