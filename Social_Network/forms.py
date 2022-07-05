from tokenize import String
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

class ResgistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def valdate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("Username is taken. Please take another one.")
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("Email is taken. Please take another one.")


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember  = BooleanField('Remeber Me')
    submit = SubmitField('Login')


class UpdateAccount(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed('jpg', 'png')])
    submit = SubmitField('Update')

    def valdate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError("Username is taken. Please take another one.")
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError("Email is taken. Please take another one.")
