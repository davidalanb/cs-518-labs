## Overview

Implement the ability to create, update, and delete users from your flask app.

### Create user 

Make a link to create_user on your home page or "accounts" page.

Implementing create_user:
* Make a create_user route that supports GET and POST
  * on GET, serve the form
  * on POST, 
    * get the form data 
    * make a request to your API to create a user
    * flash a message
    * redirect to user listing

### Update / delete user

Update / delete user:
* On the user detail page, make a link to a update/delete page.
* This page should have two forms:
  * one form to update the user
  * one form to delete the user

Update user:
* Make an update_user route that supports GET and POST
  * On GET, serve the update/delete page (described above)

The forms:
* the update_user form should submit a POST request to update_user route
* the delete_user form should submit a POST request to delete_user route

Implementing POST
* On POST to update or delete user
  * make a request to your API
  * flash a message
  * redirect:
    - to user detail after update
    - to user listing after delete

### Grading

code:
* app.py (and user_routes.py, if you used Blueprints)
* templates
demo:
* [sp25] submit screenshots
* [fa25] Submit short demo video showing the following:

--

criteria:
* create user
    * [fail] missing field -> reload with error msg
    * [success] -> user detail
* read users(s)
    * user listing with multiple users
    * click user -> user detail
* update password
    * [fail] password mismatch -> reload with error msg
    * [success] reload with success msg
* delete user
    * [fail] id mismatch -> reload / error
    * [success] -> user listing 
