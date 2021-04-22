from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField,SubmitField
import psycopg2
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class LoginForm(Form):

    email = StringField("Email", validators=[validators.Length(min=7, max=50), validators.DataRequired(message="Please Fill This Field")])

    password = PasswordField("Password", validators=[validators.DataRequired(message="Please Fill This Field")])


class RegisterForm(Form):

    name = StringField("Name", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])

    username = StringField("Username", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])

    email = StringField("Email", validators=[validators.Email(message="Please enter a valid email address")])

    password = PasswordField("Password", validators=[

        validators.DataRequired(message="Please Fill This Field"),

        validators.EqualTo(fieldname="confirm", message="Your Passwords Do Not Match")
    ])

    confirm = PasswordField("Confirm Password", validators=[validators.DataRequired(message="Please Fill This Field")])



class PostForm(FlaskForm):
    title=StringField("title",validators=[DataRequired(),validators.Length(min=3,max=10)])
    content=TextAreaField("content",validators=[DataRequired()])
    submit=SubmitField("Submit")