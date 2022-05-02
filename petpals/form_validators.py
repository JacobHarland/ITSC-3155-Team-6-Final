from flask_login import current_user
from flask_wtf.file import FileAllowed
from petpals.models import User
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError


def unique_email_validator(_, email):
    'Validation to make sure users cannot have same email'

    if current_user.is_authenticated and current_user.email == email.data:
        return
    if User.query.filter_by(email=email.data).first():
        raise ValidationError('Email already in use. Please enter a different email.')


def unique_username_validator(_, username):
    'Validation to make sure users cannot have same username'

    if current_user.is_authenticated and current_user.username == username.data:
        return
    if User.query.filter_by(username=username.data).first():
        raise ValidationError(
            'Username already in use. Please enter a different username.'
        )


fullname_validators = [DataRequired(), Length(max=50)]
username_validators = [
    DataRequired(),
    Length(min=2, max=18),
    Regexp(
        r'^[\w-]*$',
        message="Username invalid, can only contain letters, numbers, dashes, or underscores",
    ),
]
new_username_validators = username_validators + [unique_username_validator]
email_validators = [DataRequired(), Email()]
new_email_validators = email_validators + [unique_email_validator]
password_validators = [DataRequired(), Length(min=8, max=32)]
image_validators = [FileAllowed(['jpeg', 'jpg', 'png', 'gif'])]
