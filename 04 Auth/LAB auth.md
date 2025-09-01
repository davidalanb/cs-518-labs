<!-- https://docs.google.com/document/d/1MIbHXfZYczmQrDQaN9bNHBA94PdQBPlyv8RwPohub3k/edit?tab=t.0  -->

# Implementing login in your app

## Grading

We will run your app and also look at the code:

* [8] Authentication: login / logout with message flashing
* [8] Authorization: customized views and restricted access
* [4] Repo and code organization and clarity

## Installation

use pip to install:
```
pip install flask_login
```
**IMPORTANT**: add flask_login to your requirements.txt for your web_app

## Implementation

### Setup

* add the new code from starter_code/app.py to your app.py
    - imports
    - login_manager initialization
    - load_user function

### UserLogin object

* copy user_login.py from starter_code/accounts to your corresponding directory
    - implement the missing code

* TEST: you can do some testing (make sure it doesn't blow up)

### Login and logout routes

* add the login and logout routes from starter_code/accounts/routes.py to your corresponding file
* GET login
    - create ./accounts/templates/login.html, and add a login form
* POST login
    - implement the  missing code

* TEST: at this point, you can test your login / logout functionality.

## Customizing views, authorization

* see starter_code/templates/index.html
    - add something like this to your code to customize the landing page

* use conditional logic in your header to show only the following:
    - not logged in: show only Home, Login, Signup
    - logged in 
        * non admin: Home, Profile, Logout
        * admin: non-admin, plus Create User, View Users

* ensure that each user can only access the appropriate content
    - use @login_required and/or conditional logic with current_user in your routes