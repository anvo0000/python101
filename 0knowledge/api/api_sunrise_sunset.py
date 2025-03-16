# Note that unless you provide a tzid, all times are in UTC
# https://sunrise-sunset.org/api
# https://www.latlong.net/
# https://www.php.net/manual/en/timezones.asia.php

from datetime import datetime
import requests
URL = "https://api.sunrise-sunset.org/json"
param = {
    "lat": 10.823099,
    "lng": 106.629662,
    "formatted": 0, # get the 24hr format
    "tzid": "Asia/Ho_Chi_Minh"
}

response = requests.get(url=URL, params=param)
response.raise_for_status()
data = response.json()

# get the sunrise's hour
# sunrise_list = sunrise.split("T") # ['2025-03-14', '06:00:02+07:00']
# sunrise_list = sunrise.split("T")[1] # 06:00:02+07:00
# sunrise_list = sunrise.split("T")[1].split(":") #['06', '00', '02+07', '00']
# sunrise_hour = sunrise.split("T")[1].split(":")[0] #06 -> get the sunrise's hour


sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

#now
time_now = datetime.now().hour
print(time_now)

