import requests

url = "https://geocoding-api.open-meteo.com/v1/search?name=munich&count=1&language=en&format=json"
response = requests.get(url)

print(response)
print(response.json())

