from flask import render_template, request, redirect, session
from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
import users
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

@app.route("/")
def index():
    return render_template("index.html")


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
    users.createroom(room)
    return redirect("/")
    
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

