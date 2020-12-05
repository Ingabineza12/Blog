from flask_wtf import  FlaskForm
from wtforms import ValidationError,StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[Required()])
    password=PasswordField('Password',validators=[Required()])
    remember=BooleanField('Remember Me')
    submi=SubmitField('Login')

class RegistrationForm(FlaskForm):
    email=StringField('Your Email Address', validators=[Required(),Email()])
    username=StringField('Enter Your username', validators=[Required()])
    password=PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message='Passwords must match')])
    password_confirm=PasswordField('Confirm Passwords',validators=[Required()])
    submit=SubmitField('signup')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("The Email has already been taken!!!")

    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("The username has already taken!!")
