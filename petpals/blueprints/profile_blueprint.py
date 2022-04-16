from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required
from petpals import db
from petpals.forms import UpdateAccountForm
from petpals.models import User
from petpals.utils import save_picture

router = Blueprint('profile_router', __name__, url_prefix='/profile')


@router.get('/user')
def profile_current_user():
    return redirect(url_for('profile.profile_user', username=current_user.username))


@router.get('/user/<username>')
def profile_user(username: str):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('profile/user_profile.html', user=user)


@router.route('/user/edit', methods=['GET', 'POST'])
@login_required
def profile_user_edit():
    form = UpdateAccountForm()
    # updates user data
    if form.validate_on_submit():
        # calls method save_picture to save picture and give filename
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            # image_file is name in models.py
            current_user.image_file = picture_file

        current_user.fullname = form.fullname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.biography = form.biography.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile.profile_current_user'))
    # auto populates fields with users current information
    elif request.method == 'GET':
        form.fullname.data = current_user.fullname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.biography.data = current_user.biography
    image_file = '/static/images/profile_pictures/' + current_user.image_file

    return render_template('profile/edit_profile.html', title='Edit Profile', image_file=image_file, form=form)


@router.route('/pet/<name>')
def profile_pet(name: str):
    # Replace with pet's profile picture and recent images from DB
    images = ("/static/images/pet_pictures/temp/Xeno-0.jpg",
              "/static/images/pet_pictures/temp/Xeno-1.jpg", "/static/images/pet_pictures/temp/Xeno-2.jpg")
    return render_template('profile/pet_profile.html', profile_picture=images[2], recent_photos=images)


@router.route('pet/edit')
@login_required
def profile_pet_edit():
    pass
