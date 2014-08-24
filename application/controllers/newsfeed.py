from flask import render_template, session, request
from application import app
from application.models import post_manager,follow_manager

@app.route('/newsfeed', methods=['GET', 'POST'])
def newsfeed():
	if 'logged_in' in session:
		if request.method == 'POST':
			start = int(request.form['start'])
			end = int(request.form['end'])
			vip_id = [session['user_id']]
			for i in follow_manager.followee_of(session['user_id']):
				vip_id.append(i.followee.id)
			posts = []
			vip_posts = []
			'''
			for post in post_manager.get_newsfeed(follow_list, start, end)
				if not post.is_secret or session['user_id'] in [post.user_id, post.wall_id] :
					posts.append(post)
			if end - start > len(posts) :
				no_more = True
			'''
			for i in Post.query.filter(Post.user_id.in_(vip_id)):
				if not i.is_secret or session['user_id'] in [i.user_id, i.wall_id]:
					posts.append(i)
			for i in Post.query.filter(Post.wall_id.in_(vip_id)):
				if i.is_secret==False or session['user_id'] in [i.user_id, i.wall_id]:
					posts.append(i)
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