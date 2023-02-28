import requests
import json
from datetime import datetime,timezone
import datetime
import re
import os
from emoji import emojize

apikey = os.environ['APIKEY']
BaseFolder = os.environ.get('BASE_FOLDER')
ScriptsFolder = os.environ.get('SCRIPTS_FOLDER')
lat ='44.9670'
lon = '-93.193816'
lat_la = '34.0689'
lon_la = '-118.4452'

def weather_ouput(lat, lon,apikey):
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
    # Return the temperature, weather description, weather emoji, sunrise, and sunset
    return temperature, weather_description, weather_emoji, sunrise, sunset

temperature,weather_description,weather_emoji,sunrise,sunset = weather_ouput(lat, lon,apikey)
outputMN = f"<br/>Currently, the weather in St Paul, MN is: <b>{temperature}°F, <i>{weather_description}</i></b>{weather_emoji}</br>Today, in St Paul, MN the sun rises at <b>{sunrise}</b> and sets at <b>{sunset}</b>.<br/>"
temperature,weather_description,weather_emoji,sunrise,sunset = weather_ouput(lat_la, lon_la,apikey)
current_time = datetime.datetime.now().strftime("%A, %d %B, %I:%M %p %Z")
outputLA =f"And currently, the weather in Los Angeles, CA is: <b>{temperature}°F, <i>{weather_description}</i></b>{weather_emoji}</br>Today, in Los Angeles, CA the sun rises at <b>{sunrise}</b> and sets at <b>{sunset}</b>.</p>This <i>README</i> file was last refreshed on {current_time} CST.</p>"

output = outputMN+outputLA
# Read the content of your README file
# with open(BaseFolder+'/README.md', 'r+') as file:
with open('README.md', 'r+') as file:
    content = file.read()
    file.seek(0)
    file.write(re.sub(r"<br\/>Currently,.*<\/p>", output, content))
    file.truncate()

