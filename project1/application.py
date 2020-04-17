import os

from flask import Flask, session,redirect,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return redirect("/register")

@app.route("/register")
def toregister():
    return render_template("register.html")

@app.route("/user_ack", methods=["POST"] )
def user_ack():
    Username = request.form.get("name")
    Email = request.form.get("email")

    return render_template("user_ack.html", name=Username , email = Email )
