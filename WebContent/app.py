from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import classes as c

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Spitfire:12Reddoor34@tms-capstone.cglah7gng54k.us-west-2.rds.amazonaws.com/CapstoneDB'
db = SQLAlchemy(app)

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
    if request.method == 'POST':
		holder = c.users.query.get(request.form['username'])
		if holder != None:
			if holder.Password != request.form['password']:
				error = 'Invalid Credentials. Please try again.'
			else:
				return redirect(url_for('database'))
		else:
			error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/database')
def database():
	if request.method == 'POST':
		if request.form['query'] == add:
			return redirect(url_for('add'))
		if request.form['query'] == update:
			return redirect(url_for('update'))
		if request.form['query'] == delete:
			return redirect(url_for('delete))
		if request.form['query'] == read:
			return redirect(url_for('read')
			
@app.route('/add')
def add():
	if request.method == 'POST':
		item = c.items(request.form['idItems'], request.form['Name'], request.form['Quantity'], request.form['Barcode']
		c.db.session.add(item)
		c.db.session.commit()
		
@app.route('/update')
def update():
	
	
@app.route('/delete')
def delete():
	if request.method == 'POST':
		c.items.query.filter_by(idItems=request.form['id']).delete()
		c.db.session.commit()
	
@app.route('/read')
def read():



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
	