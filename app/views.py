from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
def home():
	return render_template('index.html',
							home=True,
							heroText=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
				(form.username.data, str(form.remember_me.data)))
		return redirect('/')
	return render_template('login.html',
							home=False,
							heroText=False,
							form=form)