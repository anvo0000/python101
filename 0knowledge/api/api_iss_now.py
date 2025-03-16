### API Code:
# 1xx: Hold on
# 2xx: Here you go, 200: connected and received responses successfully.
# 3xx: Go away, you don't have authorization to retrieve this data
# 4xx: You screwed up, now you need to find a way back, 404: not found
# 5xx: The website internally screwed up, 505: internal server error
from http.client import responses
# https://www.webfx.com/web-development/glossary/http-status-codes/


import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
response.raise_for_status()
if response.status_code == 200:
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    print(data)