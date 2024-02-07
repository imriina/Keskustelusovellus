import users, rooms
from sqlalchemy.sql import text
from db import db
from flask import session
from sqlalchemy.sql import text
from sqlalchemy import func


def createpost(header, content):
	user_id_ad = users.get_user_id()
	if user_id_ad == 0:
		return False
	sql = "INSERT INTO rooms (topic, user_id, sent_at) VALUES (:topic, :user_id, NOW());"
	db.session.execute(text(sql), {"topic":topic, "user_id":user_id_ad})
	db.session.commit()
	return True