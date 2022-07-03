from flask import Blueprint, render_template, flash, redirect, url_for

views = Blueprint('views', __name__)

posts = [
    {
        'author': 'Benny',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 1, 2022'
    },
    {
        'author': 'ChickenBenny',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 1, 2022'
    }
]

@views.route("/")
def home():
    return render_template('home.html', posts = posts)

@views.route("/about")
def aoubt():
    return render_template('about.html')

