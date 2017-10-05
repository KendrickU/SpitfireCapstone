# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import classes as c

# create the application object
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
				return redirect(url_for('home'))
		else:
			error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
	
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
	