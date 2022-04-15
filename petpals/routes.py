from flask import render_template

from petpals import app
from petpals.blueprints.auth_blueprint import router as auth_router
from petpals.blueprints.post_blueprint import router as post_router
from petpals.blueprints.profile_blueprint import router as profile_router


@app.get('/')
def index():
    return render_template('index.html', title="Home")


@app.get("/about")
def about():
    return render_template('about.html', title="About Us")


@app.get("/faq")
def faq():
    return render_template('faq.html', title="FAQ")


@app.get('/forum')
def forum():
    return render_template('forum.html')


app.register_blueprint(profile_router)
app.register_blueprint(post_router)
app.register_blueprint(auth_router)
