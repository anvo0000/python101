# If the ISS is close to my current position var= -5,+5 degrees.
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

import requests
from datetime import datetime

MY_LAT = 10.823099 # HCMC latitude
MY_LONG = 106.629662 # HCMC longitude
timezone = "Asia/Ho_Chi_Minh"
SUNRISE_SUNSET_URL = "https://api.sunrise-sunset.org/json"
ISS_URL = "http://api.open-notify.org/iss-now.json"

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": timezone
    }
    response = requests.get(SUNRISE_SUNSET_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    print(f"time_now:{time_now}\nSunrise: {sunrise}\nSunset: {sunset}")
    if sunrise <= time_now <= sunset:
        return False # Daytime
    else:
        return True # Nighttime

# print(is_night_time())

def is_iss_overhead():
    response = requests.get(url=ISS_URL)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if ((MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and
        (MY_LONG-5 <= iss_longitude <= MY_LONG + 5)):
        return True

if is_iss_overhead() and is_night_time():
    print("Look ISS is above you!")
else:
    print("Check your email regularly to have a chance looking at the ISS by your bare eyes.")





