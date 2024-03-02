import users, post, rooms
from sqlalchemy.sql import text
from db import db
from flask import session
from sqlalchemy.sql import text
from sqlalchemy import func

def create_comment(content, post_id):
	user_id_ad3 = users.get_user_id()
	if user_id_ad3 == 0:
		return False
	sql = """ INSERT INTO comments 	(post_id, maker_id, content, time)
			  VALUES 		   	(:post_id, :usr_id, :content, NOW())"""
	db.session.execute(text(sql), {'post_id': post_id, 'usr_id': user_id_ad3, 'content':content})
	db.session.commit()


def get_comments_by_post_id(post_id):
    sql = """ SELECT * FROM comments WHERE post_id =:post_id """
    result = db.session.execute(text(sql), {'post_id':post_id})
    comments = result.fetchall()
    return comments

def get_comment_by_id(comment_id):
	sql = """ SELECT * FROM comments WHERE comment_id =:id"""
	result = db.session.execute(text(sql), {'id': comment_id})
	comment = result.fetchone()
	return comment

def delete_comment(comment_id):
	sql = "DELETE FROM comments WHERE comment_id=:comment_id"
	db.session.execute(text(sql), {"comment_id":comment_id})
	db.session.commit()	
