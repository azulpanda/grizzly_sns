from flask import render_template, session, request
from application import app
from application.models.schema import *
from application.models.user_manager import *
from application.models.post_manager import *

@app.route('/', defaults={'wall_id':0})
@app.route('/wall/<int:wall_id>', methods = ['GET', 'POST'])
def wall(wall_id):
	if 'logged_in' in session:
		if User.query.get(wall_id) != None:
			wall_email = get_email(wall_id)
			if request.method == 'POST':
				start = int(request.form['start'])
				end = int(request.form['end'])
				posts = []
				raw_posts = Post.query.filter(Post.wall_id == wall_id).all()
				for i in raw_posts:
					if i.is_secret==False or session['user_id'] in [i.user_id, i.wall_id]:
						posts.append(read_post(i.id))
				if end>len(posts):
					ordered_posts = sorted(posts, key=lambda k: k['created_time'], reverse=True)[start:]
					no_more = True
				else:
					ordered_posts = sorted(posts, key=lambda k: k['created_time'], reverse=True)[start:end]
					no_more = False
				return render_template('wall_posts.html', ordered_posts = ordered_posts, no_more = no_more)
			else:
				return render_template('wall.html', wall_email = wall_email, wall_id = wall_id)
		else:
			return render_template('layout.html', error = 'No user')
	else:
		return render_template('layout.html', error = 'Log in')