from application import db
from schema import *

def add_user(form):
	user = User(
		email = form.email.data, 
		username = form.username.data, 
		gender = form.gender.data, 
		password = db.func.md5(form.password.data), 
		mobile = form.mobile.data, 
		birthday = form.birthday.data
	)
	db.session.add(user)
	db.session.commit()

def get_id(email):
	return User.query.filter(User.email == email).all()[0].id

def get_email(id):
	return User.query.get(id).email

def login_check(email, password):
	return User.query.filter(User.email == email, User.password == db.func.md5(password))

def add_profile_image(user_id, filename):
	user = User.query.get(user_id)
	user.profile_image = filename
	db.session.commit()
