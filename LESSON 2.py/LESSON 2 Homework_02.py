#Homweork 2: Ask the user for the name of two cities and the current temperatures in Fahrenheit. Convert the temperatures to Celsius.
#If the temperature in both cities is below freezing point (32 °F), 
#print a warning message saying "Alert: The temperatures in both cities are below freezing point."
#else if the temperature in only one of the cities is below freezing point,
#print a warning message saying "Alert: The temperature in one of the cities is below freezing point."
#Otherwise, print a message saying "The temperatures in both cities are above the freezing point."
#Lastly, always print the temperatures in Celsius (up to one decimal point).
name_1= str(input("Please enter the name of the first city."))
temperature_1_f= float(input("Please enter the current temperature of the first city in degrees Fahrenheit."))
print("The current temperature in", name_1, "is", temperature_1_f, "degrees Fahrenheit.")
temperature_1_c = (temperature_1_f - 32) * 5/9
round_temperature_1_c= (round(temperature_1_c, 2))
print("The current temperature in", name_1, "is", round_temperature_1_c, "in degrees Celsius.")
name_2= str(input("Please enter the name of the second city."))
temperature_2_f= float(input("Please enter the current temperature of the second city in degrees Fahrenheit."))
print("The current temperature in", name_2, "is", temperature_2_f, "degrees Fahrenheit.")
temperature_2_c = (temperature_2_f - 32) * 5/9
round_temperature_2_c= (round(temperature_2_c, 2))
print("The current temperature in", name_2, "is", round_temperature_2_c, "in degrees Celsius.")
if round_temperature_1_c < 0 and round_temperature_2_c < 0:
    print("Alert: The temperatures in both cities are below freezing point.")
elif round_temperature_1_c < 0 or round_temperature_2_c < 0:
     print("Alert: The temperature in one of the cities is below freezing point.")
else:
     print("The temperatures in both cities are above freezing point.")