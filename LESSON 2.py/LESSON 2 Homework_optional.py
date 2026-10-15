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
