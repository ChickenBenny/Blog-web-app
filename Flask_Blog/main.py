from flask import Flask, render_template
from forms import ResgistrationForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path

DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bennys Project'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

def create_database(app):
    if not path.exists(f'Flask_Blog/{DB_NAME}'):
        db.create_all(app = app)
        print('Created Database!')

db = SQLAlchemy(app)
db.init_app(app)
create_database(app)


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

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


@app.route("/")
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")
def aoubt():
    return render_template('about.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = ResgistrationForm()
    return render_template('register.html', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = ResgistrationForm()
    return render_template('login.html', form = form)



if __name__ == '__main__':
    app.run(debug = True)