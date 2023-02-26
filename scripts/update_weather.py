import requests
import json
from datetime import datetime,timezone
import datetime
import re
import os
import sys
import secrets
apikey = secrets.apikey
lat = secrets.lat
lon = secrets.long

# Define your location


# Call the OpenWeatherMap API to get the current weather data for your location
api_key = "16bbb6d5c78389fdcc7f64d8826e2c8d"
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={apikey}&units=imperial"
response = requests.get(url)
weather_data = json.loads(response.text)

# Get the temperature and weather description
temperature = weather_data['current']['temp']
weather_description = weather_data['current']['weather'][0]['description']

# Get the sunrise and sunset times
sunrise_timestamp = weather_data['current']['sunrise']
sunset_timestamp = weather_data['current']['sunset']

# Convert the sunrise and sunset times to your local timezone
sunrise = datetime.datetime.fromtimestamp(sunrise_timestamp).strftime("%H:%M")
sunset = datetime.datetime.fromtimestamp(sunset_timestamp).strftime("%H:%M")

# Format the output for your README
output = f"<br/>Currently, the weather is: <b>{temperature}°F, <i>{weather_description}</i></b></br>Today, the sun rises at <b>{sunrise}</b> and sets at <b>{sunset}</b>.</p>\n<h3>Where to find me</h3>"

# Write the output to your README file
readme_path = os.path.abspath("README.md")
with open(readme_path, "r+") as file:
    content = file.read()
    file.seek(0)
    file.write(re.sub(r"<br\/>Currently,.*<\/p>", output, content))
    file.truncate()
