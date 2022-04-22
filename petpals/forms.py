from wsgiref.validate import validator
from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from petpals.models import User
from flask_login import current_user

class SignupForm(FlaskForm):
    fullname = StringField('Full Name',
                            validators=[DataRequired(),Length(min=1, max=50)])
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=18)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=8, max=32)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Validation to make sure users cannot have same username
    def validate_username(self, username):
        # user = database query for username input to check if exists already. Is none if nothing found
        user = User.query.filter_by(username=username.data).first()
        # if user = none, this if statement is not reached
        if user:
            raise ValidationError('Username already in use. Please enter a different username.')

    # Validation to make sure users cannot have same email
    def validate_email(self, email):
        # user = database query for email input to check if exists already. Is none if nothing found
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use. Please enter a different email.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=8, max=32)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    fullname = StringField('Full Name',
                            validators=[DataRequired(),Length(min=1, max=50)])
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=18)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                            validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    biography = TextAreaField('Bio')
    submit = SubmitField('Update')

    # Validation to make sure users cannot have same username
    def validate_username(self, username):
        # for update form, so only want to validate if user changes their information
        if username.data != current_user.username:
            # user = database query for username input to check if exists already. Is none if nothing found
            user = User.query.filter_by(username=username.data).first()
            # if user = none, this if statement is not reached
            if user:
                raise ValidationError('Username already in use. Please enter a different username.')

    # Validation to make sure users cannot have same username
    def validate_email(self, email):
        # for update form, so only want to validate if user changes their information
        if email.data != current_user.email:
            # user = database query for email input to check if exists already. Is none if nothing found
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use. Please enter a different email.')

class UpdatePetForm(FlaskForm):
    name = StringField('Pet Name',
                            validators=[DataRequired(),Length(min=1, max=50)])
    species = StringField('Pet Species', validators=[DataRequired(), Length(min=1, max=45)])
    subspecies = StringField('Pet Subspecies', validators=[Length(max=45)])
    color = StringField('Pet Color', validators=[Length(max=45)])
    tagline = StringField('Tagline', validators=[Length(max=150)])
    biography = TextAreaField('Bio', validators=[DataRequired(), Length(max=2000)])
    profile_picture = FileField('Update Profile Picture',
                            validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    picture_one = FileField('Update Picture 1',
                            validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    picture_two = FileField('Update Picture 2',
                            validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    picture_three = FileField('Update Picture 3',
                            validators=[FileAllowed(['jpeg', 'jpg', 'png', 'gif'])])
    submit = SubmitField('Update')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    # Validation to make sure email exists within database for password reset to occur
    def validate_email(self, email):
        # user = database query for email input to check if exists already. Is none if nothing found
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with the associated email.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=8, max=32)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class ChangePassword(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Current Password',
                            validators=[DataRequired(), Length(min=8, max=32)])
    new_password = PasswordField('New Password',
                            validators=[DataRequired(), Length(min=8, max=32)])
    confirm_password = PasswordField('Confirm New Password',
                            validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')
