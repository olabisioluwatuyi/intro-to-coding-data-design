# Homework 1: Ask the user for the city name. Ask the user for the current temperature in Fahrenheit
# Convert the temperature to Celsius
# If the temperature is below freezing point (0 °C),print a warning message saying "Alert: The temperature is below freezing point."
#Otherwise, print a message saying "The temperature is above the freezing point." Lastly, always print the temperature in Celsius (up to one decimal point).
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