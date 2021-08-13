from datetime import timedelta
from flask import Flask
from flask.globals import request, session
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import url
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = 'ofeoni3pomoimrg'
app.permanent_session_lifetime = timedelta(days=10)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Articles.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Body = db.Column(db.String(100))

    def __init__(self, Title, Body):
        self.Title = Title
        self.Body = Body





@app.route('/')
def home():
    return redirect(url_for('articles'))


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method=="POST":
        app.permanent = True

        session["name"] = request.form["name"]
        session["password"] = request.form["password"]

        return redirect(url_for('articles'))
    
    if "name" in session:
        return redirect(url_for('articles'))

    return render_template('login.html')






@app.route('/articles', methods = ['GET', 'POST'])
def articles():
    
    if "name" in session:
        if request.method=="POST":
            new_article = Articles(request.form["Title"], request.form["Body"])

            db.session.add(new_article)
            db.session.commit()
            return render_template('articles.html', Arts=Articles.query.all())

        return render_template('articles.html', Arts=Articles.query.all())

    
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop("name", None)

    return redirect(url_for('login'))


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)