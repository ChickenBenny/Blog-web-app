from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from . import db, bcrypt
from .forms import ResgistrationForm, LoginForm
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
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remeber.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please try again.')
    return render_template('login.html', form = form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
@auth.route("/account")
def account():
    return render_template('account.html')