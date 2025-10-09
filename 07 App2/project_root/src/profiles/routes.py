from datetime import datetime
from functools import wraps
from flask import Blueprint, current_app, flash, redirect, render_template, abort, request, url_for
from flask_login import current_user, login_required

from accounts.data.user_api import UserAPI
from profiles.data.profile_api import ProfileAPI

profiles = Blueprint('profiles', __name__,
                        template_folder='templates')

from typing import cast

def get_um() -> UserAPI:
    """A type-hinted getter for the ProfileManager."""
    return cast(UserAPI, current_app.um)

def get_pm() -> ProfileAPI:
    """A type-hinted getter for the ProfileManager."""
    return cast(ProfileAPI, current_app.pm)

@profiles.post('/profiles/delete/all')
def delete_all():
    ''' for testing '''
    
    n = get_pm().delete_all()
    return f"deleted {n} profiles"

@profiles.get('/profiles/')
def read_profiles():

    profs = get_pm().read_all() 

    # TODO: implement profiles.html
    return render_template('profiles.html',profs=profs)

#======================= TODO: IMPLEMENT THESE ===========

@profiles.route('/profiles/create', methods=['GET','POST'])
def create_profile():
    '''
    on GET, serve profile create form
    on POST, get username and profile_name from form

    if username is not valid, flash a message and redirect here
    else create the profile and redirect to the new profile page
    '''

    return "not implemented yet"

@profiles.get('/profiles/<profile_name>')
@login_required
def profile(profile_name):
    '''get profile by profile name
    render profile_view with profile data
    profile view should:
        give profile name and username in a table
        show a list of skills
        have a form that allows you to add skills
        the form should have a hidden input with value equal to the profile id}
    '''  

"""
@accounts.get('/users/{username}/profiles/)
def get_user_profiles(username):
   ''' get profiles by username 
   show a listing in a table
   THIS ENDPOINT GOES IN accounts.routes'''
"""

@profiles.post('/profiles/<profile_name>/add-skill')
def add_skill(profile_name):
    ''' add skill from form
    form should have profile_id and skill
    add skill to profile skills and redirect back to the profile'''
