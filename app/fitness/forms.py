
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Length,EqualTo
from wtforms import StringField,TextAreaField,SubmitField

class CommentForm(FlaskForm):
  content = TextAreaField('Leave a Comment.',validators=[InputRequired()])
  submit = SubmitField ('Submit')

  