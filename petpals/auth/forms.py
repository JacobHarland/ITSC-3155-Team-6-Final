from flask_wtf import FlaskForm
from petpals.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Regexp,
    ValidationError,
)


class SignupForm(FlaskForm):
    fullname = StringField(
        'Full Name', validators=[DataRequired(), Length(min=1, max=50)]
    )
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, max=18),
            Regexp(
                '^[\w-]*$',
                message="Username not valid, can only contain letters, numbers, dashes, or underscores",
            ),
        ],
    )
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=8, max=32)]
    )
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    # Validation to make sure users cannot have same username
    def validate_username(self, username):
        # user = database query for username input to check if exists already. Is none if nothing found
        user = User.query.filter_by(username=username.data).first()
        # if user = none, this if statement is not reached
        if user:
            raise ValidationError(
                'Username already in use. Please enter a different username.'
            )

    # Validation to make sure users cannot have same email
    def validate_email(self, email):
        # user = database query for email input to check if exists already. Is none if nothing found
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'Email already in use. Please enter a different email.'
            )


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=8, max=32)]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
