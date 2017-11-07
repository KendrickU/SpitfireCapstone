# import the Flask class from the flask module
# Create a new table for a new show
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import classes as c
import json
"""@package docstring
Documentation for this module.
More details.
"""
# create the application object
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Spitfire:12Reddoor34@tms-capstone.cglah7gng54k.us-west-2.rds.amazonaws.com/CapstoneDB'
db = SQLAlchemy(app)
app.secret_key = "super secret key"


# use decorators to link the function to a url
@app.route('/')
def home():
	"""Redircts to the login page.
	"""
	return redirect(url_for('login'))  # return a string

@app.route('/welcome')
def welcome():
	"""This will the main page for users
	that work. They will be able to check status on inventory
	and assign them to shows.
	"""
	showList = c.Shows.query.with_entities(c.Shows.idShows, c.Shows.show, c.Shows.start_date, c.Shows.end_date)
	return render_template('welcome.html', showList=showList)  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
	"""The login page
	users will provide a username and password if correct
	will direct them to the welcome/main page.
	"""
	error = None
	if request.method == 'GET':
		return render_template('login.html')
	username = request.form['username']
	password = request.form['password']
	registered_user = c.users.query.filter_by(username=username).first()
	if registered_user == None or registered_user.password != password:
		error = 'Invalid Credentials. Please try again.'
		return render_template('login.html', error=error)
	return redirect(url_for('welcome'))

@app.route('/database')
def database():
	"""Gives access to the inventory
	with the ability to add, edit, and delete
	inventory only select users will have that privlege.
	"""
	itemList = c.items.query.with_entities(c.items.idItems, c.items.name, c.items.quantity, c.items.code)
	return render_template('database.html', itemList=itemList)  # render a template
	

@app.route('/add', methods=['GET', 'POST'])
def add():
	"""This function will be used to add new items into inventory
	This ability will only be given to select personal.
	"""
	item = c.items(request.form['idItems'], request.form['name'], request.form['quantity'], request.form['mastercategory'], request.form['subcategory'], request.form['pictures'], request.form['code'])
	c.db.session.add(item)
	c.db.session.commit()
	return redirect('/database')

@app.route('/database/update/<int:idItems>', methods=['GET', 'POST'])
def update(idItems):
	"""Lets the user edit items already in inventory.
	Only select users will be able to modify inventory.
	"""
	updateItem = c.items.query.get_or_404(idItems)
	if request.method == 'GET':
		return render_template('update.html', updateItem=updateItem)
	else:
		updateItem.idItems = request.form['updatedidItems']
		updateItem.Name = request.form['updatedName']
		updateItem.Quantity = request.form['updatedQuantity']
		updateItem.MasterCategory = request.form['updatedMaster_Category']
		updateItem.Sub_Category = request.form['updatedSub_Category']
		updateItem.Pictures = request.form['updatedPictures']
		updateItem.Barcode = request.form['updatedBarcode']
		c.db.session.commit()
		return redirect('/database')

@app.route('/database/delete/<int:idItems>', methods=['GET', 'POST'])
def delete(idItems):
	"""This function give the user the
	ability to delete items from inventory.
	"""
	deleteItem = c.items.query.get_or_404(idItems)
	c.db.session.delete(deleteItem)
	c.db.session.commit()
	return redirect('/database')

@app.route('/calendar')
def calendar():
	"""Rednders a calender.
	The calender will make it easier to visualize
	gear and their locations to aviod confilicts.
	"""
	return render_template("calendar.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
	"""This function lets the user search
	through the database.
	"""
	q = request.args.get('q', '')
	information = c.contacts.query.filter_by(contactName=q)
	return redirect('/welcome')
	
@app.route('/account')
def account():
	"""The function is used to render the page used
	on the account rep side.
	This includes the ability to create, edit, and delete shows.
	"""
	showList = c.Shows.query.with_entities(c.Shows.idShows, c.Shows.show, c.Shows.start_date,
										   c.Shows.end_date,c.Shows.client, c.Shows.job_type,
										   c.Shows.status, c.Shows.handler,c.Shows.salesperson,
										   c.Shows.created_by)
	return render_template('account.html', showList=showList)


@app.route('/addShow', methods=['GET', 'POST'])
def addShow():
	if request.method == 'POST':
		shows = c.Shows(request.form['idShows'],request.form['show'],request.form['start'],request.form['end'],request.form['show_start'],request.form['return'],request.form['venue'],request.form['client'],request.form['job_type'],request.form['status'],request.form['handler'],request.form['salesperson'],request.form['created_by'])
		c.db.session.add(shows)
		c.db.session.commit()
		return redirect('/account')


# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)
