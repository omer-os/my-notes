# flask notes

# basic flask app 
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>page 1</h1>'

@app.route('/page2')
def page2():
    return '<h1>page 2</h1>'

if __name__=='__main__':
    app.run(debug=True)

```



```python
@app.route('/page2/<string:name>/<int:id>')
def page2(name,id):
    return f'<h1>hello {name}, your id is {id}</h1>'
```

<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

## adding html file to flask app

```templates/home.html
<p>hello world</p>
```

```python
from flask import Flask,render_template
@app.route('/home)
def home():
    return render_template('home.html)
```



## HTTP methods , GET and POST and saving to sessions

``` python
from flask import Flask
from flask.globals import request, session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from datetime import timedelta


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=5)
app.secret_key = 'helloworld'

@app.route('/')
def homePage():
    return render_template('homepage.html')

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method=="POST":
        name = request.form["name"]
        email = request.form["email"]
        session["name"] = name
        session["email"] = email
        session.permanent_session_lifetime = True
        
        return redirect(url_for('sginin'))
    
    else:
        if "name" in session:
            return render_template('articles.html')
 
        return render_template('login.html')

@app.route('/articles')
def sginin():
    if "name" in session:
        return render_template('articles.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop("name", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
```