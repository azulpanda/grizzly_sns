from application import app
from flask import render_template, request, session, redirect, url_for
from application.models.user_manager import *
from application.models.follow_manager import *
from application.models.schema import *
import json

@app.route('/follow', methods=['GET', 'POST'])
def follow():
	if 'logged_in' in session:
		followees = []
		followers = []
		for i in get_followee(session['user_id']):
			followees.append({'user_id':i.followee.id, 'username':i.followee.username, 'email':i.followee.email})
		for i in get_follower(session['user_id']):
			followers.append({'user_id':i.follower.id, 'username':i.follower.username, 'email':i.follower.email})
		return render_template('follow.html', followers = followers, followees = followees)
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/search_user', methods=['POST'])
def search_user():
	if 'logged_in' in session:
		username = request.form['username']
		raw_user = User.query.filter(User.username.like('%'+username+'%')).all()
		user_list = []
		for i in raw_user:
			user_list.append({'user_id':i.id, 'username':i.username, 'email':i.email})
		return json.dumps(user_list)
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/', defaults={'follow_id':0})
@app.route('/start_follow/<int:follow_id>', methods=['POST'])
def start_follow(follow_id):
	if 'logged_in' in session:
		if User.query.get(follow_id) != None:
			add_follow(session['user_id'], follow_id)
			return redirect(url_for('follow'))
		else:
			return render_template('layout.html', error = 'No user to follow')
	else:
		return render_template('layout.html', error = 'Log in')
				


				# on_my_wall = Post.query.filter(Post.wall_id == session['user_id'])
				# i_wrote = 
				# following_posts = 