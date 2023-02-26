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
BaseFolder = os.environ.get('BASE_FOLDER')

# Call the OpenWeatherMap API to get the current weather data for your location
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={apikey}&units=imperial"
response = requests.get(url)
weather_data = json.loads(response.text)

# Get the temperature and weather description
temperature = weather_data['current']['temp']
weather_description = weather_data['current']['weather'][0]['description']
city = weather_data['name']
state = weather_data['sys']['country']

# Get the sunrise and sunset times
sunrise_timestamp = weather_data['current']['sunrise']
sunset_timestamp = weather_data['current']['sunset']

# Convert the sunrise and sunset times to your local timezone
sunrise = datetime.datetime.fromtimestamp(sunrise_timestamp).strftime("%H:%M")
sunset = datetime.datetime.fromtimestamp(sunset_timestamp).strftime("%H:%M")

# Format the output for your README
output = f"<br/>Currently, the weather is: <b>{temperature}°F, <i>{weather_description}</i></b></br>Today, the sun rises at <b>{sunrise}</b> and sets at <b>{sunset}</b>.</p>\n<h3>Where to find me</h3>"

# Write the output to your README file
with open(BaseFolder+'/README.md', "r+") as file:
    content = file.read()
    file.seek(0)
    file.write(re.sub(r"<br\/>Currently,.*<\/p>", output, content))
    file.truncate()
