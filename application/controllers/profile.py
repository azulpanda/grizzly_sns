from application import app
from flask import render_template, request, redirect, url_for, session
from application.models.file_manager import *
from application.models.user_manager import *
# 바꾸삼

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
		new_filename = '%d.%s' % (session['user_id'], image_file.filename.split('.')[-1])
		image_path = app.config['IMAGE_UPLOAD_DIR'] + new_filename
		
		file_manager.save_image(image_file, image_path)
		user_manager.add_profile_image(session['user_id'], new_filename)
		return redirect(url_for('profile'))
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/image/profile/<filename>')
def get_profile_image(filename):
	return file_manager.read_profile_image(app.config['IMAGE_UPLOAD_DIR'] + filename)