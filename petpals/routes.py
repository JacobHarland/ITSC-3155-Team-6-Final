from encodings import utf_8
from flask import redirect, render_template, flash, url_for
from petpals import app, db, bcrypt
from petpals.models import User, Post
from petpals.forms import SignupForm, LoginForm
from flask_login import login_user

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
    form = SignupForm()
    # displays a message if data was sent
    if form.validate_on_submit():
        # bcrypt, hashes a password from form and decodes it as a string instead of bytes with utf-8
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. You are now able to login. Welcome to PetPals!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # searches database to see if email has been created or exists        
        user = User.query.filter_by(email=form.email.data).first()
        # checks if user exists and password verifies with db
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Login failed, please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.get('/forum')
def forum():
    return render_template('forum.html')

@app.get('/post')
def post():
    return render_template('post.html')

@app.get('/post_form')
def post_form():
    return render_template('post_form.html')

@app.post('/post')
def create_post():
    # TODO: Add post to DB
    # TODO: Redirect to post
    return redirect('/post')

