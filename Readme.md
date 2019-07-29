# The Meals Databse

This a student project is based on Flask, Bootstrap and [TheMealDB](https://www.themealdb.com/) api. The base code that is in the repo should be pretty self explaniatory at this stage :) 



### Clone the repository 

Take a copy of the code on to your own computer

```
git clone https://github.com/FrauenLoop-Berlin/Meals-Database.git
```

### Create virtualenv
As this is a new project you will need to create a virtual environment inside the Meals-Database folder. Will use the latest version of python3 that is installed on your computer
```
virtualenv -p python3 venv
```

### Create a branch
You should create a branch to code a new feature using the command below

```
git checkout -b feature-name
```



### Code your changes
Write your code and test it locally. Once you are happy with the changes commit. 




### Commit and push your branch
```
git add . 
git commit -m "Some message about what you changed"
git push
```
The first time that you commit to your branch you are likely to hit an error as the git server doesn't know your branch exists. Read through the error you from git and it should give you some suggestions on how to solve this. 

### Merging the code
This part is handled by the repository administrator. 


# API

Documentation on the API can be found at [TheMealDB](https://www.themealdb.com/) 

### Categories 
This gives you all the available categories
(https://www.themealdb.com/api/json/v1/1/categories.php)

### Meals by category
This shows all the meals available by category.
(https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood)

### Specific Meals
Each meal has an ID and you can query the API to get a specific meal by the ID
(https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772)