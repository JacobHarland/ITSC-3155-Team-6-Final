from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    subspecies = db.Column(db.String, nullable=True)
    owner_name = db.Column(db.String, nullable=True)
    owner_phone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Profile({self.profile_id}, {self.name}, {self.species}, {self.subspecies}, {self.owner_name}, {self.owner_phone})"
