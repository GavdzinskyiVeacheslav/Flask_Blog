from datetime import datetime

from blog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    last_seen = db.Column(db.DateTime)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.email}, {self.password}, {self.image_file})'


class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    context = db.Column(db.Text(60), nullable=False)
    image_post = db.Column(db.String(30), nullable=True, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'Post({self.title}, {self.date_posted}, {self.image_post})'

