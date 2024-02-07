from flask import render_template, request, redirect, session
from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
import users, rooms
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

@app.route("/")
def index():
    list = rooms.get_list()
    return render_template("index.html", count=len(list), rooms=list)


@app.route("/register", methods=["GET", "POST"])
def register():  
    if request.method == "GET":      
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        role = request.form["role"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if not users.register(username, password1,role):
            return render_template("register.html")
        session["username"] = username
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("login.html")   
        return redirect("/")

@app.route("/createroom", methods=["POST"])
def createTopic():
    room = request.form["room"]
    rooms.createroom(room)
    return redirect("/")

@app.route("/createpost", methods=["POST"])
def createpost():
    post = request.form["room"]
    post.createpost(post)
    return redirect("/")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/messages")
def messages():
    return render_template("messages.html") 

@app.route("/delete_room", methods=['POST'])
def delete_room():
    room_name = request.form.get("room_name")
    room_id = rooms.get_room_id(room_name)
    rooms.delete_room(room_id)
    return redirect("/")


