from flask import Flask, abort, redirect, render_template, request

from models import Profile, db

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://root:abc123@localhost:3306/3155final_dev"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/profiles")
def get_profiles():
    all_profiles = Profile.query.all()
    return render_template("all_profiles.html", profiles=all_profiles)


@app.get("/profiles/<profile_id>")
def get_profile_by_id(profile_id):
    return render_template("profile.html")


@app.post("/profiles")
def add_profile():
    name = request.form.get("name", "")
