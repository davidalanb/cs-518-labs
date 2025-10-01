from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from typing import cast

from accounts.data.user_manager import UserManager
from accounts.data.user_api import UserAPI

accounts = Blueprint('accounts', __name__,
                        template_folder='templates')

def get_uapi() -> UserAPI:
    """A type-hinted getter for the UserAPI."""
    return cast(UserAPI, current_app.uapi)

@accounts.route('/users/create', methods=['POST', 'GET'])
def create():
    ''' on GET, serve user create form
    on POST, get form data and update'''

    return "create user"

@accounts.get('/users/')
def users():
    return "view users"

@accounts.route('/users/<username>', methods=['POST', 'GET'])
def view(username):
    ''' on GET, serve populated user update form
    on POST, get form data and update user'''

    return "view / update users"

@accounts.post('/users/delete/all')
def delete_all():
    return "delete all users"

@accounts.post('/users/delete/<username>')
def delete(username):
    return "delete user"