from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import ResgistrationForm, LoginForm
from .views import home

auth = Blueprint('auth', __name__)

@auth.route("/register", methods = ['GET', 'POST'])
def register():
    form = ResgistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    return render_template('login.html', form = form)
