
import urllib.request
import json

url = "https://api.chucknorris.io/jokes/random"

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

response = urllib.request.urlopen(req)

data = json.loads(response.read())

print(data["value"])
