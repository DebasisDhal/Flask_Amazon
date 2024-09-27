from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.fields.numeric import FloatField, IntegerField
from wtforms.fields.simple import EmailField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, NumberRange


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

class ShopItemsForm(FlaskForm):
    product_name = StringField('Name of Product', validators=[DataRequired()])
    current_price = FloatField('Current Price', validators=[DataRequired()])
    previous_price = FloatField('Previous Price', validators=[DataRequired()])
    in_stock = IntegerField('In Stock', validators=[DataRequired(), NumberRange(min=0)])
    product_picture = FileField('Product Picture', validators=[DataRequired()])
    flash_sale = BooleanField('Flash Sale')

    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update')