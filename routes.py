from flask import render_template, request, redirect, session
from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash


app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

app.secret_key = getenv("SECRET_KEY")

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
            return redirect("register")
        sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :is_admin);"
        db.session.execute(text(sql), {'username':username, 'password':password1, 'is_admin': role})
        db.session.commit()
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]   
        session["username"] = username    
        return redirect("/")
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
