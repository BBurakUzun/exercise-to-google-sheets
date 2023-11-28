import requests

GENDER = "male"
WEIGHT_KG = 76.5
HEIGHT_CM = 180
AGE = 20

APP_ID = "7018089b"
API_KEY = "9f698d5c37f63afc4208704f054e3aeb"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


exercise_text = input("Tell me about your exercises")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
print(response.text)