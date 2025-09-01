from flask import Blueprint, flash, redirect, render_template, request, url_for

accounts = Blueprint('accounts', __name__,
                        template_folder='templates')

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

@accounts.post('/users/delete/<username>')
def delete(username):
    return "delete user"