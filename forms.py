
from flask_wtf import FlaskFOrm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email= StringField('Email', validatosr=[DataRequires(), Email()])
    password =StringFeild('Password', validatosr=[DataRequires()])
    confirm_password = StringFeild('Confirm Password', validatosr=[DataRequires(), EqualTo('password')])
    submit = StringFeild('sign up')
class RegistrationForm(FlaskForm):
    email
    remeber
    submit
    
