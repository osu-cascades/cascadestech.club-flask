from flask import render_template, session, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, PostForm
from .. import db
from ..models import Permission, Role, User, Post
from ..decorators import admin_required, permission_required

@main.route('/')
def home():
	return render_template('index.html')


@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.location = form.location.data
		current_user.about_me = form.about_me.data
		current_user.interests = form.interests.data
		current_user.experience = form.experience.data
		current_user.projects = form.projects.data
		current_user.grad_date = form.grad_date.data
		current_user.github = form.github.data
		current_user.linkedin = form.linkedin.data
		db.session.add(current_user)
		flash('Your profile has been updated.')
		return redirect(url_for('.user', username=current_user.username))
	form.first_name.data = current_user.first_name
	form.last_name.data = current_user.last_name
	form.location.data = current_user.location
	form.about_me.data = current_user.about_me
	form.interests.data = current_user.interests
	form.experience.data = current_user.experience
	form.projects.data = current_user.projects
	form.grad_date.data = current_user.grad_date
	form.github.data = current_user.github
	form.linkedin.data = current_user.linkedin
	return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
	user = User.query.get_or_404(id)
	form = EditProfileAdminForm(user=user)
	if form.validate_on_submit():
		user.email = form.email.data
		user.username = form.username.data
		user.confirmed = form.confirmed.data
		user.role = Role.query.get(form.role.data)
		user.first_name = form.first_name.data
		user.last_name = form.last_name.data
		user.location = form.location.data
		user.about_me = form.about_me.data
		user.interests = form.interests.data
		user.experience = form.experience.data
		user.projects = form.projects.data
		user.grad_date = form.grad_date.data
		user.github = form.github.data
		user.linkedin = form.linkedin.data
		db.session.add(user)
		flash('The profile has been updated.')
		return redirect(url_for('.user', username=user.username))
	form.email.data = user.email
	form.username.data = user.username
	form.confirmed.data = user.confirmed
	form.role.data = user.role_id
	form.first_name.data = user.first_name
	form.last_name.data = user.last_name
	form.location.data = user.location
	form.about_me.data = user.about_me
	form.interests.data = user.interests
	form.experience.data = user.experience
	form.projects.data = user.projects
	form.grad_date.data = user.grad_date
	form.github.data = user.github
	form.linkedin.data = user.linkedin
	return render_template('edit_profile.html', form=form, user=user)


@main.route('/events', methods=['GET', 'POST'])
def events():
	form = PostForm()
	if current_user.can(Permission.MODERATE) and form.validate_on_submit():
		post = Post(title=form.title.data, body=form.body.data, author=current_user._get_current_object())
		db.session.add(post)
		return redirect(url_for('.events'))
	page = request.args.get('page', 1, type=int)
	pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
		page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
	posts = pagination.items
	return render_template('events.html', form=form, posts=posts, pagination=pagination)


@main.route('/post/<int:id>')
def post(id):
	post = Post.query.get_or_404(id)
	return render_template('post.html', posts=[post])


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
	post = Post.query.get_or_404(id)
	if current_user != post.author and not current_user.is_administrator():
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.body = form.body.data
		db.session.add(post)
		flash('The post has been updated.')
		return redirect(url_for('post', id=post.id))
	form.title.data = post.title
	form.body.data = post.body
	return render_template('edit_post.html', form=form)


@main.route('/delete/<int:id>')
@login_required
def delete(id):
	post = Post.query.get_or_404(id)
	if current_user != post.author and not current_user.is_administrator():
		abort(403)
	else:
		db.session.delete(post)
		flash('The post has been removed.')
		return redirect(url_for('.events'))


@main.route('/members')
def members():
	page = request.args.get('page', 1, type=int)
	pagination = User.query.order_by(User.last_name.desc()).paginate(
		page, per_page=current_app.config['MEMBERS_PER_PAGE'], error_out=False)
	members = pagination.items
	return render_template('members.html', members=members, pagination=pagination)