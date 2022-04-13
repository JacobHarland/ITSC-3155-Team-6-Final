from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from flask_mail import Message
from petpals import app, bcrypt, db
from petpals.blueprints.profile_blueprint import router as profile_router
from petpals.forms import LoginForm, SignupForm, RequestResetForm, ResetPasswordForm
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

# sends the email using Flask-Mail
def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Petpals Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    message.body = f'''To reset your Petpals password, please visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request, ignore this email and no changes will be made
'''

@app.route('reset_password', methods=['GET', 'POST'])
def reset_request():
    # if user is logged in, clicking reset password redirects to home
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RequestResetForm()
    # gets the email of the user who submitted the password request
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['Post', 'GET'])
def reset_token(token):
    # if user is logged in, redirects to home
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_token(token)
    # if verify_reset_token returns none, then the token is invalid or expired
    if user is None:
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm
    if form.validate_on_submit():
        # bcrypt, hashes a password from form and decodes it as a string instead of bytes with utf-8
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been reset. You are now able to login. Welcome to PetPals!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

app.register_blueprint(profile_router)
