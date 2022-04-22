from datetime import datetime

from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer

from petpals import app, db, login_manager


# https://flask-login.readthedocs.io/en/latest/
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# test data
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(18), nullable=False)
    username = db.Column(db.String(18), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    biography = db.Column(db.TEXT)
    _image_file = db.Column('image_file', db.String(20))
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    @property
    def image_file(self):
        if self._image_file is None:
            return 'default.jpg'
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        self._image_file = image_file

    @property
    def image_path(self):
        return f'/static/images/profile_pictures/{self.image_file}'

    # creates a temporary password to log in a user
    def get_reset_token(self):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    # tries to load created reset token, if exception return none, if no exception return user id
    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, expires_sec)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Pet(db.Model):
    pet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(18), nullable=False)
    species = db.Column(db.String(45), nullable=False)
    subspecies = db.Column(db.String(45))
    color = db.Column(db.String(45))
    tagline = db.Column(db.String(150))
    image_file = db.Column(db.String(45))
    biography = db.Column(db.Text, nullable=False)
    img1_path = db.Column(db.String(45))
    img2_path = db.Column(db.String(45))
    img3_path = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Profile('{self.name}', '{self.species}', '{self.subspecies}', '{self.color}', '{self.tagline}', '{self.biography}')"
