from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import InputRequired,Length,EqualTo

class FormPost(FlaskForm):
  title = StringField('Blog Title', validators=[InputRequired(), Length(1, 64)])
  author = StringField('Author : ',)
  category = RadioField('Blog Category :', choices = [('Health', 'Health')], validators = [InputRequired()])
  content = TextAreaField('Your Post', validators=[InputRequired()])
  submit = SubmitField('Post')
  
  
class CommentForm(FlaskForm):
  content = TextAreaField('Leave a comment ...', validators=[InputRequired()])