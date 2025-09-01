from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from accounts.user_login import UserLogin
from accounts.data.user_api import UserAPI
um = UserAPI()

accounts = Blueprint('accounts', __name__,
                        template_folder='templates')

@accounts.route('/login', methods=['GET','POST'])
def login():

    if request.method=='GET':
        return render_template('login.html')

    users = None

    ''' TODO
    # get username and password from form
    # set users (read users from db by query)
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
