from flask import render_template, session, request
from application import app
from application.models.schema import *
from application.models.post_manager import *
from application.models.follow_manager import *

@app.route('/newsfeed', methods=['GET', 'POST'])
def newsfeed():
	if 'logged_in' in session:
		if request.method == 'POST':
			start = int(request.form['start'])
			end = int(request.form['end'])	
			vip_id = [session['user_id']]
			for i in get_followee(session['user_id']):
				vip_id.append(i.followee.id)
			posts = []
			vip_posts = []
			for i in Post.query.filter(Post.user_id.in_(vip_id)):
				if i.is_secret==False or session['user_id'] in [i.user_id, i.wall_id]:
					posts.append(read_post(i.id))
			for i in Post.query.filter(Post.wall_id.in_(vip_id)):
				if i.is_secret==False or session['user_id'] in [i.user_id, i.wall_id]:
					posts.append(read_post(i.id))
			for i in posts:
				if i not in vip_posts:
					vip_posts.append(i)
			if end>len(vip_posts):
				ordered_posts = sorted(vip_posts, key=lambda k: k['created_time'], reverse=True)[start:]
				no_more = True
			else:
				ordered_posts = sorted(vip_posts, key=lambda k: k['created_time'], reverse=True)[start:end]
				no_more = False
			return render_template('newsfeed_posts.html', ordered_posts = ordered_posts, no_more = no_more)
		else:
			return render_template('newsfeed.html')
	else:
		return render_template('layout.html', error = 'Log in')