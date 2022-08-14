from flask import Blueprint, render_template, url_for, request
from flask_login import login_required, current_user

from blog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', title='Главная')


@main.route('/blog', methods=['POST', 'GET'])
@login_required
def blog():
    post = Post.query.get(current_user.id)
    if post:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
        image_file = url_for(
            'static',
            filename=f'profile_pics/{current_user.username}/{post.image_post}',
        )

        return render_template(
            'blog.html',
            title='Блог',
            posts=posts,
            image_file=image_file,
        )

    else:

        return render_template(
            'blog.html',
            title='Блог',
            nothing='Постов пока нет',
        )


@main.route('/html_page')
def html_page():
    return render_template('html_page.html')


@main.route('/css_page')
def css_page():
    return render_template('css_page.html')


@main.route('/js_page')
def js_page():
    return render_template('js_page.html')


@main.route('/python_page')
def python_page():
    return render_template('python_page.html')


@main.route('/flask_page')
def flask_page():
    return render_template('flask_page.html')


@main.route('/django_page')
def django_page():
    return render_template('django_page.html')
