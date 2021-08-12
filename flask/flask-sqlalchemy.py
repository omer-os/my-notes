from flask import Flask, render_template, request, flash, redirect, url_for

# importing 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# adding database location
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

#createing database
db = SQLAlchemy(app)
class students(db.Model):
    # id is the id of each column , primary_key means that each column should have different id from each other

   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))

def __init__(self, name, city, addr,):
   self.name = name
   self.city = city
   self.addr = addr







@app.route('/')
def index():
    # passing data to html page 
    return render_template('index.html', students=students.query.all())



# add new element
@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')




if __name__=='__main__':
   db.create_all()
   # dadabase created
   app.run(debug=True)