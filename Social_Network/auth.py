import os
import secrets
from PIL import Image
from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from . import app, db, bcrypt
from .forms import ResgistrationForm, LoginForm, UpdateAccount
from .models import User
from .views import home

auth = Blueprint('auth', __name__)

@auth.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = ResgistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data} created success!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form = form)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('views.home'))
        else:
            flash('Login unsuccessful. Please try again.')
    return render_template('login.html', form = form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, image_type = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + image_type #把圖片用亂碼代表
    picture_path = os.path.join(f'{app.root_path}static/profile_pics{picture_fn}')
    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_fn


@login_required
@auth.route("/account", methods = ['GET', 'POST'])
def account():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    return render_template('account.html', image_file = image_file, form = form)