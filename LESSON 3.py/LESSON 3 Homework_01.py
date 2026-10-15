#user should be able to enter the names and temperatures of as many cities as they want. Use a loop to facilitate this 
# and print out all the cities along with
#their temperatures in Celsius and Fahrenheit. Again, give a warning if the
#temperature is below the freezing point. To stop the loop, the user should be able to enter "exit" as the city name.
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
    




    

            













