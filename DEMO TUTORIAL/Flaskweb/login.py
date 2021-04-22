from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.secret_key="myname"
app.permanent_session_lifetime=timedelta(minutes=1)


app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class users(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

    def __init__(self,name,email):
        self.name=name
        self.email=email


@app.route("/")
def home():
    # return render_template("index.html",content=name)
    return render_template("index.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        user=request.form["nam"]
        session["user"]=user
        
        found_user=users.query.filter_by(name=user).first()
        if found_user:
            session["email"]=found_user.email

        else:
                usr=users(user,"")
                db.session.add(usr)
                db.session.commit()
        flash("Successfully logged in!")
        return redirect(url_for("user")) 
    else: 
        return render_template("login.html")



@app.route("/view")
def view():
    return render_template("view.html",values=users.query.all())

@app.route("/user",methods=["POST","GET"])
def user():
    email=None
    if "user" in session:
        user=session["user"]
       
        if request.method=="POST":
            email=request.form["email"]
            found_user=users.query.filter_by(name=user).first()
            found_user.email=email
            db.session.commit()
            session["email"]=email
        else:
            if "email" in session:
                email=session["email"]
        return render_template("user.html",email=email)
    else:
        if "user" in session:
            flash("You have been logged out! ")
            # return redirect(url_for("user"))
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user=session["user"]
        flash("You have been logged out!")

    session.pop("user",None)
    session.pop("email",None)

    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)