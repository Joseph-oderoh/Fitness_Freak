from flask import render_template, request, redirect, url_for, flash, abort
from . import home
from .forms import PostForm,CommentForm
from ..models import Post, User, Comment
from sqlalchemy import desc
from flask_login import current_user, login_required


@home.route('/home')
def homepage():
    title= "Fitness_Freak --Homepage"
    postform = PostForm()
    commentform = CommentForm()
    posts = all_posts(Post.query.order_by(desc('post_created')))
    recent_posts = all_posts(Post.query.order_by(desc('post_created')).limit(5))
    return render_template('home.html', title=title, postform=postform, commentform=commentform, recent_posts=recent_posts, posts=posts)

def all_posts(posts):
    for post in posts:
        post.user = User.query.filter_by(id=post.post_by).first()
        for comment in post.post_comments:
            comment.user = User.query.filter_by(id=comment.user.id).first()
    return posts

# about
def about():
    return render_template('about.html')
