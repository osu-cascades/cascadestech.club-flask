from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, DateField, SelectField, PasswordField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo, URL, Optional
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class EditProfileForm(Form):
	name = StringField('First Name', validators=[Length(0, 64)], render_kw={"placeholder" : "Enter your first name"})
	last = StringField('Last Name', validators=[Length(0, 64)], render_kw={"placeholder" : "Enter your last name"})
	location = StringField('Location', validators=[Length(0, 64)], render_kw={"placeholder" : "Where are you from?"})
	about_me = TextAreaField('About Me', render_kw={"placeholder" : "Enter some information about yourself"})
	interests = TextAreaField('Interests', render_kw={"placeholder" : "Enter some of your interests, professionally or otherwise"})
	experience = TextAreaField('Experience', render_kw={"placeholder" : "Enter some of your relevant work history"})
	projects = TextAreaField('Projects', render_kw={"placeholder" : "Enter some information about some projects you're working on"})
	grad_date = DateField('Graduation Date', format='%m/%d/%Y', render_kw={"placeholder" : "mm/dd/yyyy"})
	github = StringField('GitHub', validators=[Optional(strip_whitespace=True), URL(message='Not a valid URL')], render_kw={"placeholder" : "Enter your GitHub URL: https://github.com/YourUsername"})
	linkedin = StringField('LinkedIn', validators=[Optional(strip_whitespace=True), URL(message='Not a valid URL')], render_kw={"placeholder" : "Enter your LinkedIn URL: https://www.linkedin.com/in/YourUsername"})
	submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
													0, 'Usernames must have only letters, numbers, dots, or underscores')])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role', coerce=int)
	name = StringField('First Name', validators=[Length(0, 64)])
	last = StringField('Last Name', validators=[Length(0, 64)])
	location = StringField('Location', validators=[Length(0, 64)])
	about_me = TextAreaField('About Me')
	interests = TextAreaField('Interests')
	experience = TextAreaField('Experience')
	projects = TextAreaField('Projects')
	grad_date = DateField('Graduation Date', format='%m/%d/%Y')
	github = StringField('GitHub', validators=[Optional(strip_whitespace=True), URL(message='Not a valid URL')])
	linkedin = StringField('LinkedIn', validators=[Optional(strip_whitespace=True), URL(message='Not a valid URL')])
	submit = SubmitField('Submit')

	def __init__(self, user, *args, **kwargs):
		super(EditProfileAdminForm, self).__init__(*args, **kwargs)
		self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
		self.user = user

	def validate_email(self, field):
		if field.data != self.user.email and User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if field.data != self.user.username and User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')


class PostForm(Form):
	title = StringField('Title', validators=[Required()], render_kw={"placeholder" : "Enter a title for the event"})
	body = PageDownField('Body', validators=[Required()], render_kw={"placeholder" : "Enter the important info about the event. Date, time, etc."})
	submit = SubmitField('Submit')