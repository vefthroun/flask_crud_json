from app import app
from http import client
from flask import Flask, render_template, request, redirect, url_for
import json


@app.route("/test")
def test():
    return render_template("htmx.html")

@app.route("/users")
def users():

    f = open("data/clients.json", "r")
    clients_str = f.read()
    all_clients = json.loads(clients_str)     

    return render_template("clients.html", clients=all_clients)
