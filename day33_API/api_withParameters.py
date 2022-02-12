import requests

# pick it from https://www.latlong.net/
MY_LAT = 50.747234
MY_LONG = 25.325382

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)