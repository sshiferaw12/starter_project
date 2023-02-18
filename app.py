from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

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

    if ((username == "abd") and (password == "pass") ): 
        return redirect(url_for('profile'))
    else: 
        message = 'Invalid login credentials. Please try again.'
        return render_template('login.html', message=message)


@app.route('/profile')
def profile():
        return render_template('profile.html')
 

@app.route('/logout')
def logout():
    return redirect(url_for('loginPage'))


if __name__ == "__main__":
    app.run(debug=True)
