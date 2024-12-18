import json
from .models import Exercises
from django.conf import settings


def getExercisesForModel(file_path):
    '''
    Gets exercises from a JSON file and uplaods them to Exercises model.
    
    params:
    file_path: Path to the JSON file that has all the exercies
    '''
    # Load the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        exercises = data['exercises']

    # Loop through each exercise
    for exercise in exercises:
        Exercises.objects.create(
            name=exercise['name'],
            primary_muscle=exercise['primaryMuscles'][0],
            instructions=" ".join(exercise['instructions']),
            level=exercise['level']
        )

    print("Exercises imported successfully!!!")