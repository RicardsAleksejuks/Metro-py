
import urllib.request
import urllib.parse
import json

api_key = "3cad95c3ee797f12bf783c97ffd8deda"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "lang": "fi"
}

url = url + "?" + urllib.parse.urlencode(params)

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    celsius = temperature - 273.15

    print(weather)
    print(f"{celsius:.1f} °C")

except urllib.error.HTTPError as error:
    print("Error:", error.code)
    print("Check your city name and API key.")
