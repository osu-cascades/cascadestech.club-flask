from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)

	@app.route('/')
	def home():
		return render_template('index.html',
							home=True,
							heroText=True)

	@app.route('/login', methods=['GET', 'POST'])
	def login():
		form = LoginForm()
		if form.validate_on_submit():
			session['username'] = form.username.data
			flash('You were successfully logged in')
			return redirect(url_for('home'))
		return render_template('login.html',
								home=False,
								heroText=False,
								form=form)

	from .main import main as main_blueprint 
	app.register_blueprint(main_blueprint)

	return app