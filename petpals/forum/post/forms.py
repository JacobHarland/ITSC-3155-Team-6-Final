from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewPostForm(FlaskForm):
    #ToDo: Add Attachment functionality?
	title = StringField("Post Title", validators=[DataRequired()])
	content = TextAreaField('Post Content', validators=[DataRequired()])
	submit = SubmitField("Publish Post")
