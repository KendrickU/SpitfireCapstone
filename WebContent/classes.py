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
    name = db.Column('name', db.String(45))
    quantity = db.Column('quantity', db.Integer)
    mastercategory = db.Column('master_category', db.String(45))
    subcategory = db.Column('sub_category', db.String(45))
    pictures = db.Column('pictures', db.String(45))
    code = db.Column('code', db.String(45))

    def __init__(self, idItems, name, quantity, mastercategory, subcategory, pictures, code):
        self.idItems = idItems
        self.name = name
        self.quantity = quantity
        self.mastercategory = mastercategory
        self.subcategory = subcategory
        self.pictures = pictures
        self.code = code

    def __repr__(self):
        return '<Item %r>' % self.Name


class Shows(db.Model):
    __tablename__ = "Shows"
    idShows = db.Column('idShows', db.Integer, primary_key=True)
    show = db.Column('show', db.String(45))
    start_date = db.Column('start', db.DateTime)
    end_date = db.Column('end', db.DateTime)
    show_start = db.Column('show_start', db.DateTime)
    return_date = db.Column('return', db.DateTime)
    venue = db.Column('venue', db.String(45))
    client = db.Column('client', db.String(45))
    job_type = db.Column('job_type', db.String(45))
    status = db.Column('status', db.String(45))
    handler = db.Column('handler', db.String(45))
    salesperson = db.Column('salesperson', db.String(45))
    created_by = db.Column('created_by', db.String(45))

    def __init__(self, idShows, show, start_date, end_date, show_start, return_date, venue, client,
                 job_type, status, handler, salesperson, created_by):
        self.idShows = idShows
        self.show = show
        self.start_date = start_date
        self.end_date = end_date
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
    Name = db.Column('name', db.String(45))
    Quantity = db.Column('quantity', db.Integer)
    Barcode = db.Column('code', db.String(45))
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

class allocation_table(db.Model):
    __tablename__ = "allocation_table"
    idallocation_table = db.Column("idallocation_table", db.Integer, primary_key=True)
    name = db.Column("name", db.String(45))
    items_id = db.Column("items_id", db.Integer)
    user = db.Column("user", db.String(45))
    id_Shows = db.Column("id_Shows", db.Integer)
    quantity = db.Column("quantity", db.Integer)
    start_date = db.Column("start_date", db.DateTime)
    end_date = db.Column("end_date", db.DateTime)
    Barcoded = db.Column("Barcoded", db.String(45))
    quantity_available = db.Column("quantity_available", db.Integer)

    def __init__(self, idallocation_table, name, items_id, user, id_Shows, quantity, start_date, end_date, Barcoded, quantity_available):
        self.idallocation_table = idallocation_table
        self.name = name
        self.items_id = items_id
        self.user = user
        self.id_Shows = id_Shows
        self.quantity = quantity
        self.start_date = start_date
        self.end_date = end_date
        self.Barcoded = Barcoded
        self.quantity_available = quantity_available

    @classmethod
    def find_quantity(cls, items_id, itemsList):
        total_quantity = 0
        for items in itemsList:
            if items_id == items.idItems:
                total_quantity = total_quantity + items.quantity
        return total_quantity

    def __repr(self):
        return '<allocation> %r' % self.name

class daily_task(db.Model):
    __tablename__="daily_task"
    iddaily_task = db.Column("iddaily_task", db.String(50), primary_key=True)
    task = db.Column("task", db.String(50))
    place = db.Column("place", db.String(50))
    note = db.Column("note", db.String(50))
    time = db.Column("time", db.String(10))
    date = db.Column("date", db.String(15))

    def __init__(self, iddaily_task, task, place, note, time, date):
        self.iddaily_task = iddaily_task
        self.task = task
        self.place = place
        self.note = note
        self.time = time
        self.date = date

    def __repr__(self):
        return '<daily_task> %r' % self.task

        # item = items(123, "123", 213, "12")
        # db.session.add(item)
        # db.session.commit()
        # db.session.query.filter_by(attribute).delete()
        # db.session.commit()

        # {"user":"hello", "pass":"test}
        # {"command":"update/remove/add", "table":"users/items", (whatever information is used)}

        # request.form['username'] != 'admin' or request.form['password'] != 'admin'
