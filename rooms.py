import users
from sqlalchemy.sql import text
from db import db
from flask import session
from sqlalchemy.sql import text
from sqlalchemy import func

def get_list():
    sql = text("SELECT rooms.topic, users.username, rooms.sent_at FROM rooms JOIN users ON rooms.user_id = users.id ORDER BY rooms.room_id;")
    result = db.session.execute(sql)
    return result.fetchall()	

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