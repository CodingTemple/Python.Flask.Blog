from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from app.models import Comment

class CommentForm(FlaskForm):
  name = StringField(validators=[DataRequired()])
  email = StringField(validators=[DataRequired(), Email()])
  body = TextAreaField(validators=[DataRequired()])
  submit = SubmitField('Post Comment')