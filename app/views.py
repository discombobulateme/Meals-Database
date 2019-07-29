from flask import Flask, render_template, url_for, request
from app import app

import requests, json

@app.route('/')
def index():
	heading = "Frauenloop"
	subheading = "Meals DB Coding Challenge"
	return render_template('index.html', heading=heading, subheading=subheading, menu=navCategories())


def navCategories():
	heading = "Frauenloop"
	subheading = "Meals DB Coding Challenge"
	url = "https://www.themealdb.com/api/json/v1/1/categories.php"
	response = requests.request("GET", url)
	#return render_template('index.html', heading=heading, subheading=subheading, menu=response.json())
	return response.json()
