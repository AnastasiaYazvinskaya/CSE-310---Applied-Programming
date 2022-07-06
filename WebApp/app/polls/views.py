from django.shortcuts import render, redirect

from django.http import HttpResponse, request
from flask import request
from .models import Recipes, Ingredients, Products

from datetime import datetime
from werkzeug.exceptions import BadRequest, InternalServerError, abort

# Create your views here.
def index(request):
    return render(request, "polls/index.html")

# Recipes page
def recipes(request):
    recipes = Recipes.objects.all()
    ingredients = Ingredients.objects.all().prefetch_related('product_id')

    return render(request, 'polls/recipes.html', {'recipes': recipes, 'ingredients': ingredients})#, 'products': products})

# Recipe page
def recipe(request, id=None):
    if id:
        recipe = Recipes.objects.get(id=id)
        recipe.description = recipe.description.split('endofstep')
        ingredients = Ingredients.objects.filter(recipe_id=id).prefetch_related('product_id')

        return render(request, 'polls/recipe.html', {'recipe': recipe, 'ingredients': ingredients})
    return redirect('/dietCreation/recipes/')

# Create recipe page
def createRecipe(request):
    recipe = RecipeAct()
    if recipe.act(request, recipe.create):
        return redirect('/dietCreation/recipes/')
    return render(request, "polls/createRecipe.html", {'recipe': recipe})

# Delete recipe
def deleteRecipe(request, id=None):
    if id:
        Recipes.objects.get(id=id).delete()
    
    return redirect('/dietCreation/recipes/')

class Recipe:
    def __init__(self, id=None):
        self.id = id
        if self.id:
            self.recipe = Recipes.objects.get(id = self.id)
            self.ingredients = Ingredients.objects.get(recipe_id = self.id)
        else:
            self.recipe = Recipes()
            self.ingredients = []

    def set_data(self, name, type, ingredients, description, as_product):
        self.recipe.name = name
        if type:
            self.recipe.type = type
        else:
            self.recipe.type = "General"
        self.recipe.description = description
        #self.recipe.as_product = as_product
        self.recipe.created = datetime.date(datetime.now())
        self.recipe.save()
        for i in range(len(ingredients['name'])):
            prod_exist = Products.objects.filter(name = ingredients['name'][i])
            if not prod_exist:
                product = Products()
                product.name = ingredients['name'][i]
                product.created = datetime.date(datetime.now())
                product.save()
            prod_id = Products.objects.get(name=ingredients['name'][i])
            recipe_id = Recipes.objects.get(id=self.recipe.id)
            ingredient = Ingredients(recipe_id=recipe_id, product_id=prod_id, weight=ingredients['weight'][i], weight_type=ingredients['weight_type'][i])
            ingredient.save()
            self.ingredients.append(ingredient)
    
    def create(self):
        return True

    def edit(self):
        return True
        
    def check_if_exist(self, recipe_name, description, as_product):
        exist = Recipes.objects.filter(name=recipe_name, description=description)
        return exist

# Work with recipes (create, edit, delete)
class RecipeAct:
    def __init__(self, recipe_id=None):
        self.recipe = Recipe(recipe_id)
    def act(self, request, func):
        # Form handling
        if request.method == 'POST':
            recipe_name = request.POST.get('r_name')
            dish_type = request.POST.get('dishtype')
            ingredients = {
                'name':[],
                'weight':[],
                'weight_type':[]
            }
            for i in range(0,30):
                try:
                    name = "name_"+str(i)
                    weight = "weight_"+str(i)
                    weight_type = "weight-type_"+str(i)
                    # If name was filled in, then save this ingredient
                    if request.POST.get(name) and request.POST.get(weight) and request.POST.get(weight_type):
                        ingredients['name'].append(request.POST.get(name).lower())
                        ingredients['weight'].append(request.POST.get(weight))
                        ingredients['weight_type'].append(request.POST.get(weight_type))
                except BadRequest:
                    pass
            description = ""
            for i in range(0,30):
                try:
                    step = "step_"+str(i)
                    if request.POST.get(step):
                        description += request.POST.get(step)
                        step = "step_"+str(i+1)
                        if i != 29 and request.POST.get(step):
                            description += "endofstep"
                except BadRequest:
                    pass
            if request.POST.get('recipe_as_product'):
                as_product = int(request.POST.get('recipe_as_product'))
            else:
                as_product = 0

            if recipe_name and ingredients['name'] and description:
                if not self.recipe.check_if_exist(recipe_name, description, as_product) or self.recipe.id:
                    dish_type = request.POST.get('dishtype').lower()
                    self.recipe.set_data(recipe_name, dish_type, ingredients, description, as_product)
                    return func()
        return False
            
    def create(self):
        self.recipe.create()  
        return True
    def edit(self):
        self.recipe.edit()  
        return True