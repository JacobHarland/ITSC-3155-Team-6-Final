from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from petpals.form_validators import (
    confirm_password_validators,
    email_validators,
    fullname_validators,
    image_validators,
    new_email_validators,
    new_username_validators,
    password_validators,
)
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length


class UpdateAccountForm(FlaskForm):
    fullname = StringField('Full Name', fullname_validators)
    username = StringField('Username', new_username_validators)
    email = StringField('Email', new_email_validators)
    picture = FileField('Profile Picture', image_validators)
    biography = TextAreaField('Bio')
    submit = SubmitField('Update')


class UpdatePetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired(), Length(min=1, max=50)])
    species = StringField(
        'Pet Species', validators=[DataRequired(), Length(min=1, max=45)]
    )
    subspecies = StringField('Pet Subspecies', validators=[Length(max=45)])
    color = StringField('Pet Color', validators=[Length(max=45)])
    tagline = StringField('Tagline', validators=[Length(max=150)])
    biography = TextAreaField('Bio', validators=[Length(max=2000)])
    profile_picture = FileField('Profile Picture', image_validators)
    picture_one = FileField('Picture 1', image_validators)
    picture_two = FileField('Picture 2', image_validators)
    picture_three = FileField('Picture 3', image_validators)
    submit = SubmitField('Update')


class ChangePassword(FlaskForm):
    email = StringField('Email', email_validators)
    password = PasswordField('Current Password', password_validators)
    new_password = PasswordField('New Password', password_validators)
    confirm_password = PasswordField(
        'Confirm New Password',
        validators=[
            DataRequired(),
            EqualTo('new_password', 'Field must be equal to %(other_label)s.'),
        ],
    )
    submit = SubmitField('Change Password')
