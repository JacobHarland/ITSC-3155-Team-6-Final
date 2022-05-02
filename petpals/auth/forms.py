from flask_wtf import FlaskForm
from petpals.form_validators import (
    confirm_password_validators,
    email_validators,
    fullname_validators,
    new_email_validators,
    new_username_validators,
    password_validators,
)
from wtforms import BooleanField, PasswordField, StringField, SubmitField


class SignupForm(FlaskForm):
    fullname = StringField('Full Name', fullname_validators)
    username = StringField('Username', new_username_validators)
    email = StringField('Email', new_email_validators)
    password = PasswordField('Password', password_validators)
    confirm_password = PasswordField('Confirm Password', confirm_password_validators)
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', email_validators)
    password = PasswordField('Current Password', password_validators)
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
