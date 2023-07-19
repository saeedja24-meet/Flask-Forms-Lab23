from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "saeed"
password = "0101"
facebook_friends=["soshi","macloba","cosa w wark dwale", "baked cheese cake", "ktaf", "abocado"]


@app.route('/',methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		nameInter=request.form['username']  
		passwordInter=request.form['password']
		if(nameInter==username and passwordInter==password):
			return redirect(url_for('home')) 
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')


@app.route('/home')
def home():
	return render_template("home.html",htmlFacbebook=facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
@app.route('/home/<string:name>')
def /friend_exists(name):
