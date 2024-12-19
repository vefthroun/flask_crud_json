from app import app
from http import client
from flask import Flask, render_template, request, redirect, url_for
import json

# má ekki vera í gagni hér > app = Flask(__name__)

@app.route("/test")
def test():

    return render_template("htmx.html")

@app.route("/users")
def users():
    return "Users"
    #return render_template("users.html")

