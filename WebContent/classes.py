from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

class users(db.Model):
	__tablename__ = "users"
	idUsers = db.Column('idUsers', db.Integer, primary_key=True)
	username = db.Column('username', db.String(45))
	password = db.Column('password', db.String(45))
	department = db.Column('department', db.String(45))
	email = db.Column('email', db.String(45))

	def __init__(self, idUsers, username, password, department, email):
		self.idUsers = idUsers
		self.username = username
		self.password = password
		self.department = department
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.User

class items(db.Model):
	__tablename__ = "items"
	idItems = db.Column('idItems', db.Integer, primary_key=True)
	Name = db.Column('Name', db.String(45))
	Quantity = db.Column('Quantity', db.Integer)
	MasterCategory = db.Column('Master_Category', db.String(45))
	Sub_Category = db.Column('Sub_Category', db.String(45))
	Pictures = db.Column('Pictures', db.BLOB)
	Barcode = db.Column('Barcode', db.String(45))
    
	def __init__(self, idItems, Name, Quantity, MasterCategory, Sub_Category, Pictures, Barcode):
		self.idItems = idItems
		self.Name = Name
		self.Quantity = Quantity
		self.MasterCategory = MasterCategory
		self.Sub_Category = Sub_Category
		self.Pictures = Pictures
		self.Barcode = Barcode
		
	def __repr__(self):
		return '<Item %r>' % self.Name 

class Shows(db.Model):
	__tablename__ = "Shows"
	idShows = db.Column('idShows', db.Integer, primary_key=True)
	show = db.Column('show', db.String(45))
	start_date = db.Column('start', db.DateTime)
	end_date = db.Column('end', db.DateTime)
	load_in = db.Column('load-in', db.DateTime)
	show_start = db.Column('show_start', db.DateTime)
	load_out = db.Column('load-out', db.DateTime)
	return_date = db.Column('return', db.DateTime)
	venue = db.Column('venue', db.String(45))
	client = db.Column('client', db.String(45))
	job_type = db.Column('job_type', db.String(45))
	status = db.Column('status', db.String(45))
	handler = db.Column('handler', db.String(45))
	salesperson = db.Column('salesperson', db.String(45))
	created_by = db.Column('created_by', db.String(45))
	
	def __init__(self, idShows, show, start_date, end_date, load_in, show_start, load_out, return_date, venue, client, job_type, status, handler, salesperson, created_by):
		self.idShows = idShows
		self.show = show
		self.start_date = start_date
		self.end_date = end_date
		self.load_in = load_in
		self.load_out = load_out
		self.return_date = return_date
		self.venue = venue
		self.client = client
		self.job_type = job_type
		self.status = status
		self.handler = handler
		self.salesperson = salesperson
		self.created_by = created_by
	
	def __repr__(self):
		return '<Show> %r' % self.show
	
class contacts(db.Model):
	__tablename__ = "contacts"
	contactName = db.Column('contactName', db.String(55), primary_key=True)
	contactAddress = db.Column('contactAddress', db.String(55))
	contactCity = db.Column('contactCity', db.String(45))
	contactZip = db.Column('contactZip', db.Integer)
	Phone = db.Column('Phone', db.String(14))
	Email = db.Column('Email', db.String(255))
	isEmployee = db.Column('isEmployee', db.String(1))
	
	def __init__(self, contactName, contactAddress, contactCity, contactZip, Phone, Email, isEmployee):
		self.contactName = contactName
		self.contactAddress = contactAddress
		self.contactCity = contactCity
		self.contactZip = contactZip
		self.Phone = Phone
		self.Email = Email
		self.isEmployee = isEmployee
		
	def __repr__(self):
		return '<contactName> %r' % self.contactName
	
class jobGear(db.Model):
	__tablename__ = "jobGear"
	idItems = db.Column('idItems', db.Integer, primary_key=True)
	Name = db.Column('Name', db.String(45))
	Quantity = db.Column('Quantity', db.Integer)
	Barcode = db.Column('Barcode', db.String(45))
	show = db.Column('show', db.String(45))
	
	def __init__(self, idItems, Name, Quantity, Barcode, show):
		self.idItems = idItems
		self.Name = Name
		self.Quantity = Quantity
		self.Barcode = Barcode
		self.show = show
		
	def __repr__(self):
		return '<jobGear> %r' % self.Name
	
class types(db.Model):
	__tablename__ = "types"
	Type = db.Column('Type', db.String(45), primary_key=True)
	
	def __init__(self, Type):
		self.Type = Type
	
	def __repr__(self):
		return '<types> %r' % self.Type
	
class venues(db.Model):
	__tablename__ = "venues"
	venueName = db.Column('venueName', db.String(55), primary_key=True)
	Address = db.Column('Address', db.String(255))
	City = db.Column('City', db.String(255))
	Zip = db.Column('Zip', db.String(255))
	Phone = db.Column('Phone', db.String(14))
	contactName = db.Column('contactName', db.String(55))
	layout = db.Column('layout', db.String(255))
	URL = db.Column('URL', db.String(55))
	
	def __init__(self, venueName, Address, City, Zip, Phone, contactName, layout, URL):
		self.venueName = venueName
		self.Address = Address
		self.City = City
		self.Zip = Zip
		self.Phone = Phone
		self.contactName = contactName
		self.layout = layout
		self.URL = URL
		
	def __repr__(self):
		return '<venues> %r' % self.venueName
	
	
#item = items(123, "123", 213, "12")
#db.session.add(item)
#db.session.commit()
#db.session.query.filter_by(attribute).delete()
#db.session.commit()

#{"user":"hello", "pass":"test}
#{"command":"update/remove/add", "table":"users/items", (whatever information is used)}

#request.form['username'] != 'admin' or request.form['password'] != 'admin' 