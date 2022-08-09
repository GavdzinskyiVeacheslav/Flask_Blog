from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Главная')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Блог')


@app.route('/html_page')
def html_page():
    return render_template('html_page.html')


@app.route('/css_page')
def css_page():
    return render_template('css_page.html')


@app.route('/js_page')
def js_page():
    return render_template('js_page.html')


@app.route('/python_page')
def python_page():
    return render_template('python_page.html')


@app.route('/flask_page')
def flask_page():
    return render_template('flask_page.html')


@app.route('/django_page')
def django_page():
    return render_template('django_page.html')


if __name__ == '__main__':
    app.run(debug=True, port=5656)
