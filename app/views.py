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
	return response.json()


@app.route('/categories/<categoriesID>')
def categories(categoriesID):
    heading = categoriesID
    subheading = "Many delicious meals"
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=%s" % categoriesID
    response = requests.request("GET", url)
    return render_template('categories.html', heading=heading, subheading=subheading, meal=response.json(),menu=navCategories())


@app.route('/meal/<mealID>')
def meals(mealID):
    heading = "Meals"
    subheading = "Accessing the Random User API"
    url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=%s"%mealID
    response = requests.request("GET", url)
    return render_template('meal.html', heading=heading, subheading=subheading, food=response.json(),menu=navCategories())