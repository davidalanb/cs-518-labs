from datetime import datetime
from functools import wraps
from flask import Blueprint, current_app, flash, redirect, render_template, abort, request, url_for
from flask_login import current_user, login_required

from profiles.data.profile_api import ProfileAPI

profiles = Blueprint('profiles', __name__,
                        template_folder='templates')

from typing import cast

def get_pm() -> ProfileAPI:
    """A type-hinted getter for the ProfileManager."""
    return cast(ProfileAPI, current_app.pm)

@profiles.post('/profiles/delete/all')
def delete_all():
    ''' for testing '''
    
    n = get_pm().delete_all()
    return f"deleted {n} profiles"

@profiles.get('/profiles/')
def profiles():

    profs = get_pm().read_all() 

    # TODO: implement profiles.html
    return render_template('profiles.html',profs=profs)

#======================= TODO: IMPLEMENT THESE ===========

@profiles.route('/profiles/create', methods=['GET','POST'])
def create_profile():
    '''
    on GET, serve profile create form
    on POST, get form data and create
        get profile_name from form
        get username from current_user

    on success, redirect to profile
    on fail, redirect back here
    '''

    return "not implemented yet"

@profiles.get('/profiles/<profile_name>')
@login_required
def profile(profile_name):

    '''get profile for current user'''  

@profiles.post('/profiles/<profile_name>/add-skill')
def add_skill(profile_name):

    ''' add skill from form
    form should have profile_id and skill
    redirect to this profile'''
