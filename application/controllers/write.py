from flask import render_template, session, redirect, request, url_for
from application import app
from application.models.schema import *
from application.models.user_manager import *
from application.models.post_manager import *

@app.route('/', defaults={'wall_id':0})
@app.route('/write/<int:wall_id>', methods = ['GET', 'POST'])
def write(wall_id):
	if 'logged_in' in session:
		if User.query.get(wall_id) != None:
			wall_email = get_email(wall_id)
			if request.method == 'POST':
				add_post(request.form, session['user_id'], wall_id)
				return redirect(url_for('wall', wall_id=wall_id))
			else:
				return render_template('write.html', wall_email = wall_email, wall_id = wall_id)
		else:
			return render_template('layout.html', error = 'No user')
	else:
		return render_template('layout.html', error = 'Log in')