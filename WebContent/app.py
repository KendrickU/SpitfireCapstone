# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import classes as c

# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Spitfire:12Reddoor34@tms-capstone.cglah7gng54k.us-west-2.rds.amazonaws.com/CapstoneDB'
db = SQLAlchemy(app)
app.secret_key = "super secret key"

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
    registered_user = c.users.query.filter_by(User=username,Password=password).first()
    if  registered_user is None:
        error = 'Invalid Credentials. Please try again.'
        return render_template('login.html', error=error)
    return redirect(url_for('welcome'))

@app.route('/database')
def database():
    itemList = c.items.query.all()
    return render_template('database.html', itemList=itemList)  # render a template

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'GET':
		return render_template('add.html')
	else:
		item = c.items(request.form['idItems'], request.form['Name'], request.form['Quantity'], request.form['Barcode'])
		c.db.session.add(item)
		c.db.session.commit()
		return redirect('/database')

@app.route('/database/update/<int:idItems>', methods=['GET', 'POST'])
def update(idItems):
	updateItem = c.items.query.filter_by(idItems=idItems).first()
	if request.method == 'GET':
		return render_template('update.html', updateItem=updateItem)
	else:
		updateItem.idItems = request.form['updatedidItems']
		updateItem.Name = request.form['updatedName']
		updateItem.Quantity = request.form['updatedQuantity']
		updateItem.Barcode = request.form['updatedBarcode']
		c.db.session.commit()
		return redirect('/database')

@app.route('/database/delete/<int:idItems>', methods=['GET', 'POST'])
def delete(idItems):
	deleteItem = c.items.query.get_or_404(idItems)
	c.db.session.delete(deleteItem)
	c.db.session.commit()
	return redirect('/database')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
