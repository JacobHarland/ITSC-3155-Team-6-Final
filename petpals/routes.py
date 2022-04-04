from flask import redirect, render_template, flash, url_for
from petpals import app
from petpals.models import User, Post
from petpals.forms import SignupForm, LoginForm

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
       flash(f'Account created for {form.username.data}!', 'success')
       return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # test data 
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else: 
            flash('Login failed, please try again', 'danger')
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

