
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Length,EqualTo
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField

class CommentForm(FlaskForm):
  content = TextAreaField('Leave a Comment.',validators=[InputRequired()])
  submit = SubmitField ('Submit')

class FormPost(FlaskForm):
  title = StringField('Title', validators=[InputRequired()])
  content = TextAreaField('Post', validators=[InputRequired()])
  category = RadioField('Category :', choices = [('Fitness', 'Fitness')], validators = [InputRequired()])
  # category = SelectField('Category',choices=[('Health','Health'),('Fitness','Fitness'),('Nutrition','Nutrition')])
  author = StringField('Author')
  
  submit = SubmitField('Add Post')

