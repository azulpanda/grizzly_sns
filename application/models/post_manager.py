from application import db
from schema import *

def add_post(data, user, wall):
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
	get_post = Post.query.get(post_id)
	post = {
	'id':get_post.id,
	'email':User.query.get(get_post.user_id).email, 
	'wall_email':User.query.get(get_post.wall_id).email,
	'body':get_post.body, 
	'is_edited':get_post.is_edited,
	'is_secret':get_post.is_secret,
	'created_time':str(get_post.created_time),
	'edited_time':str(get_post.edited_time),
	'user_id':get_post.user_id,
	'wall_id':get_post.wall_id
	}
	return post

def remove_post(post_id):
	post = Post.query.get(post_id)
	db.session.delete(post)
	db.session.commit()

def edit_post(data, post_id):
	post = Post.query.get(post_id)
	post.body = data['body']
	db.session.commit()
