from flask import render_template, session, redirect, request, url_for
from application import app
from application.models.schema import *
from application.models.user_manager import *
from flask.ext.wtf import Form
from wtforms import (
	StringField,
	PasswordField
)
from wtforms import validators

class UserForm(Form):
	email = StringField(
		u'email',
		[
			validators.data_required(message=u'please enter email'),
			validators.Email(message=u'use email form')
		],
		description = {'placehoder': u'likelion@gmail.com'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter password')
		],
		description = {'placehoder': u'QWERqwer!@#$1234'}
	)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		form = UserForm()
		if form.validate_on_submit():
			user = login_check(form.email.data, form.password.data)
			if user.count() == 1:
				user = user.one()
				session['user_id'] = user.id
				session['email'] = user.email
				session['logged_in'] = True
				return redirect(url_for('wall'))
			else:
				login_error = "wrong email or password"
				return render_template('login.html', form = form, login_error = login_error)
		else:
			return render_template('login.html', form = form)
	else:
		form = UserForm()
		return render_template('login.html', form = form)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.pop('email', None)
	return redirect(url_for('layout'))