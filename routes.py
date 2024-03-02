from flask import render_template, request, redirect, session
from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
import users, rooms, post, comment
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
    header = request.form["header"]
    content = request.form["content"]
    post.create_post(header, content)
    return redirect("/")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/messages/<room_id>", methods=["GET", "POST"])
def messages(room_id):
    if request.method == "GET":
        topic = rooms.get_room_by_id(room_id)
        posts = post.get_posts_by_room_id(room_id)
        return render_template("messages.html", topic=topic, posts=posts)
    if request.method == "POST":
        header = request.form["header"]
        content = request.form["content"]
        post.create_post(header, content, room_id)
        return redirect(f"/messages/{room_id}")

@app.route("/delete_room", methods=['POST'])
def delete_room():
    room_name = request.form.get("room_name")
    room_id = rooms.get_room_id(room_name)
    rooms.delete_room(room_id)
    return redirect("/")

@app.route("/delete_post", methods=['POST'])
def delete_post():
    post_id = request.form.get("post")
    post2 = post.get_post_by_id(post_id)
    room_id = post2.room_id
    post.delete_post(post_id)
    return redirect(f"/messages/{room_id}")

@app.route("/post/<post_id>", methods=["GET", "POST"])
def post_page(post_id):
    if request.method == "GET":
        post2 = post.get_post_by_id(post_id)
        comments = comment.get_comments_by_post_id(post_id)
        return render_template("post.html", post=post2, comments=comments)
    if request.method == "POST":
        content = request.form["content"]
        comment.create_comment(content, post_id)
        return redirect(f"/post/{post_id}")


@app.route("/delete_comment", methods=['POST'])
def delete_comment():
    comment_id = request.form.get("comment")
    comment2 = comment.get_comment_by_id(comment_id)
    post_id = comment2.post_id
    comment.delete_comment(comment_id)
    return redirect(f"/post/{post_id}")

@app.route("/search", methods=['POST'])
def search():
    key = request.form["key"]
    content = post.search(key)
    return render_template("search_results.html", posts=content, key=key)

@app.route("/savedposts", methods=['GET'])
def savedposts():
    if request.method == "GET":
        content = post.get_saved_posts()
        return render_template("savedposts.html", posts=content)

@app.route("/add_post_to_saved", methods=["GET", "POST"])
def add_post_to_saved():
    post_id = request.form["post"]
    post.add_post_to_saved(post_id)
    post2 = post.get_post_by_id(post_id)
    room_id = post2.room_id
    return redirect(f"/messages/{room_id}")

@app.route("/remove_from_saved", methods=['POST'])
def remove_from_saved():
    post_id = request.form["post"]
    post.remove_from_saved(post_id)
    return redirect("/savedposts")