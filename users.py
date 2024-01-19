from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from db import db


def register(username, password, role):
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :is_admin);"
    db.session.execute(text(sql), {'username':username, 'password':hash_value, 'is_admin': role})
    db.session.commit()
    return True
    