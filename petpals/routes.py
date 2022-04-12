import os
import secrets
from fileinput import filename
from flask import flash, redirect, render_template, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from petpals import app, db, bcrypt
from petpals.forms import LoginForm, SignupForm, UpdateAccountForm
from petpals.models import Post, User

@app.get('/')
def index():
    return render_template('index.html', title="Home")

@app.get("/about")
def about():
    return render_template('about.html', title="About Us")

@app.get("/faq")
def faq():
    return render_template('faq.html', title="FAQ")

@app.route('/signup', methods=['GET','POST'])
def signup():
    # if user is logged in, clicking signup redirects to home
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    # displays a message if data was sent
    if form.validate_on_submit():
        # bcrypt, hashes a password from form and decodes it as a string instead of bytes with utf-8
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fullname=form.fullname.data, username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. You are now able to login. Welcome to PetPals!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    # if user is logged in, clicking login redirects to home
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # searches database to see if email has been created or exists        
        user = User.query.filter_by(email=form.email.data).first()
        # checks if user exists and password verifies with db
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # gets the page the user was trying to access 
            next_page = request.args.get('next')
            # ternary operator, if next page exists redirect to it, otherwise to index
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login failed, please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.get('/forum')
def forum():
    return render_template('forum.html')

@app.get('/post')
def post():
    return render_template('post.html')

@app.get('/post/form')
def post_form():
    return render_template('post_form.html')

@app.post('/post')
def create_post():
    # TODO: Add post to DB
    # TODO: Redirect to post
    return redirect('/post')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile')

def save_picture(form_picture):
    # random name for each file uploaded
    random_hex = secrets.token_hex(8)
    # _ for unused variables
    # returns and splits the text and file type of the file uploaded by user
    _, f_ext = os.path.splitext(form_picture.filename)
    # combine random hex with file extension in order to save it
    picture_filename = random_hex + f_ext
    # path of location to save the file
    picture_path = os.path.join(app.root_path, 'static/images/profile_pictures', picture_filename)

    form_picture.save(picture_path)

    prev_picture = os.path.join(app.root_path, 'static/images/profile_pictures', current_user.image_file)
    if os.path.exists(prev_picture) and current_user.image_file != 'default.jpg':
        os.remove(prev_picture)

    return picture_filename

@app.route('/profile/edit', methods=['GET','POST'])
@login_required
def edit_profile():
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
        return redirect(url_for('profile'))
    # auto populates fields with users current information
    elif request.method == 'GET':
        form.fullname.data = current_user.fullname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.biography.data = current_user.biography
    image_file = url_for('static', filename='/images/profile_pictures/' + current_user.image_file)
    return render_template('edit_profile.html', title='Edit Profile', image_file=image_file, form=form)
