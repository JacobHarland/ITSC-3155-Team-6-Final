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

    pets = db.relationship(
        'Pet', back_populates='owner', cascade="all, delete", lazy='dynamic'
    )
    posts = db.relationship('Post', back_populates='author', cascade="all, delete")
    replies = db.relationship('Reply', back_populates='author', cascade="all, delete")
    likes = db.relationship('ReplyLike', back_populates='user', cascade='all, delete')

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
        return f'/static/images/user/profile/{self.image_file}'

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
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    views = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    author = db.relationship('User', back_populates='posts')
    replies = db.relationship('Reply', back_populates='op', cascade="all, delete")

    def __repr__(self):
        return f"Post('{self.title}', '{self.timestamp}')"


class Reply(db.Model):
    reply_id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)

    author = db.relationship('User', back_populates='replies')
    op = db.relationship('Post', back_populates='replies')
    likes = db.relationship(
        'ReplyLike', back_populates='reply', lazy='dynamic', cascade='all, delete'
    )

    def __repr__(self):
        return f"Reply('{self.content}', '{self.timestamp}')"


class ReplyLike(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    reply_id = db.Column(db.Integer, db.ForeignKey('reply.reply_id'), primary_key=True)
    liked = db.Column(db.Boolean, nullable=False, default=True)

    user = db.relationship('User', back_populates='likes')
    reply = db.relationship('Reply', back_populates='likes')


class Pet(db.Model):
    pet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(18), nullable=False)
    species = db.Column(db.String(45), nullable=False)
    subspecies = db.Column(db.String(45))
    color = db.Column(db.String(45))
    tagline = db.Column(db.String(150))
    _image_file = db.Column('image_file', db.String(45))
    biography = db.Column(db.Text)
    img1_path = db.Column(db.String(45))
    img2_path = db.Column(db.String(45))
    img3_path = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True
    )

    owner = db.relationship('User', back_populates='pets')

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
        return f'/static/images/pet/profile/{self.image_file}'

    @property
    def recent_photo_paths(self):
        photos = (self.img1_path, self.img2_path, self.img3_path)
        return tuple(
            f'/static/images/pet/recent/{photo}'
            for photo in photos
            if photo is not None
        )

    def __repr__(self):
        return f"Profile('{self.name}', '{self.species}', '{self.subspecies}', '{self.color}', '{self.tagline}', '{self.biography}')"
