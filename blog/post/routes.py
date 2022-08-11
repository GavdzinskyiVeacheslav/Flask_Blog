from flask import Blueprint
from flask_login import current_user

from blog.models import Post
from blog.post.forms import PostForm

post = Blueprint('post', __name__)


@post.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            image_post=form.picture.data,
            author=current_user,
        )
        picture_file = save_picture_post(form.picture.data)