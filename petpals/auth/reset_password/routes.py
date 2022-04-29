from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user
from flask_mail import Message
from petpals import bcrypt, db, mail
from .forms import RequestResetForm, ResetPasswordForm
from petpals.models import User

router = Blueprint('reset_password_router', __name__, template_folder='templates', url_prefix='/reset_password')

def send_reset_email(user):
    "Sends the email using Flask-Mail"
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('auth_router.reset_password_router.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@router.route('', methods=['GET', 'POST'])
def reset_request():
    # if user is logged in, clicking reset password redirects to home
    if current_user.is_authenticated:
        return redirect(url_for('home_router.index'))
    form = RequestResetForm()
    # gets the email of the user who submitted the password request
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent to reset your password.', 'info')
        return redirect(url_for('auth_router.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


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
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # bcrypt, hashes a password from form and decodes it as a string instead of bytes with utf-8
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been reset. You are now able to login. Welcome to PetPals!', 'success')
        return redirect(url_for('auth_router.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
