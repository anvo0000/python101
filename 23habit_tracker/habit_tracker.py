# https://docs.pixe.la/
import os
import dotenv
import requests
from datetime import datetime

dotenv.load_dotenv()
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
graphid = f"graphs{PIXELA_USERNAME}" #graphsanvo0000


#---STEP 1: Create a User anvo0000
user_param = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_param)
# print(response.text)
## {"message":"Success. Let's visit https://pixe.la/@anvo0000 , it is your profile page!","isSuccess":true}

#---STEP2: Create a Graph graphsanvo0000
# https://docs.pixe.la/entry/post-graph
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
graph_config = {
    "id" : graphid,
    "name": "Outdoor Run Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora" #blue
}

# response = requests.post(url=PIXELA_GRAPH_ENDPOINT,
#                          json=graph_config,
#                          headers=headers)
# print(response.text) ## https://pixe.la/v1/users/anvo0000/graphs/graphsanvo0000.html


#---STEP 3: Post/Create a pixel to Habit Graph graphsanvo0000
# https://www.w3schools.com/python/python_datetime.asp
pixel_date = datetime(year=2025, month=3, day=16).strftime("%Y%m%d") #20250322
print(pixel_date)

PIXELA_GRAPH_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graphid}"
print(PIXELA_GRAPH_PIXEL_ENDPOINT)
pixel_config = {
    "date": pixel_date,
    "quantity": "0.9"
}
# response = requests.post(url=PIXELA_GRAPH_PIXEL_ENDPOINT,
#                          json=pixel_config,
#                          headers=headers)
# print(response.text)

#---STEP 4: Update a pixel to Habit Graph graphsanvo0000 20250316
pixel_date = datetime(year=2025, month=3, day=16).strftime("%Y%m%d") #20250322
PIXELA_GRAPH_PIXEL_DATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graphid}/{pixel_date}"
pixel_put_config = {
    "quantity": "90"
}
# response = requests.put(PIXELA_GRAPH_PIXEL_DATE_ENDPOINT, json=pixel_put_config, headers=headers)
# print(response.text)

#---STEP 5: Update a pixel to Habit Graph graphsanvo0000 20250316
pixel_date = datetime(year=2025, month=3, day=16).strftime("%Y%m%d") #20250322
PIXELA_GRAPH_PIXEL_DATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graphid}/{pixel_date}"
response = requests.delete(PIXELA_GRAPH_PIXEL_DATE_ENDPOINT, headers=headers)
print(response.text)

