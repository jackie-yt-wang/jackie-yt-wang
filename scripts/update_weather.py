import requests
import json
from datetime import datetime,timezone
import datetime
import re
import os
import sys
import importlib
from emoji import emojize

BaseFolder = os.environ.get('BASE_FOLDER')
ScriptsFolder = os.environ.get('SCRIPTS_FOLDER')

# secrets_file = os.path.join(os.environ.get('SCRIPTS_FOLDER'), 'secrets.py')
# spec = importlib.util.spec_from_file_location('secrets', secrets_file)
# secrets = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(secrets)
# apikey = secrets.apikey
# lat = secrets.lat
# lon = secrets.long

apikey = os.environ['APIKEY']
lat = os.environ['LAT']
lon =os.environ['LONG']

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

output = f"<br/>Currently, the weather is: <b>{temperature}°C, <i>{weather_description}</i></b>{weather_emoji}</br>Today, the sun rises at <b>{sunrise}</b> and sets at <b>{sunset}</b>.</p>This <i>README</i> file was last refreshed on {current_time}.</p>"

# Read the content of your README file
with open(BaseFolder+'/README.md', 'r+') as file:
    content = file.read()
    file.seek(0)
    file.write(re.sub(r"<br\/>Currently,.*<\/p>", output, content))
    file.truncate()

