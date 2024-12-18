import requests
from .models import Recipes
from django.conf import settings

# Spoonacular API key (ask chat if i keep this in settings.py how to reference it in this file)
API_KEY = settings.SPOONACULAR_API_KEY
BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

def getRecipesForModel():
    '''
    Gets recipes from Spoonacular API and uploads them to Recipes model.
    '''
    
    # Define parameters for the API call
    API_calls = 0
    total_results = 1
    offset = 0
    number = 100

    while ((API_calls < 151) or (offset < total_results)):
        params = {
            'apiKey': API_KEY,
            'addRecipeInformation': True,
            'number': number,
            'offset': offset

        }

        # Make the API request
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            total_results = results.get('total_results')
            recipes = results.get('results')

            for recipe in recipes:
                # Extract relevant data and save to the database
                Recipes.objects.create(
                    name=recipe.get('title'),
                    vegetarian=recipe.get('vegetarian'),
                    ready_mins=recipe.get('readyInMinutes'),
                    link=recipe.get('sourceUrl')
                )
            offset += number
            print(f"Fetched {len(recipes)} recipes. Total fetched so far: {offset}")
        else:
            print("Error fetching recipes:", response.status_code, response.text)
            break
    
    print("Recipes successfully added to the database.")
