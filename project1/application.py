import os,sys,time

from flask import Flask, session,redirect,render_template,request
from userinfo import *
# from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__,static_url_path='/static')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Session(app)
db.init_app(app)
with app.app_context():
    db.create_all()

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return redirect("/register")

@app.route("/register")
def toregister():
    return render_template("register.html")

@app.route("/user_ack", methods=["POST","GET"] )
def user_ack():
    Username = request.form.get("name")
    Password = request.form.get("password")
    Email = request.form.get("email")
    try:
        var = user(username = Username, email = Email, password = Password , time = time.ctime(time.time()))
        db.session.add(var)
        db.session.commit()

    except ValueError:
        return render_template("error.html")
            
    return render_template("user_ack.html", name=Username , email = Email )

@app.route("/admin")
def admin():
    Admin = user.query.all()

    return render_template("admin.html", Admin =Admin)

