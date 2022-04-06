from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# protects against modifying cookies and crosssite request forgery attacks
app.config['SECRET_KEY'] = '3b05adb71fc2d58cb11457a257f37b35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from petpals import routes