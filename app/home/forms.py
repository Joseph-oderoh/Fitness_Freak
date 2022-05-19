from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=200)])
    submit =SubmitField('Submit')
    
class CommentForm(FlaskForm):
    commentbody = TextAreaField("Comment", validators=[DataRequired()])
    postbtn = SubmitField("Post")