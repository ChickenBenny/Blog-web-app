from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import path

DB_NAME = "database.db"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bennys Project'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'




from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix = '/')
app.register_blueprint(auth, url_prefix = '/')

from .models import User, Post
    
