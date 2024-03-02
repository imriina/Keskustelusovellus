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
