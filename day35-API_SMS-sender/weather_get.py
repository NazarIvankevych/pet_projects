import requests

# response = requests.get(
#     "http://api.openweathermap.org/data/2.5/weather?q=Chervonohrad&appid=a2f0dc5c837187609a89d447ab9e2547")
response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=50.383&lon=24.233&dt=1586468027&appid=a2f0dc5c837187609a89d447ab9e2547")
print(response.status_code)
print(response.json())
