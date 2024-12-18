import json
from .models import Exercises
from django.conf import settings


def getExercises():
    # Load the JSON file
    with open("C:\Users\oviya\MyFitProject\exercises_list.json", 'r') as file:
        exercises = json.load(file)

    # Loop through each exercise in the JSON
    for exercise in exercises:
        Exercises.objects.create(
            name=exercise.get("name"),
            primary_muscle=exercise.get("primaryMuscles")[0],
            instructions=" ".join(exercise.get("instructions")),
            level=exercise.get("level")
        )

    print("Exercises imported successfully!")