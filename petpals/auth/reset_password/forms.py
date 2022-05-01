from flask_wtf import FlaskForm
from petpals.form_validators import email_validators, password_validators
from petpals.models import User
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class RequestResetForm(FlaskForm):
    email = StringField('Email', email_validators)
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        'Validation to make sure email exists within database for password reset to occur'

        if not User.query.filter_by(email=email.data).first():
            raise ValidationError('There is no account with the associated email.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', password_validators)
    confirm_password = PasswordField(
        'Confirm New Password',
        validators=[
            DataRequired(),
            EqualTo('password', 'Field must be equal to New Password.'),
        ],
    )
    submit = SubmitField('Reset Password')
