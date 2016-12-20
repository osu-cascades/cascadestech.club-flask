from flask import render_template, session, flash, redirect, url_for
from . import main
from .forms import LoginForm
from .. import db
from ..models import User

@main.route('/')
def home():
	return render_template('index.html',
							home=True,
							heroText=True)


@main.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		session['username'] = form.username.data
		flash('You were successfully logged in')
		return redirect(url_for('.home'))
	return render_template('login.html',
							home=False,
							heroText=False,
							form=form)