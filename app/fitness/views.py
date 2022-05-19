from . import fitness
from .. import db
from .. models import User, Comment, Post
from .forms import PostForm, CommentForm
from flask_login import login_required, current_user
from flask import  render_template,redirect, request,url_for,abort,flash
@fitness.route('/')
def index():
    title = 'Fitness'
    post = Post.query.order_by(Post.date_created).all()
    return render_template('index.html', post = post, title=title)
@fitness.route('/create_new', methods = ['POST','GET'])
# @login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        # user_id = current_user
        new_post_object = Post(title = title,content = content)
        # user_id=current_user._get_current_object().id
        new_post_object.save_pitch()
        return redirect(url_for('fitness.index'))
    return render_template('add_post.html', form = form)


@fitness.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    post=Post.query.filter_by(id=post_id).first()
    print(post)
    return render_template('showpost.html',post=post)