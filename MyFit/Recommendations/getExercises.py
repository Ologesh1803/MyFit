import json
from .models import Exercises

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

# need to finish documentation of function, may need to change params
def getExercisesForUser(user_preferences):
    return Exercises.objects.filter(
        primary_muscle=user_preferences.get('primary_muscle'),
        level=user_preferences.get('level')
    )