# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Spitfire:12Reddoor34@tms-capstone.cglah7gng54k.us-west-2.rds.amazonaws.com/CapstoneDB'
db = SQLAlchemy(app)
app.secret_key = "super secret key"

class users(db.Model):
    __tablename__ = "users"
    idUsers = db.Column('idUsers', db.Integer, primary_key=True)
    User = db.Column('User', db.String(45))
    Password = db.Column('Password', db.String(45))

    def __init__(self, idUsers, User, Password):
        self.idUsers = idUsers
        self.User = User
        self.Password = Password

    def __repr__(self):
        return '<User %r>' % self.User
    
class item(db.Model):
    __tablename__ = "items"
    idItems = db.Column('idItems', db.Integer, primary_key=True)
    Name = db.Column('Name', db.String(45))
    Quantity = db.Column('Quantity', db.Integer)
    Barcode = db.Column('Barcode', db.String(45))
    
    def __init__(self, idItems, Name, Quantity, Barcode):
        self.idItems = idItems
        self.Name = Name
        self.Quantity = Quantity
        self.Barcode = Barcode
        
    def __repr__(self):
        return '<Item %r>' % self.Name 

# use decorators to link the function to a url
@app.route('/')
def home():
    return redirect(url_for('login'))  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = users.query.filter_by(User=username,Password=password).first()
    if  registered_user is None:
        error = 'Invalid Credentials. Please try again.'
        return render_template('login.html', error=error)
    return redirect(url_for('welcome'))

@app.route('/database')
def database():
    items = item.query.all()
    return render_template('database.html', items=items)  # render a template

@app.route('/add')
def add():
    return render_template('add.html')  # render a template

@app.route('/update')
def update(idItems):
    return render_template('update.html')  # render a template

@app.route('/delete')
def delete(idItems):
    return render_template('delete.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
