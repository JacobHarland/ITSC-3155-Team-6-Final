from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from petpals.models import User


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