# Ref: https://docx.syndigo.com/developers/docs/nutritionix-api-guide
# https://docx.syndigo.com/developers/docs/natural-language-for-exercise
import requests
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

WEIGHT_KG = 50
HEIGHT_CM = 150
AGE = 38

endpoint = os.getenv("NUTRITIONIX_ENDPOINT")
app_id = os.getenv("NUTRITIONIX_APP_ID")
api_key = os.getenv("NUTRITIONIX_API_KEY")

headers = {
    'x-app-id': app_id,
    'x-app-key': api_key
  }
# exercise_query = input("Tell me exercise you did: ")
exercise_query = "run 2km"

parameters = {
    "query": exercise_query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
# exercises = requests.post(url=endpoint, headers=headers, json=parameters)
# print(exercises.text)

#----OFFLINE MODE ----#
import exercise_data
print(exercise_query)
exercises = exercise_data.data["exercises"]
print("OFFLINE MODE\n", exercises)
#----OFFLINE MODE ----#

# Expected Result
# Date	        Time	    Exercise	Duration	Calories
# 21/07/2020	15:00:00	Running	    22	        130
csv_file = 'exercise_log.csv'
df = []
row = {}
today = datetime.now()
exercise_date = today.strftime("%d/%m/%Y")
exercise_time = today.strftime("%H:%M:%S")
print(exercise_date, exercise_time)
for item in exercises:
    row["date"] = exercise_date
    row["time"] = exercise_time
    row["exercise"] = item["name"].title()
    row["duration"] = item["duration_min"]
    row["calories"] = item["nf_calories"]
    df = pd.DataFrame([row])

df.to_csv(csv_file, mode="a",index=False,header=False)





