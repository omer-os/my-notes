from datetime import timedelta
from flask import Flask
from flask.globals import request, session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key="nbrounpiqnouegbnpf"
# the session will stay for 10 days
app.permanent_session_lifetime = timedelta(days=10)


@app.route('/')
def home():
    return redirect(url_for('articles'))

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method=="POST":
        name = request.form["name"]
        password = request.form["password"]

        session['name'] = name
        session['password'] = password
        session.permanent = True
        return redirect(url_for('articles'))
    
    if "name" and "password" in session:
        return render_template('articles.html')
    return render_template('sginin.html')
    
        

@app.route('/articles')
def articles():
    if "name" and "password" in session:
        return render_template('articles.html')
    
    return redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True)