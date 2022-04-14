from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from petpals import db
from petpals.forms import UpdateAccountForm
from petpals.utils import save_picture

router = Blueprint('post_router', __name__, url_prefix='/profile')


@router.route('/user')
def profile_user():
    # Replace with pet's profile picture and recent images from DB
    # If there is no picture, use the default picture
    profile_picture = "/static/images/pet_pictures/temp/Xeno-0.jpg"
    if profile_picture is None:
        profile_picture = "/static/images/profile_pictures/default.jpg"
    return render_template('profile/user_profile.html', profile_picture=profile_picture)


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
        return redirect(url_for('profile_router.profile_user'))
    # auto populates fields with users current information
    elif request.method == 'GET':
        form.fullname.data = current_user.fullname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.biography.data = current_user.biography
    image_file = url_for(
        'static', filename='/images/profile_pictures/' + current_user.image_file)
    return render_template('edit_profile.html', title='Edit Profile', image_file=image_file, form=form)


@router.route('/pet')
def profile_pet():
    # Replace with pet's profile picture and recent images from DB
    images = ("/static/images/pet_pictures/temp/Xeno-0.jpg",
              "/static/images/pet_pictures/temp/Xeno-1.jpg", "/static/images/pet_pictures/temp/Xeno-2.jpg")
    return render_template('profile/pet_profile.html', profile_picture=images[2], recent_photos=images)


@router.route('pet/edit')
@login_required
def profile_pet_edit():
    pass
