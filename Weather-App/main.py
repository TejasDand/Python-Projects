# Weather App
import requests
import json
import pyttsx3

print("\nWelcome to the Weather App! (for exit type 'Exit')\n")

while True:
    city = input("Enter the name of the city: ").title()
    
    if city == 'Exit':
        break

    url = f"https://api.weatherapi.com/v1/current.json?key=d4521167e05f4dd4adf52607252005&q={city}"
    r = requests.get(url)
    engine = pyttsx3.init()

    wdic = json.loads(r.text)
    w = wdic["current"]["temp_c"]
    updated = wdic["current"]["last_updated"]
    wind_speed = wdic["current"]["wind_kph"]

    print(f"The current weather in {city} is {w} degrees Celcius and wind speed is {wind_speed} kilometers per hour. Last updated at {updated}.\n")
    
    engine.setProperty('rate', 150)
    engine.say(f"The current weather in {city} is {w} degrees Celcius and wind speed is {wind_speed} kilometers per hour. Last updated at {updated}.")
    engine.runAndWait()

# This app doesn't working anymore because of the limited and free uses of the API Key. API Key is expired.