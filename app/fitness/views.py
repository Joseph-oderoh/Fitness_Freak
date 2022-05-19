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
        new_post_object.save_post()
        return redirect(url_for('fitness.index'))
    return render_template('add_post.html', form = form)


@fitness.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    post=Post.query.filter_by(id=post_id).first()
    print(post)
    return render_template('showpost.html',post=post)

@fitness.route('/post/<post_id>/update',methods=['GET', 'POST'])
#@login_required
def update_post(post_id):
    post=Post.query.filter_by(id=post_id).first()
    # if post.user != current_user:
    #     abort(403)

    form=PostForm()
    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash('You have updated your post.')
        return redirect(url_for('.post',post_id=post.id) )
    elif request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content

    return render_template('add_post.html', form = form,title='Update Post')

@fitness.route('/post/<post_id>/delete',methods=['GET', 'POST'])
#@login_required
def delete_post(post_id):
    post=Post.query.filter_by(id=post_id).first()
    # if post.user != current_user:
        # abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted successfully.')
    return redirect(url_for('fitness.index'))

@fitness.route('/comments/<post_id>', methods=['GET', 'POST'])
##@login_required
def comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    post = Post.query.get(post_id)
    form = CommentForm()
    if post is None:
        abort(404)
    if form.validate_on_submit():
            comment = Comment(
            content=form.content.data,
            post_id=post_id,
            user_id=current_user.id
        )
            db.session.add(comment)
            db.session.commit()
            form.content.data = ''
            flash('Your comment has been posted successfully.')
    return render_template('comments.html',posts= post, comment=comments, form = form)

@fitness.route('/comment/<comment_id>', methods=['POST','GET'])
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id = comment_id).first()
    post_id = comment.post_id
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted successfully.')
    return redirect(url_for('.post',post_id = post_id))


