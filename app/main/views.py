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