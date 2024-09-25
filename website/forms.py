from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length


class SignUpForm(FlaskForm):
    email = EmailField('Email', validators= [DataRequired()])
    username = StringField('Username', validators= [DataRequired(), length(min=2)])
    password1 = PasswordField('Enter your Password', validators= [DataRequired(), length(min=6)])
    password2 = PasswordField('Conform your Password', validators= [DataRequired(), length(min=6)])
    submit =  SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField('Log in')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), length(min=6)])
    change_password = SubmitField('Change Password')