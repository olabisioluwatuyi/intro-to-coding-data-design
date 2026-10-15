# Ask the user for the city name 
# Ask the user for the current temperature in Fahrenheit
# Convert the temperature to float
# Convert the temperature to Celsius
# Check if the temperature is below freezing point
# Print the user input in a formatted string
name= str(input("Please enter the name of a city."))
temperature_f= float(input("Please enter the current temperature of the city in degrees Fahrenheit."))
print("The current temperature in", name, "is", temperature_f, "degrees Fahrenheit.")
temperature_c = (temperature_f - 32) * 5/9
round_temperature_c= (round(temperature_c, 2))
print("The current temperature in", name, "is", round_temperature_c, "in degrees Celsius.")
if round_temperature_c < 0:
    print("Alert: The temperature is below freezing point.")
elif round_temperature_c == 0:
    print("The temperature is at freezing point.")
else:
    print("The temperature is above freezing point.")



