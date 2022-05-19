from . import fitness
from .. import db
from .. models import User, Comment, Post
from .forms import PostForm, CommentForm
from flask_login import login_required, current_user
from flask import  render_template,redirect, request,url_for,abort,flash