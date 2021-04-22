from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,DataRequired,Email

class RegistrationForm(FlaskForm):
    username=StringField(validators=[DataRequired(),Length(min=3,max=20)])
    email=StringField(validators=[DataRequired(),Email()])
    password=PasswordField(validators=[DataRequired(),Length(min=4,max=6)])
    submit=SubmitField(label='SignIn')

class LoginForm(FlaskForm):
    username=StringField(validators=[DataRequired(),Length(min=3,max=20)])
    password=PasswordField(validators=[DataRequired(),Length(min=4,max=6)])
    submit=SubmitField(label='SignIn')
