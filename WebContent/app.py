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

IdList = []

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
	contactList = c.contacts.query.with_entities(c.contacts.contactName, c.contacts.contactAddress, c.contacts.contactCity, c.contacts.contactZip, c.contacts.Phone, c.contacts.Email)
	dailyTaskList = c.daily_task.query.with_entities(c.daily_task.iddaily_task, c.daily_task.task, c.daily_task.place, c.daily_task.note, c.daily_task.time, c.daily_task.date)
	venuesList = c.venues.query.with_entities(c.venues.venueName, c.venues.Address, c.venues.City, c.venues.Zip, c.venues.Phone, c.venues.contactName, c.venues.layout, c.venues.URL)
	userList = c.users.query.with_entities(c.users.idUsers, c.users.username, c.users.password, c.users.department, c.users.email)
	return render_template('welcome.html', showList=showList, contactList=contactList, dailyTaskList=dailyTaskList, venuesList=venuesList, userList=userList)  # render a template

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
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		registered_user = c.users.query.filter_by(username=username).first()
		if registered_user == None or registered_user.password != password:
			error = 'Invalid Credentials. Please try again.'
			return render_template('login.html', error=error)
		return redirect(url_for('welcome'))
	return render_template('login.html')

@app.route('/database')
def database():
	"""Gives access to the inventory
	with the ability to add, edit, and delete
	inventory only select users will have that privlege.
	"""
	itemList = c.items.query.with_entities(c.items.idItems, c.items.name, c.items.quantity, c.items.code)
	return render_template('database.html', itemList=itemList)  # render a template


@app.route('/add', methods=['POST'])
def add():
	"""This function will be used to add new items into inventory
	This ability will only be given to select personal.
	"""
	if request.method == 'POST':
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
		updateItem.name = request.form['updatedName']
		updateItem.quantity = request.form['updatedQuantity']
		updateItem.mastercategory= request.form['updatedMaster_Category']
		updateItem.subcategory = request.form['updatedSub_Category']
		updateItem.pictures = request.form['updatedPictures']
		updateItem.code = request.form['updatedBarcode']
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
	"""Renders a calender.
	The calender will make it easier to visualize
	gear and their locations to avoid conflicts.
	"""
	showList = c.Shows.query.with_entities(c.Shows.idShows, c.Shows.show, c.Shows.start_date,
										   c.Shows.end_date,c.Shows.client, c.Shows.job_type,
										   c.Shows.status, c.Shows.handler,c.Shows.salesperson,
										   c.Shows.created_by)
	return render_template('calendar.html', showList=showList)

@app.route('/search')
def search():
	"""This function lets the user search
	through the database.
	"""
	q = request.args.get('q', '')
	information = c.contacts.query.filter_by(contactName=q)
	return redirect('/welcome')

@app.route('/searchShow')
def searchShow():
	"""This will let the users search
	through the existing shows in the Shows table.
	This page will only be available in the account view.
	"""
	showName = request.args.get('showName', '')
	information = c.Shows.query.filter_by(show=showName)
	return render_template('search.html', information=information)

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


@app.route('/addShow', methods=['POST'])
def addShow():
	"""This function will be used to add a new show into the Shows Table
	This ability will only be given to select personal and only shown on 
	The account page. 
	"""
	if request.method == 'POST':
		shows = c.Shows(request.form['idShows'],request.form['show'],request.form['start'],request.form['end'],request.form['show_start'],request.form['return'],request.form['venue'],request.form['client'],request.form['job_type'],request.form['status'],request.form['handler'],request.form['salesperson'],request.form['created_by'])
		c.db.session.add(shows)
		c.db.session.commit()
		return redirect('/account')

@app.route('/gearList', methods=['POST'])
def gearList():
	"""Gives access to the inventory that is assigned to a certain show.
	with the ability to add 
	inventory only select users will have that privlege.
	"""
	return render_template("gearList.html")

@app.route('/gearListWelcome', methods=['POST'])
def gearListWelcome():
	"""Gives access to the inventory that is assigned to a certain show.
	This is for the welcome page and users will be able to 
	return inventory on this page. 
	"""
	return render_template("gearListWelcome.html")

