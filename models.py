from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    subspecies = db.Column(db.String, nullable=True)
    owner_name = db.Column(db.String, nullable=True)
    owner_phone = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"Profile({self.profile_id}, {self.name}, {self.species}, {self.subspecies}, {self.color}, {self.owner_name}, {self.owner_phone})"


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    fullname = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User({self.user_id}, {self.username}, {self.fullname}, {self.email})"


class Forum_post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    file = db.Column(db.BLOB, nullable=True)

    def __repr__(self):
        return f"Forum_post({self.post_id}, {self.title}, {self.content})"
