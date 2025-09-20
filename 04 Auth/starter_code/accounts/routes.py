from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from accounts.user_login import UserLogin
# um = UserAPI()

'''
    Update for auth lab: use current_app.um wherever you used um before
'''

accounts = Blueprint('accounts', __name__,
                        template_folder='templates')

#---------------------- CRUD routes -----------------------

'''
    CRUD routes from previous lab
'''

#------------------- login routes---------------------------

@accounts.route('/login', methods=['GET','POST'])
def login():
    '''on GET, serve login page.  on POST, authenticate and login
    use current_app.um to access UserAPI / UserManager
    '''

    if request.method=='GET':
        return render_template('login.html')

    users = None

    ''' TODO
    # get username and password from form
    # read user using the 'authenticate' method
    '''    

    if users:
        u = users[0]

        # TODO: get values from u to pass to UserLogin
        ul = UserLogin(None,None,None)

        login_user(ul)
        flash('logged in')
        return redirect(url_for('index'))
    else:
        flash('login unsuccessful')
        return redirect(url_for('accounts.login'))

@accounts.route("/logout")
@login_required
def logout():
    logout_user()
    flash('logged out')
    return redirect(url_for('index'))