@app.route('/account/show/<int:idShows>', methods=['GET', 'POST'])
def show(idShows):
	"""This page is unique to what show the users has selected and 
	renders the GearList to show only the specific gear assigned
	to that particular show. This is for the account page.
	"""
	updateShow = c.Shows.query.get_or_404(idShows)
	if request.method == 'GET':
		itemList = c.items.query.with_entities(c.items.idItems, c.items.name, c.items.quantity, c.items.code)
		gearList = c.allocation_table.query.filter_by(id_Shows=idShows).with_entities(c.allocation_table.idallocation_table, c.allocation_table.items_id, c.allocation_table.name, c.allocation_table.quantity, c.allocation_table.quantity_available, c.allocation_table.Barcoded)
		return render_template('gearList.html', updateShow=updateShow, itemList=itemList, gearList=gearList)
	if request.method == 'POST':
		Gear = c.allocation_table(request.form['idallocation_table'], request.form['name'], request.form['items_id'], request.form['user'], request.form['id_Shows'], request.form['quantity'], request.form['start_date'], request.form['end_date'], request.form['Barcoded'], request.form['quantity_available'])
		c.db.session.add(Gear)
		c.db.session.commit()
		itemList = c.items.query.with_entities(c.items.idItems, c.items.name, c.items.quantity, c.items.code)
		gearList = c.allocation_table.query.filter_by(idallocation_table=idShows).with_entities(c.allocation_table.idallocation_table, c.allocation_table.name, c.allocation_table.quantity) #complete this
		return render_template('gearList.html', updateShow=updateShow, itemList=itemList, gearList=gearList)

@app.route('/welcome/showGear/<int:idShows>', methods=['GET', 'POST'])
def showGear(idShows):
	"""This page is unique to what show the users has selected and 
	renders the GearList to show only the specific gear assigned
	to that particular show. This is for the welcome page.
	"""
	updateShow = c.Shows.query.get_or_404(idShows)
	if request.method == 'GET':
		itemList = c.items.query.with_entities(c.items.idItems, c.items.name, c.items.quantity, c.items.code)
		gearList = c.allocation_table.query.filter_by(id_Shows=idShows).with_entities(c.allocation_table.idallocation_table, c.allocation_table.items_id, c.allocation_table.name, c.allocation_table.quantity, c.allocation_table.quantity_available, c.allocation_table.Barcoded)
		return render_template('gearListWelcome.html', updateShow=updateShow, itemList=itemList, gearList=gearList)

@app.route('/dailyTask')
def dailyTask():
	"""Gives access to the daily Tasks
	Users can see all daily tasks on the welcome page. 
	"""
	dailyTaskList = c.daily_task.query.with_entities(c.daily_task.iddaily_task, c.daily_task.task, c.daily_task.place, c.daily_task.note, c.daily_task.time, c.daily_task.date)
	return render_template('dailyTask.html', dailyTaskList=dailyTaskList)

@app.route('/addDailyTask', methods=['POST'])
def addDailyTask():
	"""This function will be used to add daily tasks.
	To the daily task table in the database. 
	"""
	if request.method == 'POST':
		dailyTask = c.daily_task(request.form['iddaily_task'], request.form['task'], request.form['place'], request.form['note'], request.form['time'], request.form['date'])
		c.db.session.add(dailyTask)
		c.db.session.commit()
		return redirect('/dailyTask')

@app.route('/dailyTask/deleteTask/<int:iddaily_task>', methods=['GET', 'POST'])
def deleteTask(iddaily_task):
	"""This function will be used to remove daily tasks.
	To the daily task table in the database. 
	"""
	deleteTask = c.daily_task.query.get_or_404(iddaily_task)
	c.db.session.delete(deleteTask)
	c.db.session.commit()
	return redirect('/dailyTask')

@app.route('/ganttView')
def ganttView():
	"""Renders a ganntt view of shows.
	The gantt view will make it easier to visualize
	gear and their locations to avoid conflicts.
	"""
	showList = c.Shows.query.with_entities(c.Shows.idShows, c.Shows.show, c.Shows.start_date, c.Shows.end_date)
	return render_template('ganttView.html', showList=showList)

