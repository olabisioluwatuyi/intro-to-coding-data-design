#Add a new functionality to your program from exercise 1.
#After the program is finished, print a summary containing the highest and lowest
#temperatures in degrees Celcius and the corresponding city names.
first_city= True
while True:
    city= input("Please enter a city, or enter exit to stop ")
    if city == "exit":
        print("The program is finished")
        break
    temperature_f= float(input("Please enter the current temperature of the city in degrees Fahrenheit."))
    print("The current temperature in", city, "is", temperature_f, "degrees Fahrenheit.")
    temperature_c = (temperature_f - 32) * 5/9
    round_temperature_c= (round(temperature_c, 2))
    print("The current temperature in", city, "is", round_temperature_c, "in degrees Celsius.")
    if round_temperature_c < 0 :
        print("Alert: The temperature in", city, "is below freezing point.")   
    if first_city:
        highest_temperature = round_temperature_c
        lowest_temperature = round_temperature_c
        highest_city = city
        lowest_city = city
        first_city = False
    else:
        if round_temperature_c > highest_temperature:
            highest_temperature = round_temperature_c
            highest_city = city
        if round_temperature_c < lowest_temperature:
            lowest_temperature = round_temperature_c
            lowest_city = city
if not first_city:
    print("Temperature Summary")
    print("The highest temperature is", highest_temperature, "degrees Celsius in",  highest_city, ".")
    print("The lowest temperature is", lowest_temperature, "degrees Celsius in",  lowest_city, ".")
