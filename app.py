from flask import Flask, render_template, redirect, url_for, flash, session, g
from forms import Login
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdregwer456345634trgwer'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)  # Log out after X amount minutes


users = [
	{
		'id': 1,
		'username': 'jurgen',
		'password': 'test'
	}
]


@app.before_request
def before_request():
	session.permanent = True
	g.user = None
	if 'user_id' in session:
		user = [x for x in users if x['id'] == session['user_id']][0]
		g.user = user
	

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/admin')
def admin():
	if g.user:
		return render_template('admin.html')
	return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		session.pop('user_id', None)
		username = form.username.data
		password = form.password.data
		user = {'id': 1, 'username': 'jurgen', 'password': 'test'}
		if user['username'] == username and user['password'] == password:
			session['user_id'] = user['id']
			return redirect(url_for('admin'))
		flash('Please check Username or Password and try again', 'danger')
		return redirect(url_for('login'))
	return render_template('login.html', form=form)


@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('user_id', None)
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run()
