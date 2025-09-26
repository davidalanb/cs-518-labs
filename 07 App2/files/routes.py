from datetime import datetime
from functools import wraps
from flask import Blueprint, current_app, flash, redirect, render_template, abort, request, url_for
from flask_login import current_user, login_required

# TODO: fix this
from blueprints.guides.data.profile_api import ProfileAPI

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

    # um = cast(UserAPI, current_app.um)
    # pm = cast(ProfileAPI, current_app.pm)

    prof = get_pm().read_by_profile_name(profile_name)

    return render_template('profile.html', profile=prof)#, username = un)    

@profiles.post('/profiles/<profile_name>/add-skill')
def update_profile(profile_name):

    update = request.form

    pid = update.get('profile_id')
    new_skill = update.get('skill')

    update_count = get_pm().add_skills(pid, [new_skill])
    if update_count:
        flash(f"added {new_skill}")
    else:
        flash("something went wrong updating skills")

    return redirect(url_for('profiles.profile', profile_name=profile_name))


# @profiles.route('/adventures/create', methods=['GET','POST'])
# def create_adventure():

#     if request.method=='GET':
#         return render_template('create_adventure.html')

#     uid = current_user.id

#     print(request.form)
#     dt = request.form.get('date') + ' ' + request.form.get('time')
#     # dt = datetime.strptime(dt, "%Y-%m-%d %H:%M")

#     # profiles = request.form.get('profiles').split(',')
#     # profiles = [s.strip() for s in profiles]

#     json_data = {
#         'user_id':uid,
#         'name':request.form.get('name'),
#         'datetime':str(dt)#,
#         # 'profiles':profiles
#     }

#     # TODO: validate
#     a = Adventure(**json_data)

#     result = current_app.am.create(a.model_dump())
#     if result:
#             flash('added adventure')
#             return redirect(url_for('profiles.view_adventures'))

#     return "something went wrong"

# # @profiles.get('/adventures/me')
# # def my_adventures():

# #     uid = current_user.id
# #     advs = current_app.am.read({'profile_id',uid})
# #     return advs
    
# @profiles.get('/adventures/')
# def view_adventures():

#     advs = current_app.am.read_all()
#     advs = AdventureCollection(adventures=advs).model_dump()
#     # print(advs.adventures.model_dump())

#     return render_template('adventures.html',advs = advs.get('adventures'))
