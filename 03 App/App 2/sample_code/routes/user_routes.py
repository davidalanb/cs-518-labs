import requests
from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
import json

from clients.user_client.user_client import UserClient

url = 'http://127.0.0.1:8000'
# url = f'https://{your-service-name}.azurewebsites.net'
client = UserClient(url)

user_routes = Blueprint('user_routes', __name__)
tmp = 'user_templates'

@user_routes.get("/users/")
def list_users():

    # TODO: get user data using your API (directly or with a client)
    # TODO: pass data to render_template
    us = []

    return render_template(f'{tmp}/users.html', users=us)

@user_routes.get('/users/<username>')
def view_user(username):

    # TODO: get user data
    # TODO: handle 404 error appropriately (with flashing)
    u = None

    return render_template(f'{tmp}/user.html',user=u)

@user_routes.route('/create_user', methods=['POST', 'GET'])
def create_user():

    if request.method == 'GET':
        return render_template('create_user.html')
    
    else:

        # TODO: get form data
        # TODO: use API to create user
        # TODO: handle 409 appropriately (with flashing)

        flash('not implemented')
        return redirect(url_for('user_routes.list_users'))


@user_routes.post('/delete_user/<_id>')
def delete_user(_id):

    # TODO: delete user 
    
    flash('not implemented')
    return redirect(url_for('user_routes.list_users'))
