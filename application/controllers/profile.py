from application import app
from flask import render_template, request, redirect, url_for, session
from application.models.file_manager import *
from application.models.user_manager import *

@app.route('/profile')
def profile():
	if 'logged_in' in session:
		user = User.query.get(session['user_id'])
		filename = user.profile_image
		return render_template('profile.html', filename = filename)
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/upload_image', methods=['POST'])
def upload_image():
	if 'logged_in' in session:
		image_file = request.files['profile-image']
		filename = image_file.filename
		extension = filename.split('.')[-1]
		new_file_name = str(session['user_id']) + '.' + extension
		directory = '/gs/grizzlybucket/profile/'
		filepath = directory + new_file_name
		
		save_file(image_file, filepath)
		add_profile_image(session['user_id'], new_file_name)

		return redirect(url_for('profile'))
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/image/profile/<filename>')
def get_profile_image(filename):
	directory = '/gs/grizzlybucket/profile/'
	filepath = directory + filename

	return read_file(filepath)