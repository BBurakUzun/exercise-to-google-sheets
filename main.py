import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 76.5
HEIGHT_CM = 180
AGE = 20

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
AUTH = os.environ["AUTH"]

exercise_text = input("Tell me about your exercises")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
n_data = data["exercises"]

now = datetime.now()
date = now.date()
today = date.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

sheety_Headers = {
    "Content-Type": "application/json",
    "Authorization": AUTH
}

for exercise_data in n_data:
    new_row = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise_data["name"].title(),
            "duration": exercise_data["duration_min"],
            "calories": exercise_data["nf_calories"]
        }
    }
    sheety_endpoint = "https://api.sheety.co/0fa6ee57a44219b15bd22a782a3da5e2/egzersizlerim/workouts"
    response = requests.post(url=sheety_endpoint, json=new_row, headers=sheety_Headers)
    print(response.status_code)
    response.raise_for_status()
    print(response.text)
