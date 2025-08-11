## Flask 1

Index:
* Create base route ('/') with hello_world example
* Create an index page ('templates/index.html') and user render_template to serve it at the base route.

Accounts page:
* Create accounts route ('/accounts')
* Serve up the acounts page ('templates/accounts.html')
* Add link from index to accounts page using url_for

List users:
* Create user listing route  ('/list_users')
* Create a link from the accounts page to the user listing page ('templates/list_users.html')
* In the list_users route, you will need to get the user data.  You have two options for doing this:
  * A) mockup some data that is validated by your user models / API spec.
  * B) connect to your actual user API.
* After getting the data, pass it to render_template
* In your listing page, use a jinja for-loop to create a list or table of users.

View user:
* Create user view route with a route parameter for id or username ('/view_user/<username>')
* Make it so that your user listing page links to individual users
* Get the data and use it to render a view for that user.