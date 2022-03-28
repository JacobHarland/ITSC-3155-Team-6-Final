from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=8, max=32)])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
    
