from sqlalchemy.sql import text
from db import db
from flask import session
from os import getenv, urandom
import secrets
from werkzeug.security import generate_password_hash, check_password_hash


def validate_password(password):
    if len(password) < 8 or len(password) > 20:
        return False
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_letter and has_digit


def register(username, password, role):
    if not validate_password(password):
        return "invalid_password"
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :is_admin);"
    db.session.execute(text(sql), {'username':username, 'password':password_hash, 'is_admin': role})
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
