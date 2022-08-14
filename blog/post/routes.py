from flask import Blueprint, flash, url_for, render_template
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from blog import db
from blog.models import Post
from blog.post.forms import PostForm
from blog.post.utils import save_picture_post

posts = Blueprint('post', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            context=form.context.data,
            image_post=form.picture.data,
            author=current_user,
        )
        picture_file = save_picture_post(form.picture.data)
        post.image_post = picture_file
        db.session.add(post)
        db.session.commit()
        flash('Пост был опубликован!', 'success')
        return redirect(url_for('main.blog'))
    image_file = url_for(
        'static',
        filename=f'profile_pics/' + current_user.username + '/post_image/' + current_user.image_file,
    )
    return render_template(
        'create_post.html',
        title='Новая статья',
        form=form,
        legend='Новая статья',
        image_file=image_file,
    )


@posts.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    image_file = url_for(
        'static',
        filename=f'profile_pics/' + post.author.username + '/post_image/' + post.image_post
    )
    return render_template(
        'post.html',
        title=post.title,
        post=post,
        image_file=image_file
    )

