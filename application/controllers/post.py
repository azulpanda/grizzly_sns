from flask import render_template, session, redirect, request, url_for
from application import app
from application.models.schema import *
from application.models.post_manager import *
from application.models.comment_manager import *

@app.route('/', defaults={'post_id':0})
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
	if 'logged_in' in session:
		if Post.query.get(post_id) != None:
			post = read_post(post_id)
			if session['user_id']==post['user_id']:
				if request.method=='POST':
					edit_post(request.form, post_id)
					return redirect(url_for('wall', wall_id=post['wall_id']))
				else:
					return render_template('edit.html', post=post)
			else: 
				return render_template('layout.html', error = 'No authorization')
		else: 
			return render_template('layout.html', error = 'No post')
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/', defaults={'post_id':0})
@app.route('/remove/<int:post_id>', methods=['GET', 'POST'])
def remove(post_id):
	if 'logged_in' in session:
		if Post.query.get(post_id) != None:
			post = read_post(post_id)
			if session['user_id']==post['user_id']:
				remove_post(post_id)
				return redirect(url_for('wall', wall_id=post['wall_id']))
		else: 
			return render_template('layout.html', error = 'No post')
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/', defaults={'post_id':0})
@app.route('/post/<int:post_id>')
def post(post_id):
	if 'logged_in' in session:
		if Post.query.get(post_id) != None:
			post = read_post(post_id)
			comments=[]
			raw_comments = Comment.query.filter(Comment.post_id == post_id).all()
			for i in raw_comments:
				comments.append(read_comment(i.id))
			ordered_comments = sorted(comments, key=lambda k: k['created_time']) 
			return render_template('post.html', post = post, ordered_comments = ordered_comments)
		else:
			return render_template('layout.html', error = 'No post')
	else:
		return render_template('layout.html', error = 'Log in')