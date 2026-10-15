#algorithm that calculates the age of a user,at least 18 years old before allowing her/him to log-into a particular system / view certain content.
birth_year= int(input("Please enter your birth year. ")) #ask and save
current_year= 2026
age= current_year - birth_year 
if age >= 18:
    print("Access Granted! Welcome to the content.")
else: 
   print("Access denied. You are only", age, "years old.")

