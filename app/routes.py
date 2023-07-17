#!/usr/bin/python3
from flask import render_template
from app import app

# @app.route('/')
@app.route('/index')
def index():
    user = {'username': "Sterling"}
    return render_template('index.html', title='Home', user=user)