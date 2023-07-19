from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "majd"
password = "1234"
facebook_friends=["mary","roza","nabil", "joelle", "adi", "hala"]




@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method =='GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		psw = request.form['password']

		if name == username and psw == password:
			return redirect(url_for('home'))
		else:
		 return render_template('login.html')


  

@app.route('/home')  # '/' for the default page
def home():
	return render_template('home.html',ff=facebook_friends)





@app.route('/friend_exists/<string:name>', methods=['GET','POST'])  # '/' for the default page
def fe(name):
	if name in facebook_friends:
		return render_template('friend_exists.html',n=name , b=True)
	else:
		return render_template('friend_exists.html', n=name , b=False)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)