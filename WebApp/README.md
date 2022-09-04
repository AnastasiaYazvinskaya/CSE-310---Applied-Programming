# Overview

DietCreation is a web application where anyone can easily share their recipes and create customized menus for themselves and their families.
The test server can be launched via the command line by navigating to the location of the application's main folder and running the command "python manage.py runserver" and open "http://127.0.0.1:8000/dietCreation/" page.

The purpose of this application is for the user to store and share recipes, as well as create a menu for himself for a different period, so that he will be able to know what and how many products he needs to buy. Also give the opportunity to save the products that the user most often uses for cooking and using this list to simplify the purchase of products.

[DietCreation Web App (Demo Video)](https://youtu.be/flPvAKhSEWs)

# Web Pages

* Home page:
    Have links for three main sections of the app: Products (not availiable now), Recipes, Menu (not availiable now); with a little description of the purpose of each of them. (You can return to this page from any page of the application using the navigation block or by clicking on the name in the header.)

* Recipes page:
    Display a full list of recipes with its name, type and list of ingredients which are taken from the database. Each recipe has delete and edit buttons. At the top of the list placed button for adding new recipe. If there are no recipes in the database, the user will be notified and a button to add a recipe will be shown. (You can return to this page from any page of the application using the navigation block.)

* Recipe page:
    Display full information about a specific recipe which is taken from the database.(You can access this page only from the page of the main list of recipes by clicking on any of the displayed recipes.)
    
* Create recipe page:
    This page contains a form to fill in information about the recipe. As a standard, she suggests adding: name, type, one ingredient, one cooking step of the recipe and mark the possibility to make it an ingredient for other recipes. If the recipe contains more than one ingredient or cooking step, then you must click on the corresponding button and an additional field will be added. After the form is completed and the user has clicked on the save recipe button, the user will be taken to a page with an updated list of recipes. (You can access this page only from the page of the main list of recipes by clicking on plus button at the top of list or if list is empty by "Create recipe" button.)

# Development Environment

The tools that I used to develop software are VSCode and the corresponding extensions for working with the python language. I also actively used Git and its version control system.

This Web App was written in Python programming language using Django framework as a backend and HTML, CSS/Bootstrap and JavaScript/JQuery as frontend.

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/4.0/)
* [Django Tutorial](https://www.w3schools.com/django/index.php)
* [JQuery Tutorial](https://www.w3schools.com/jquery/default.asp)
* [Bootstrap 4 Tutorial](https://www.w3schools.com/bootstrap4/default.asp)

# Future Work

* Create a page to edit recipe data.

* Create 4 pages for products (list, create, edit, view a single product) that the user buys from the store and uses in recipes. (Similar to recipes)

* Create 4 pages for the menu (list of different menus, create a new one, change, view a separate menu), which the user will compile according to the available recipes.

* Add users so that all actions are available only to authorized users, except for viewing recipes.
