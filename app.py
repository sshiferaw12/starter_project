from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "session_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'my_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


# with app.app_context():
#       db.create_all()
#       usr = User("sola","pp")
#       usr1 = User("bab","ppdf")
#       usr2 = User("df","fd")
#       db.session.add(usr1)
#       db.session.add(usr2)
#       db.session.commit()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/career')
def career():
      return render_template("career.html")


@app.route('/contact')
def contact():
    return 'Hello, World'

@app.route('/thankyou',methods = ["POST"])
def contactFormFilled():
    name = request.form["name"]
    return render_template("thankyou.html",name=name)

@app.route('/login')
def loginPage():
    return render_template("login.html")


@app.route("/handle-login", methods=["POST"])
def handleLogin():

    username = request.form["username"]
    password = request.form["password"]

    userFound = User.query.filter_by(username=username,password=password).first()   
    
    if (userFound): 
        session['username'] = username
        return redirect(url_for('profile'))
    else: 
        message = 'Invalid login credentials. Please try again.'
        return render_template('login.html', message=message)

@app.route('/profile')
def profile():
    if ('username' in session):
        return render_template('profile.html')
    else:
        return render_template('login.html',message="Hey you are not allowed here, you need to login!")

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('loginPage'))


if __name__ == "__main__":
    app.run(debug=True,)
