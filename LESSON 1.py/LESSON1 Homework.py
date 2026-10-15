# Enter the name of a city and the current temperature in Celsius. 
name= (input("Please enter the name of a city  ")) # ask and save 
temperature= float(input("Please enter the current temperature of the city in celsius ")) # ask and save
print("The currrent temperature in ", name," is", temperature, "degrees Celsius.")
#Enter the name of two cities and the current temperatures in each city in Celsius. Display the average temperature.
name_1= (input("Please enter the name of the first city  ")) # ask and save 1
name_2= (input("Please enter the name of the second city  ")) # ask and save 2
temperature_1= float(input("Please enter the current temperature of the first city in celsius ")) # ask and save 1
temperature_2= float(input("Please enter the current temperature of the second city in celsius ")) # ask and save 2
average_c= (temperature_1+temperature_2) / 2
#Convert and print the average temperature in Fahrenheit.
average_f= (average_c * 9/5) + 32
print(average_c)
print(average_f)
print("The average temperature between", name_1, "and", name_2, "is", average_c, "degrees Celsius.")
print("The average temperature between", name_1, "and", name_2, "is", average_c, "degrees Celsius." "That is", average_f, "degrees Fahrenheit.")