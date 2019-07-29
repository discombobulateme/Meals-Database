from flask import Flask, render_template, url_for, request
from app import app

import requests, json

@app.route('/')
def index():
	heading = "Frauenloop"
	subheading = "Meals DB Coding Challenge"
	return render_template('index.html', heading=heading, subheading=subheading)

@app.route('/meal/<mealID>')
def randos(mealID):
    heading = "Meals"
    subheading = "Accessing the Random User API"
    url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=%s"%mealID
    response = requests.request("GET", url)
    return render_template('meal.html', heading=heading, subheading=subheading, food=response.json())