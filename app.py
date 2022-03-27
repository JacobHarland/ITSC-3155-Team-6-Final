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
    profile = Profile.query.get_or_404(profile_id)
    return render_template("profile.html", profile=profile)


@app.post("/profiles")
def add_profile():
    name = request.form.get("name", "")
    owner_name = request.form.get("owner_name", "")
    species = request.form.get("species", "")
    subspecies = request.form.get("subspecies", "")
    owner_phone = request.form.get("owner_phone", "")
    color = request.form.get("color", "")

    new_profile = Profile(
        name=name,
        owner_name=owner_name,
        owner_phone=owner_phone,
        species=species,
        subspecies=subspecies,
        color=color,
    )
    db.session.add(new_profile)
    db.session.commit()

    return redirect(f"/profiles/{new_profile.profile_id}")
