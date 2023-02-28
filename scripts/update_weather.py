import requests
import json
from datetime import datetime,timezone
import datetime
import re
import os
import sys
import importlib
from emoji import emojize
from github import Github

# g = Github(os.environ['TOKEN'])
# repo = g.get_repo('jackie-yt-wang/secrets')
# content = repo.get_contents("weather-api.txt")
# apikey = content.decoded_content.decode('utf-8').strip('\n')

apikey = os.environ['APIKEY']
BaseFolder = os.environ.get('BASE_FOLDER')
ScriptsFolder = os.environ.get('SCRIPTS_FOLDER')
lat ='44.9670'
lon = '-93.193816'

# Call the OpenWeatherMap API to get the current weather data for your location
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
current_time = datetime.datetime.now().strftime("%A, %d %B, %H:%M %Z")

# Define the weather emoji based on the weather description
if "cloud" in weather_description:
    weather_emoji = emojize(":cloud:")
elif "sun" in weather_description or "clear" in weather_description:
    weather_emoji = emojize(":sunny:")
elif "rain" in weather_description:
    weather_emoji = emojize(":rain_cloud:")
elif 'snow' in weather_description:
    weather_emoji = emojize(':snowflake:')
else:
    weather_emoji = ""

output = f"<br/>Currently, the weather in St Paul, MN is: <b>{temperature}°F, <i>{weather_description}</i></b>{weather_emoji}</br>Today, the sun rises at <b>{sunrise}</b> and sets at <b>{sunset}</b>.</p>This <i>README</i> file was last refreshed on {current_time}.</p>"

# Read the content of your README file
with open(BaseFolder+'/README.md', 'r+') as file:
    content = file.read()
    file.seek(0)
    file.write(re.sub(r"<br\/>Currently,.*<\/p>", output, content))
    file.truncate()

