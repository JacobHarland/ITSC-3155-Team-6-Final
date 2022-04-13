from datetime import datetime
from petpals import db, login_manager
from flask_login import UserMixin

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
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
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
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Profile('{self.name}', '{self.species}', '{self.subspecies}', '{self.color}', '{self.tagline}', '{self.biography}')"
