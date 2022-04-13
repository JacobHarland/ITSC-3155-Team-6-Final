import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv('dbuser', 'root')
db_pass = os.getenv('dbpass')
db_host = os.getenv('dbhost', 'localhost') #move this to wherever the "main" app file is
db_port = os.getenv('dbport', 3306)
db_name = os.getenv('dbname')
secret_key = os.getenv('secretkey')

connect = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

app = Flask(__name__)

# Move to env
# protects against modifying cookies and crosssite request forgery attacks
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# login_required needs to know where login route is.
login_manager.login_view = 'login'
# changes styling, info is bootstrap coloring
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')
mail = Mail(app)

from petpals import routes