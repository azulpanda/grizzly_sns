from flask import render_template, redirect, request, url_for
from application import app
from application.models import user_manager
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, RadioField,	validators
from wtforms.fields.html5 import DateField

def existing_email(form, field):
	if User.query.filter(User.email == form.email.data).all() != []:
		raise validators.ValidationError(u'existing email')

class SignupForm(Form):
	email = StringField(
		u'email',
		[
			validators.data_required(message=u'please enter email'),
			validators.Email(message=u'use email form'),
			existing_email
		],
		description = {'placehoder': u'likelion@gmail.com'}
	)
	username = StringField(
		u'username',
		[
			validators.data_required(message=u'please enter username')
		],
		description = {'placehoder': u'aslan'}
	)
	password = PasswordField(
		u'password',
		[
			validators.data_required(message=u'please enter password'),
			validators.length(min=8, max=20, message=u'password should be 8-20 characters')
		],
		description = {'placehoder': u'password'}
	)
	retype_password = PasswordField(
		u'retype_password',
		[
			validators.data_required(message=u'please retype password'),
			validators.EqualTo('password', message=u'wrong password')
		],
		description = {'placehoder': u'password'}
	)
	gender = RadioField(
		u'gender',
		choices=[('m', 'Male'), ('f', 'Female')]
	)
	mobile = StringField(
		u'mobile',
		[
			validators.data_required(message=u'please enter mobile')
		],
		description = {'placehoder': u'010-1234-5678'}
	)
	birthday = DateField(
		u'birthday'
	)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	if request.method == 'POST':
		form = SignupForm()
		if form.validate_on_submit():
			user_manager.add(form)
			return redirect(url_for('login'))
		else: 
			return render_template('signup.html', form = form)
	else:
		form = SignupForm()
		return render_template('signup.html', form = form)