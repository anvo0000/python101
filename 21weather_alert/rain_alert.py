import json
import  requests
import os
import dotenv
dotenv.load_dotenv()
MY_LAT = 10.823099 # HCMC latitude
MY_LONG = 106.629662 # HCMC longitude

FORECAST_API = os.getenv("FORECAST_API")
FORECAST_URL = os.getenv("FORECAST_URL")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": FORECAST_API,
    "cnt": 4
}



# Weather Forecast

response_forecast = requests.get(url=FORECAST_URL, params=parameters)
print(response_forecast.request.url)
response_forecast.raise_for_status()
weather_data = response_forecast.json()

print(weather_data)# <class 'dict'>

# get weathers
will_rain = False
list_wt = weather_data.get("list")
for item in list_wt:
    weather = item.get("weather")
    # print(weather[0]["id"])
    condition_code = weather[0]["id"]
    if condition_code < 800:
        will_rain = True

if will_rain:
    print("Bring umbrella")

