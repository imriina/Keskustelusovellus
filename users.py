from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from db import db
from flask import session
from os import getenv, urandom
import secrets


def register(username, password, role):
	hash_value = generate_password_hash(password)
	sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :is_admin);"
	db.session.execute(text(sql), {'username':username, 'password':hash_value, 'is_admin': role})
	db.session.commit()
	return login(username, password)

def login(username, password):
	sql = text("SELECT password, id, admin FROM users WHERE username=:username")
	returning = db.session.execute(sql, {"username":username})
	user = returning.fetchone()
	if not user:
		return False
	if not check_password_hash(user[0], password):
		return "wrong_password"
	session["id"] = user[1]
	session["username"] = username
	session["admin"] = user[2]
	session["csrf_token"] = secrets.token_hex(16)
	return True

def get_user_id():
    return session.get("id", 0)


def logout():
	del session["id"]
	del session["username"]
	del session["admin"]
	return True
