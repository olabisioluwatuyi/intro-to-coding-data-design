
import requests

# Function to get the coordinates of a city
def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    parameters = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=parameters)    
    data = response.json()
    if not data.get("results"):
     return None
    return data["results"][0]
  


# Dictionary to store weather information
cities = {}

while True:
    city = input("Please enter a city, or exit to stop: ").strip()

    if city.lower() == "exit":
        print("The program is finished")
        break

    city_result = get_coordinates(city)

    if city_result is None:
            print("City not found. Please try again.")
            continue

    latitude = city_result["latitude"]
    longitude = city_result["longitude"]
    elevation = city_result["elevation"]

        # Get current weather information
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_parameters = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,rain,cloud_cover,is_day",
            "timezone": "auto"
        }

    response = requests.get(weather_url, params=weather_parameters)
    weather_data = response.json()
    print(weather_data["current"])
    current_weather = weather_data["current"]

    temperature_c = current_weather["temperature_2m"]
    temperature_f = (temperature_c * 9/5) + 32

# Check if it is raining
    if current_weather["rain"] > 0:
     raining = "yes"
    else:
        raining = "no"

# Estimate if the sun is shining
    if (current_weather["is_day"] == 1 and
    current_weather["cloud_cover"] < 50):
            sun_shining = "yes"
    else:
        sun_shining = "no"

    cities[city] = {
        "Celsius": round(temperature_c, 2),
        "Fahrenheit": round(temperature_f, 2),
        "raining": raining,
        "sun_shining": sun_shining
    }
    print(cities)

# Print the summary
print("\nSummary:")

for city, weather in cities.items():
    temperature_c = weather["Celsius"]
    temperature_f = weather["Fahrenheit"]
    raining = weather["raining"]
    sun_shining = weather["sun_shining"]

    if sun_shining == "yes":
        sun = "sun"
    else:
        sun = "no sun"

    if raining == "yes":
        rain = "rain"
    else:
        rain = "no rain"

    print()
    print(city + ":", str(round(temperature_c)) + "°C,",
          str(round(temperature_f)) + "°F,",
          sun + " and " + rain)

    if temperature_c < 0:
        print("Warning: The temperature in", city,
              "is below the freezing point.")

    if raining == "yes" and sun_shining == "yes":
        print("There may be a rainbow in", city + ".")


