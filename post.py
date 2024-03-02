import users, rooms
from sqlalchemy.sql import text
from db import db
from flask import session, request
from sqlalchemy.sql import text
from sqlalchemy import func


def create_post(header, content, room_id):
	user_id_ad3 = users.get_user_id()
	if user_id_ad3 == 0:
		return False
	sql = """ INSERT INTO post 	(room_id, maker_id, header, content, time)
			  VALUES 		   	(:room_id, :usr_id, :header, :content, NOW())"""
	db.session.execute(text(sql), {'room_id': room_id, 'usr_id': user_id_ad3, 'header': header, 'content':content})
	db.session.commit()

def get_posts_by_room_id(room_id):
	sql = """ SELECT * FROM post WHERE room_id =:room_id """
	result = db.session.execute(text(sql), {'room_id':room_id})
	posts = result.fetchall()
	return posts

def get_post_by_id(post_id):
	sql = """ SELECT * FROM post WHERE post_id =:id"""
	result = db.session.execute(text(sql), {'id': post_id})
	post = result.fetchone()
	return post

def delete_post(post_id):
	sql = "DELETE FROM post WHERE post_id=:post_id"
	db.session.execute(text(sql), {"post_id":post_id})
	db.session.commit()

def search(key):
	sql = """ SELECT DISTINCT * FROM post WHERE (post.content LIKE :key OR post.header LIKE :key)"""
	result = db.session.execute(text(sql), {'key': '%'+key+'%'})
	posts = result.fetchall()
	return posts

def add_post_to_saved(post_id):
	user_id_ad3 = users.get_user_id()
	if user_id_ad3 == 0:
		return False
	sql = """INSERT INTO savedposts (post_id, user_id)
		   VALUES                   (:post_id, :user_id)"""
	db.session.execute(text(sql), {'post_id':post_id, 'user_id':user_id_ad3})
	db.session.commit()

def remove_from_saved(post_id):
	user_id_ad3 = users.get_user_id()
	if user_id_ad3 == 0:
		return False
	sql = """DELETE FROM savedposts WHERE user_id = :user_id AND post_id=:post_id """
	db.session.execute(text(sql), {'user_id':user_id_ad3, 'post_id':post_id})
	db.session.commit()

def get_saved_posts():
	user_id_ad3 = users.get_user_id()
	if user_id_ad3 == 0:
		return False
	sql = """ SELECT * FROM savedposts JOIN post ON post.post_id = savedposts.post_id WHERE savedposts.user_id =:user_id"""
	result = db.session.execute(text(sql), {'user_id':user_id_ad3})
	content = result.fetchall()
	return content