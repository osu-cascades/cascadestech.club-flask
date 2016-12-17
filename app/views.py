from flask import render_template
from app import app


@app.route('/')
def home(name=None):
	return "Hello World!"#render_template('index.html', name=name)