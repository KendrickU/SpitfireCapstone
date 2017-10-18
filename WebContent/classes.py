from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

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
    
class items(db.Model):
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

class Shows(db.Model):
	__tablename__ = "Shows"
	idShows = db.Column('idShows', db.Integer, primary_key=True)
	show = db.Column('show', db.String(100))
	production = db.Column('production', db.String(45))
	start_date = db.Column('start date', db.String(45))
	end_date = db.Column('end date', db.String(45))
	
	def __init__(self, idShows, show, production, start_date, end_date):
		self.idShows = idShows
		self.show = show
		self.production = production
		self.start_date = start_date
		self.end_date = end_date
	
	def __repr__(self):
		return '<Show> %r' % self.show
	
#item = items(123, "123", 213, "12")
#db.session.add(item)
#db.session.commit()
#db.session.query.filter_by(attribute).delete()
#db.session.commit()

#{"user":"hello", "pass":"test}
#{"command":"update/remove/add", "table":"users/items", (whatever information is used)}

#request.form['username'] != 'admin' or request.form['password'] != 'admin' 