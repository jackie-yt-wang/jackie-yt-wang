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
    

# Define a function to get the current weather data for a location and return the temperature, weather description, weather emoji, sunrise, and sunset
def weather_output(lat, lon, apikey):
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

# Call the weather_output function for St. Paul, MN and Los Angeles, CA
lat_mn, lon_mn = 44.9544, -93.0900  # St Paul, MN coordinates
lat_la, lon_la = 34.0522, -118.2437  # Los Angeles, CA coordinates

# Call the weather_output function to get the current weather data
temperature_mn, description_mn, emoji_mn, sunrise_mn, sunset_mn = weather_output(lat_mn, lon_mn, apikey)
temperature_la, description_la, emoji_la, sunrise_la, sunset_la = weather_output(lat_la, lon_la, apikey)

output = f"<br/>Currently, the weather in St Paul, MN is: <b>{temperature_mn:.2f}°F, <i>{description_mn}</i></b>{emoji_mn}</br>" \
         f"And the weather in Los Angeles, CA is: <b>{temperature_la:.2f}°F, <i>{description_la}</i></b>{emoji_la}</br>" \
         f"Today, in St Paul, MN the sun rises at <b>{sunrise_mn}</b> and sets at <b>{sunset_mn}</b>." \
         f"<br/><br/><img align='left' alt='jpg' src='https://thumbs.dreamstime.com/b/twin-cities-skyline-monochrome-silhouette-vector-illustration-203367510.jpg' width='180' height='135' />" \
         f"<br/><img align='left' alt='jpg' src='https://static.vecteezy.com/system/resources/previews/013/749/922/original/los-angeles-city-skyline-silhouette-background-in-california-landscape-black-and-white-silhouette-vector.jpg' width='180' height='135' />" \
         "<br/><br/><br/><br/><br/><br/>" \
         "<hr>" \
         "<h3>Where to find me</h3>" \
         f"<p><a href='https://github.com/jackie-yt-wang' target='_blank'><img alt='Github' src='https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=Github&logoColor=white' /></a> <a href='https://www.linkedin.com/in/jackie-yutang-wang/' target='_blank'><img alt='LinkedIn' src='https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white' /></a>" \
         f"<br/><br/>This <i>README</i> file was last refreshed on {datetime.datetime.now().strftime('%A, %d %B, %I:%M %p %Z')} CST.</p>"

# Read the content of your README file
# with open(BaseFolder+'/README.md', 'r+') as file:
with open('README.md', 'r+') as file:
    content = file.read()
    file.seek(0)
    file.write(re.sub(r"<br/>Currently,.*.</p>", output, content))
    file.truncate()

