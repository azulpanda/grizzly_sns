from application import db
from schema import *

def add_follow(follower, followee):
	follow = Follow(
		follower_id = follower,
		followee_id = followee
		)
	if Follow.query.filter(Follow.follower_id == follower, Follow.followee_id == followee).count() == 0:
		db.session.add(follow)
		db.session.commit()

def get_follower(id):
	return Follow.query.filter(Follow.followee_id == id).all()

def get_followee(id):
	return Follow.query.filter(Follow.follower_id == id).all()
