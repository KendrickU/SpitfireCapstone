from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

class items(db.Model):
	idItems = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(45))
	Quantity = db.Column(db.Integer)
	Barcode = db.Column(db.String(45))
	
	def __init__(self, idItems, Name, Quantity, Barcode):
		self.idItems = idItems
		self.Name = Name
		self.Quantity = Quantity
		self.Barcode = Barcode
		
	def __repr__(self):
		return '<Item %r>' % self.Name 
class users(db.Model):
	idUsers = db.Column(db.Integer, primary_key=True)
	User = db.Column(db.String(45))
	Password = db.Column(db.String(45))
	
	def __init__(self, idUsers, User, Password):
		self.idUsers = idUsers
		self.User = User
		self.Password = Password
	
	def __repr__(self):
		return '<User %r>' % self.User

#item = items(123, "123", 213, "12")
#db.session.add(item)
#db.session.commit()
#db.session.query.filter_by(attribute).delete()
#db.session.commit()

#{"user":"hello", "pass":"test}
#{"command":"update/remove/add", "table":"users/items", (whatever information is used)}

#request.form['username'] != 'admin' or request.form['password'] != 'admin'