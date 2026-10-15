#Exercise 1:Ask the user to enter two numbers (num1 and num2) using input(). Convert the input to integers and compare if num1 is greater than num2. Print the result.
num_1= int(input("Please enter the first number")) #ask and save
num_2= int(input("Please enter the second number")) #ask and save
if num_1 < num_2:
    print("The first number is less than the second number.")
else:
    print("The first number is greater than the second number.")

#Exercise 2:Ask a user to enter their name. If the name has 6 characters or more, inform the user that they have a long name.
name= str(input("Please enter your name.")) #ask and save
if len(name) >= 6:
    print("You have a long name.")
else:
    print("You have a short name.")
#Exercise 3:Ask the user to enter an integer using input(). Convert the input to an integer and determine if it's even or odd. Print the result.
num= int(input("Please enter a number"))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
#Exercise 4:Set a password (e.g., "python123") as a string. Ask the user to enter a password using input(). Compare the user's input with the actual password and check if they match. Print "Access Granted" if the password is correct; otherwise, print "Access Denied".
password= 'python123'
password= str(input("Please enter your password."))
if password == 'python123':
    print("Access Granted!")
else:
    print("Access Denied!")
password= 'python123'
password= str(input("Please enter your password."))
if password == 'python123':
    print("Access Granted!")
else:
    print("Access Denied!")    
#Exercise 5:Ask the user to enter a numeric grade (0 to 100) using input().Convert the input to an integer and classify the grade as follows:90 or above:"A" 80 to 89:"B" 70 to 79:"C" 60 to 69:"D" Below 60:"F" Print the grade classification.
grade= int(input("Please enter your numeric grade."))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
#Exercise 6:Ticket Price Ask the user to enter their age using input(). Convert the input to an integer and determine the ticket price based on age: 0 to 3 years: Free, 4 to 12 years: $10, 13 to 64 years: $15 65 and above: $5. Print the ticket price.
age= int(input("Please enter your age."))
if age <= 3:
    print("Your ticket is free")
elif age <= 12:
    print("Your ticket is 10$")
elif age <= 64:
    print("Your ticket is 15$")
else:
    print("Your ticket is 5$")

#Exercise 7:Enhance the code below, so that when a user wants anything else besides coffee or tea you inform the user that the required beverage is not available:
print("Turning on the machine...")
beverage = str(input("Do you want tea or coffee?"))
if beverage == "tea":
    print("Preparing tea...") 
elif beverage == "coffee" :
    print("Preparing coffee...")
elif beverage != "tea":
    print("The required beverage is not available")
elif beverage != "coffee":
    print("The required beverage is not available")
else:
   print("Turning off the machine.")
