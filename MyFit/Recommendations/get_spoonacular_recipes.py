import requests
from .models import Recipes
from django.conf import settings

# Spoonacular API key (ask chat if i keep this in settings.py how to reference it in this file)
API_KEY = '0fd59c8687a149f18a6cf5730d8966f2'
BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

def getRecipes():
    '''Gets recipes from Spoonacular API and uploads them to Recipe model.'''
    
    # Define parameters for the API call
    params = {
        'apiKey': API_KEY,
        'addRecipeInformation': True
    }

    # Make the API request
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        recipes = response.json().get('results', [])

        for recipe in recipes:

            # Extract relevant data
            name = recipe.get('title')
            vegetarian = recipe.get('vegetarian')
            ready_mins = recipe.get('readyInMinutes')
            link = recipe.get('sourceUrl')

            # Save to the database
            Recipes.objects.create(
                name=name,
                vegetarian=vegetarian,
                ready_mins=ready_mins,
                link=link
            )

        print("Recipes successfully added to the database.")
    else:
        print("Error fetching recipes:", response.status_code, response.text)
