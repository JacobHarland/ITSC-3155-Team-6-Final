import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Flask Secret Key
# Protects against modifying cookies and crosssite request forgery attacks
app.secret_key = os.getenv('SECRET_KEY')

# Bcrypt
bcrypt = Bcrypt(app)

# Login Manager
login_manager = LoginManager(app)
# login route for login_required
login_manager.login_view = 'auth_router.login'
# Changes styling, info is bootstrap coloring
login_manager.login_message_category = 'info'

# Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail(app)


from .auth.reset_password.routes import router as reset_password_router
from .auth.routes import router as auth_router
from .forum.post.reply.routes import router as reply_router
from .forum.post.routes import router as post_router
from .forum.routes import router as forum_router
from .home.routes import router as home_router
from .profile.routes import router as profile_router

# Register Blueprints
auth_router.register_blueprint(reset_password_router)
app.register_blueprint(auth_router)
post_router.register_blueprint(reply_router)
forum_router.register_blueprint(post_router)
app.register_blueprint(forum_router)
app.register_blueprint(home_router)
app.register_blueprint(profile_router)
