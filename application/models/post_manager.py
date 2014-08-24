from application import db
from schema import *

def add(data, user, wall):
	secret = 0
	if 'secret' in data:
		secret = '1'
	post = Post(
		user_id = user, 
		wall_id = wall, 
		body = data['body'], 
		is_secret = secret
	)
	db.session.add(post)
	db.session.commit()

def read_post(post_id):
	post = Post.query.get(post_id)
	return {
		'id'		:post.id,
		'email'		:post.user.email, 
		'wall_email':post.wall.email,
		'body'		:post.body, 
		'is_edited'	:post.is_edited,
		'is_secret'	:post.is_secret,
		'created_time':str(post.created_time),
		'edited_time':str(post.edited_time),
		'user_id'	:post.user_id,
		'wall_id'	:post.wall_id
	}

def remove_post(post_id):
	post = Post.query.get(post_id)
	db.session.delete(post)
	db.session.commit()

def edit_post(data, post_id):
	post = Post.query.get(post_id)
	post.body = data['body']
	db.session.commit()
