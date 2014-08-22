from application import db
from schema import *
from user_manager import *

def add_comment(data, user, post):
	comment = Comment(
		user_id = user, 
		post_id = post, 
		body = data['comment_body']
	)
	db.session.add(comment)
	db.session.commit()

def read_comment(comment_id):
	get_comment = Comment.query.get(comment_id)
	comment = {
	'id':get_comment.id,
	'body':get_comment.body, 
	'is_edited':get_comment.is_edited,
	'created_time':str(get_comment.created_time),
	'edited_time':str(get_comment.edited_time),
	'user_id':get_comment.user_id,
	'email':get_email(get_comment.user_id),
	'post_id':get_comment.post_id
	}
	return comment

def remove_comment_mng(comment_id):
	comment = Comment.query.get(comment_id)
	db.session.delete(comment)
	db.session.commit()

def edit_comment_mng(data, comment_id):
	comment = Comment.query.get(comment_id)
	comment.body = data['comment_body']
	db.session.commit()