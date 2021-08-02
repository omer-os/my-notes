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
