import requests
from typing import Dict
import json

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
# What I DID: Registered an account on OpenWeatherMap, recieved an email with my own API key
API_KEY = "3deff6e8c77b8970c66ad0356c33b1a7"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()


# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
API_KEY_0 = r"https://official-joke-api.appspot.com/jokes/random" #r: the string is to be treated as a raw string

def get_joke(API_KEY_0):
    #same impliementation above using request.get
    res0 = requests.get(API_KEY_0)
    #read JSON encoded data from a file and convert it into a Python dictionary
    joke = json.loads(res0.text)
    return joke

def main():
    temp = get_weather("London")
    #print(temp)
    
    weather = temp["main"]
    print("City: ", temp["name"], sep="")
    print("Current temp: ", weather["temp"], "Kelvin")

    joke = get_joke(API_KEY_0)
    print("The random joke is: ", joke["setup"])
    print("The punchline is: ", joke["punchline"])


if __name__ == "__main__":
    main()
