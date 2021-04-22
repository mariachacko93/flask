
from flask import url_for,redirect,render_template,flash,session
from forms import RegistrationForm,LoginForm
from flaskreg import db,app
from models import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# from reg import app,db

app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password123@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"]="REG"









@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register",methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Account created successfully ..Please Login!!")
        return redirect(url_for("login"))
    return render_template("reg.html",form=form)

@app.route("/login",methods=["POST","GET"])
def login():
    form=LoginForm()
    if form.validate_on_submit():    
        if form.username.data=="maria" and form.password.data=="maria":
            # flash("LoggedIn successfully")

            # return redirect(url_for("homepage"))
            return render_template("homepage.html")

        else:
            flash("Login Unsuccessfully")

            return redirect(url_for("home"))
        
    return render_template("login.html",form=form)

if __name__=="__main__":
    app.run(debug=True)