from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required
from petpals import bcrypt, db
from petpals.forms import ChangePassword, UpdateAccountForm
from petpals.models import User
from petpals.utils import save_profile_picture

router = Blueprint('profile_router', __name__, url_prefix='/profile')


@router.get('/user')
def profile_current_user():
    return redirect(url_for('profile_router.profile_user', username=current_user.username))


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
            picture_file = save_profile_picture(form.picture.data)
            # image_file is name in models.py
            current_user.image_file = picture_file

        current_user.fullname = form.fullname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.biography = form.biography.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile_router.profile_current_user'))
    # auto populates fields with users current information
    elif request.method == 'GET':
        form.fullname.data = current_user.fullname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.biography.data = current_user.biography
    image_file = '/static/images/profile_pictures/' + current_user.image_file

    return render_template('profile/edit_profile.html', title='Edit Profile', image_file=image_file, form=form)


@router.route('/user/edit/password', methods=['GET', 'POST'])
@login_required
def profile_user_edit_password():
    form = ChangePassword()

    # validate current password
    # bcrypt the new password
    # set the new password to current_user.fullname = form.fullname.data

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # checks if user exists and password verifies with db
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            current_user.password = hashed_password
            db.session.commit()
            flash(f'Your password has been updated!', 'success')
            return redirect(url_for('profile_router.profile_current_user'))        
        else:
            flash('Login failed, please check email and password', 'danger')
    return render_template('edit_password.html', title='Edit Password', form=form)


@router.route('/user/<username>/<pet_name>')
def profile_pet(username: str, pet_name: str):
    # pet = db.session.query(User, Pet).filter(
    #         User.username == username,
    #         Pet.name == pet_name
    #     ).first()
    
    user = User.query.filter_by(username=username).first()
    pet = user.pets.filter_by(name=pet_name).first_or_404()
    # Replace with pet's profile picture and recent images from DB
    return render_template('profile/pet_profile.html', pet=pet)


@router.route('pet/edit')
@login_required
def profile_pet_edit():
    pass
