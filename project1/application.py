import os,sys,time

from flask import Flask, session,redirect,render_template,request,url_for
from userinfo import *
from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__,static_url_path='/static')
app.secret_key='reddy100'
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Session(app)
db.init_app(app)
Session(app)
with app.app_context():
    db.create_all()
    

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    if session.get("user") is None:
        return redirect("/register")
    else:
        return render_template("login.html", message = "done")  

@app.route("/register")
def toregister():
    return render_template("register.html")

@app.route("/user_ack", methods=["POST","GET"] )
def user_ack():
    Username = request.form.get("name")
    Password = request.form.get("password")
    Email = request.form.get("email")
    # print("--------",Username,Password,Email)
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

@app.route("/authentication",methods = ["POST","GET"])
def authentication():
    if request.method=="POST":
        username = request.form.get("name")
        password = request.form.get("password")
        userData = user.query.filter_by(username=username).first()

        if userData is not None:
            # print(username,password)
            # print(userData.username,userData.password)
            if userData.username == username and userData.password == password:
                # return redirect(url_for('userhome',user=username))
                session['user'] = username 
                return render_template("login.html", username= userData.username)
            else:    
                return render_template("register.html", message = "entered Username/password is incorrect")
        else:
            return redirect("/register")
    else:
        return "<h1> please login/ register</h1>"

# @app.route("/home/<user>")
# def userhome(user):
#     if user in session:
#         return render_template("login.html",username=user,message = "Succesfully loggeg in: WELCOME!!!")

#     return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/register")