<<<<<<< HEAD:petpals/routes.py
from flask import flash, redirect, render_template, url_for, request
=======
from flask import Blueprint, flash, redirect, render_template, url_for
>>>>>>> main:petpals/auth/reset_password/routes.py
from flask_login import current_user
from flask_mail import Message
from petpals import bcrypt, db, mail
from .forms import RequestResetForm, ResetPasswordForm
from petpals.models import User

router = Blueprint('reset_password_router', __name__, template_folder='templates', url_prefix='/reset_password')

<<<<<<< HEAD:petpals/routes.py

@app.get("/")
def index():
    return render_template("index.html")


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/faq")
def faq():
    return render_template("faq.html")


@app.get("/forum")
def forum():
    all_posts = Post.query.all()
    user = User.query.first()
    return render_template("forum.html", posts=all_posts, db=db, user=user, User=User)


@app.route("/search", methods=["GET", "POST"])
def search():
    search_param = request.form["search_param"]
    filtered_posts = (
        db.session.query(Post).filter(Post.content.contains(search_param)).all()
    )
    user = User.query.first()
    return render_template(
        "forum.html", posts=filtered_posts, db=db, user=user, User=User
    )


# sends the email using Flask-Mail
=======
>>>>>>> main:petpals/auth/reset_password/routes.py
def send_reset_email(user):
    "Sends the email using Flask-Mail"
    token = user.get_reset_token()
<<<<<<< HEAD:petpals/routes.py
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[user.email]
    )
    msg.body = f"""To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
=======
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('auth_router.reset_password_router.reset_token', token=token, _external=True)}
>>>>>>> main:petpals/auth/reset_password/routes.py
If you did not make this request then simply ignore this email and no changes will be made.
"""
    mail.send(msg)


<<<<<<< HEAD:petpals/routes.py
@app.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    # if user is logged in, clicking reset password redirects to home
    if current_user.is_authenticated:
        return redirect(url_for("index"))
=======
@router.route('', methods=['GET', 'POST'])
def reset_request():
    # if user is logged in, clicking reset password redirects to home
    if current_user.is_authenticated:
        return redirect(url_for('home_router.index'))
>>>>>>> main:petpals/auth/reset_password/routes.py
    form = RequestResetForm()
    # gets the email of the user who submitted the password request
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent to reset your password.", "info")
        return redirect(url_for("auth_router.login"))
    return render_template("reset_request.html", title="Reset Password", form=form)


<<<<<<< HEAD:petpals/routes.py
@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    # if user is logged in, redirects to home
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    user = User.verify_reset_token(token)
    # if verify_reset_token returns none, then the token is invalid or expired
    if user is None:
        flash("Invalid or expired token", "warning")
        return redirect(url_for("reset_request"))
=======
@router.route("/<token>", methods=['GET', 'POST'])
def reset_token(token):
    # if user is logged in, redirects to home
    if current_user.is_authenticated:
        return redirect(url_for('home_router.index'))
    user = User.verify_reset_token(token)
    # if verify_reset_token returns none, then the token is invalid or expired
    if user is None:
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('auth_router.reset_password_router.reset_request'))
>>>>>>> main:petpals/auth/reset_password/routes.py
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # bcrypt, hashes a password from form and decodes it as a string instead of bytes with utf-8
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user.password = hashed_password
        db.session.commit()
<<<<<<< HEAD:petpals/routes.py
        flash(
            "Your password has been reset. You are now able to login. Welcome to PetPals!",
            "success",
        )
        return redirect(url_for("auth_router.login"))
    return render_template("reset_token.html", title="Reset Password", form=form)


app.register_blueprint(profile_router)
app.register_blueprint(post_router)
app.register_blueprint(auth_router)
=======
        flash('Your password has been reset. You are now able to login. Welcome to PetPals!', 'success')
        return redirect(url_for('auth_router.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
>>>>>>> main:petpals/auth/reset_password/routes.py