@app.route('/contacts')
def contacts():
	"""Gives access to the contacts
	External and internal contacts in the database. 
	"""
	contactList = c.contacts.query.with_entities(c.contacts.contactName, c.contacts.contactAddress, c.contacts.contactCity, c.contacts.contactZip, c.contacts.Phone, c.contacts.Email)
	userList = c.users.query.with_entities(c.users.idUsers, c.users.username, c.users.password, c.users.department, c.users.email)
	return render_template('contacts.html', contactList=contactList, userList=userList)

@app.route('/addContact', methods=['POST'])
def addContact():
	"""This function will be used to add contacts.
	To the contacts table in the database. 
	"""
	if request.method == 'POST':
		contacts = c.contacts(request.form['contactName'],request.form['contactAddress'],request.form['contactCity'],request.form['contactZip'],request.form['Phone'],request.form['Email'],request.form['isEmployee'])
		c.db.session.add(contacts)
		c.db.session.commit()
		return redirect('/contacts')

@app.route('/contacts/deleteContact/<string:contactName>', methods=['GET', 'POST'])
def deleteContact(contactName):
	"""This function will be used to remove contacts.
	To the contacts table in the database. 
	"""
	deleteContact = c.contacts.query.get_or_404(contactName)
	c.db.session.delete(deleteContact)
	c.db.session.commit()
	return redirect('/contacts')

@app.route('/contacts/updateContact/<string:contactName>', methods=['GET', 'POST'])
def updateContact(contactName):
	"""This function will be used to update a selected contact.
	To the contacts table in the database. 
	"""
	updateContact = c.contacts.query.get_or_404(contactName)
	if request.method == 'GET':
		return render_template('updateContact.html', updateContact=updateContact)
	else:
		updateContact.contactName = request.form['updatedcontactName']
		updateContact.contactAddress = request.form['updatedcontactAddress']
		updateContact.contactCity = request.form['updatedcontactCity']
		updateContact.contactZip= request.form['updatedcontactZip']
		updateContact.Phone = request.form['updatedPhone']
		updateContact.Email = request.form['updatedEmail']
		updateContact.isEmployee = request.form['updatedisEmployee']
		c.db.session.commit()
		return redirect('/contacts')

@app.route('/itemList')
def itemList():
	"""Gives access to the inventory list
	This is for the welcome page alone.  
	"""
	itemList = c.items.query.with_entities(c.items.idItems, c.items.name, c.items.quantity, c.items.code)
	return render_template('itemList.html', itemList=itemList)



@app.route('/account/show/<int:idShows>/addGear/<int:idItems>', methods=['GET', 'POST'])
def addGear(idShows,idItems):
	"""This process an inventory item to be assigned to a certain show 
	and subtracts the quantity that was taken out 
	Users have this option only on the accounts page. 
	"""
	updateItem = c.items.query.get_or_404(idItems)
	updateShow = c.Shows.query.get_or_404(idShows)
	if request.method == 'GET':
		return render_template('addGear.html', updateItem=updateItem, updateShow=updateShow)
	else:
		Gear = c.allocation_table(request.form['idallocation_table'], request.form['name'], request.form['items_id'], request.form['user'], request.form['id_Shows'], request.form['quantity'], request.form['start_date'], request.form['end_date'], request.form['Barcoded'], request.form['quantity_available'])
		updateItem = c.items.query.get_or_404(request.form['items_id'])
		updateItem.quantity = int(updateItem.quantity) - int(request.form['quantity'])
		c.db.session.commit()
		c.db.session.add(Gear)
		c.db.session.commit()
		return redirect(url_for('show', idShows=idShows))

@app.route('/welcome/showGear/<int:idShows>/returnItem/<int:idallocation_table>', methods=['GET', 'POST'])
def returnItem(idShows, idallocation_table):
	"""This process an inventory item that is assigned to a show
	to be returned and adds the quantity that was taken out 
	to be added back in. Users have this option only on the welcome page. 
	"""
	if idallocation_table in IdList:
		return redirect(url_for('showGear', idShows=idShows))
	else:
		IdList.append(idallocation_table)
	updateGear = c.allocation_table.query.get_or_404(idallocation_table)
	item = c.items.query.get_or_404(updateGear.items_id)
	item.quantity = item.quantity + updateGear.quantity
	c.db.session.commit()
	return redirect(url_for('showGear',idShows=idShows))

# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=False)
