from flask import Flask, render_template, url_for, request
from app import app

import requests, json

@app.route('/')
def index():
	heading = "Frauenloop"
	subheading = "Meals DB Coding Challenge"
	return render_template('index.html', heading=heading, subheading=subheading)