from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class NewReplyForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired(), Length(max=10000)])
    submit = SubmitField("Reply")
