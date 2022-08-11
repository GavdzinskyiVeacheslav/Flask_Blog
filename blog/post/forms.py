from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Статья', validators=[DataRequired()])
    picture = FileField('Изображение (png, jpg)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Опубликовать')


class PostUpdateForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Статья', validators=[DataRequired()])
    picture = FileField('Изображение (png, jpg)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Опубликовать')
