import users, post
from sqlalchemy.sql import text
from db import db
from flask import session
from sqlalchemy.sql import text
from sqlalchemy import func
import secrets

def get_list():
	session["csrf_token"] = secrets.token_hex(16)
	sql = text("SELECT rooms.topic, users.username, rooms.sent_at, rooms.room_id FROM rooms JOIN users ON rooms.user_id = users.id ORDER BY rooms.room_id;")
	result = db.session.execute(sql)
	return result.fetchall()	

def get_room_id(topic):
	sql = db.session.execute(text("SELECT room_id FROM rooms WHERE topic=:topic"), {"topic": topic})
	room = sql.fetchone()
	return room[0] if room else None

def get_room_by_id(topic_id):
	sql = """ SELECT * FROM rooms WHERE room_id =:id"""
	result = db.session.execute(text(sql), {'id': topic_id})
	topic = result.fetchone()
	return topic

def createroom(topic):
	user_id_ad = users.get_user_id()
	if user_id_ad == 0:
		return False
	sql = "INSERT INTO rooms (topic, user_id, sent_at) VALUES (:topic, :user_id, NOW());"
	db.session.execute(text(sql), {"topic":topic, "user_id":user_id_ad})
	db.session.commit()
	return True

def show_rooms():
	sql = "SELECT name FROM rooms ORDER BY name"
	return db.session.execute(text(sql)).fetchall

def delete_room(room_id):
	sql = "DELETE FROM rooms WHERE room_id=:room_id"
	db.session.execute(text(sql), {"room_id":room_id})
	db.session.commit()

def create_post_helper(maker_id,room_id, header, content):
	sql = "INSERT INTO post (room_id, maker_id, header, content, time) VALUES (:post_id, :room_id, :maker_id, :header, :content, NOW());"
	db.session.execute(text(sql), {"room_id": room_id, "maker_id": maker_id, "header": header, "content": content})
	db.session.commit()
