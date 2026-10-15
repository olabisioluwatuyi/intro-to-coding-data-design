cities = {}
while True:
    city= input("Please enter a city: ")
    if city.lower() == "exit":
        print("The program is finished")
        break
    temperature_in_unit= input("Would you like to enter the temperature in degrees Fahrenheit or Celsius?: ").strip().lower ()
    if temperature_in_unit == "fahrenheit":
        temperature_f = float(input("Please enter the current temperature in Fahrenheit in " + city + ":" ))
        temperature_c = (temperature_f - 32) * 5/9
    elif temperature_in_unit == "celsius":
        temperature_c = float(input("Please enter the current temperature in Celsius in " + city + ":" ))
        temperature_f = (temperature_c * 9/5) + 32
    else:
        print("The temperature unit is invalid. Please try again.")
        continue
    raining = input("Is it raining in " + city + "? (no/yes): ").strip().lower()
    sun_shining = input("Is the sun shining in " + city + "? (no/yes): ").strip().lower()
    cities[city] = {
    "Fahrenheit": round(temperature_f, 2),
    "Celsius": round(temperature_c, 2),
    "raining": raining,
    "sun_shining": sun_shining
}
print("Summary:")
for city, weather in cities.items():
    temperature_f = weather["Fahrenheit"]
    temperature_c = weather["Celsius"]
    raining = weather["raining"]
    sun_shining = weather["sun_shining"]
    if sun_shining == "yes":
        sun = "sun"
    else:
        sun = "no sun"
    if raining == "yes":
        rain = "rain"
    else:
        rain ="no rain"
    print()
    print(city + ":", str(round(temperature_c)) + "°C, ", 
        str(round(temperature_f)) + "°F, ",
        sun + " and " + rain)
    if temperature_c < 0:
        print("Warning: The temperature in", city, "is below the freezing point")
    if raining == "yes" and sun_shining == "yes":
        print("There is a rainbow in", city + ".")
  
    