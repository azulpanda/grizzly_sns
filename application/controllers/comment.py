from flask import render_template, session, redirect, request, url_for
from application import app
from application.models.schema import *
from application.models.post_manager import *
from application.models.comment_manager import *

@app.route('/', defaults={'post_id':0})
@app.route('/comment/<int:post_id>', methods=['POST'])
def comment(post_id):
	if 'logged_in' in session:
		if Post.query.get(post_id) != None:
			post = read_post(post_id)
			if post['is_secret']==False or session['user_id'] in [post['user_id'], post['wall_id']] :
				if request.method == 'POST':
					add_comment(request.form, session['user_id'], post_id)
				return redirect(url_for('post', post_id=post_id))
			else:
				return render_template('layout.html', error = 'No post')
		else:
			return render_template('layout.html', error = 'No post')
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/', defaults={'comment_id':0})
@app.route('/edit_comment/<int:comment_id>', methods=['GET', 'POST'])
def edit_comment(comment_id):
	if 'logged_in' in session:
		if Comment.query.get(comment_id) != None:
			comment=read_comment(comment_id)
			if session['user_id']==comment['user_id']:
				if request.method=='POST':
					edit_comment_mng(request.form, comment_id)
					return redirect(url_for('post', post_id=comment['post_id']))
				else:
					return render_template('edit_comment.html', comment=comment)
			else: 
				return render_template('layout.html', error = 'No authorization')
		else: 
			return render_template('layout.html', error = 'No comment')
	else:
		return render_template('layout.html', error = 'Log in')

@app.route('/', defaults={'comment_id':0})
@app.route('/remove_comment/<int:comment_id>', methods=['GET', 'POST'])
def remove_comment(comment_id):
	if 'logged_in' in session:
		if Comment.query.get(comment_id) != None:
			comment=read_comment(comment_id)
			if session['user_id']==comment['user_id']:
				remove_comment_mng(comment_id)
				return redirect(url_for('post', post_id=comment['post_id']))
		else: 
			return render_template('layout.html', error = 'No comment')
	else:
		return render_template('layout.html', error = 'Log in')