from application import db
from schema import *
from user_manager import *

def add(body, user_id, post_id):
	db.session.add(Comment(
		user_id = user_id,
		post_id = post_id, 
		body = body
	))
	db.session.commit()

def read(comment_id):
	comment = Comment.query.get(comment_id)
	return {
		'id'		:comment.id,
		'body'		:comment.body, 
		'is_edited'	:comment.is_edited,
		'created_time':str(comment.created_time),
		'edited_time':str(comment.edited_time),
		'user_id'	:comment.user_id,
		'email'		:get_email(comment.user_id),
		'post_id'	:comment.post_id
	}

def remove_comment_mng(comment_id):
	comment = Comment.query.get(comment_id)
	db.session.delete(comment)
	db.session.commit()

def edit_comment_mng(data, comment_id):
	comment = Comment.query.get(comment_id)
	comment.body = data['comment_body']
	db.session.commit()