from flask_wtf import FlaskForm
from petpals.form_validators import (
    email_validators,
    fullname_validators,
    new_email_validators,
    new_username_validators,
    password_validators,
)
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class SignupForm(FlaskForm):
    fullname = StringField('Full Name', fullname_validators)
    username = StringField('Username', new_username_validators)
    email = StringField('Email', new_email_validators)
    password = PasswordField('Password', password_validators)
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', 'Field must be equal to Password.'),
        ],
    )
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', email_validators)
    password = PasswordField('Current Password', password_validators)
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
