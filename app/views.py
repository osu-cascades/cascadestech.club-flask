from flask import render_template
from app import app


@app.route('/')
def home(name=None):
	return render_template('index.html', name=name)