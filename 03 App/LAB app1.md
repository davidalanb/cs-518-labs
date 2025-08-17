## Flask 1

### Submission and grading

* Add your updated code to your repo
  - make sure you follow the directory structure below
* Submit your repo URL to Canvas 
  - graders will pull your code and run your app
* Grading rubric below

### structure

app structure:
* app/
  * users/
    * data/
    * templates/
      * create.html
      * users.html		<- user listing page
    * routes.py
  * templates/
    * index.html
  * app.py

### Directions

Index:
* app.py: index route ('/')
* templates/index.html - welcome message

Blueprints:
* setup blueprints in app.py and users/routes.py
* in users/routes.py, setup routes to create and users.
* templates/header.html - dynamic links to index, create user, and view users

List users:
* users/routes.py: 
  * In the list_users route, you will need to get the user data.  You have two options for doing this:
    * A) mockup some data (helpful at first)
    * B) read data from your DB. (you'll need to do this anyway) 
  * After getting the data, validate it and pass it to render_template
* users.html: In your listing page, use a jinja for-loop to create a list or table of users.

Create user:
* users/templates/create.html:
  - create a form for submitting new user data
* users/routes.py: make a 'create' route that handles GET and POST
  - GET: serve create form
  - POST: get form data, validate, and make a DB create operation

View / update user:
* users/templates/view.html:
  - create a form for viewing / updating user data
* users/routes.py: make a view user route with a route parameter for username ('/view/<username>'), that handles GET and POST
  - GET: get user data and serve the populated view form
  - POST: get user form data to and update by user id
* users/templates/users.html: Make your user listing page link to individual users

Delete user:
* users/templates/view.html:
  - add a second form to delete user
* users/routes.py: make a delete route that performs the delete

Note:
* flash messages when necessary, and redirect appropriately

### Grading

criteria:
* [5] create user
    * GET: show create user form
    * POST: [fail] username taken -> reload with error msg
    * POST: [success] -> redirect to view user
* [5] view users
    * GET: show user listing with links to view/update users
* [5] view / update user
    * GET: show user update form with user data
    * GET: [fail] username not found -> redirect to view users with error msg
    * POST: [success] reload with success msg
* [5] delete user
    * POST: [success] -> user listing 