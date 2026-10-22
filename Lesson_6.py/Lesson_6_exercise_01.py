# Create a function that greets a list of persons.
# The function should take two arguments names_list and greeting_text. 
# Inside the function create a for-loop which iterates over 
# the names and prints out the greeting of your choice

# names_list = ["Maria", "Olabisi", "Ronah", "Olubukola"]
# greeting_text = "Hello, "

# Function to greet a list of people:
def greet_people(names_list, greeting_text):
  for name in names_list:
    print(f"{greeting_text}{name}")

greet_people(["Maria", "Olabisi", "Ronah", "Olubukola"], "Hello, ")
greet_people(["Maria", "Olabisi", "Ronah", "Olubukola"], "Good morning, ")
greet_people(["Maria", "Olabisi", "Ronah", "Olubukola"], "Good day, ")


# Function to greet people based on familiarity
def greet_people_special(names_list, greeting_text_standard, greeting_text_casual, greeting_text_formal):
  for name in names_list:
    if (name == "Maria"):
      print(f"{greeting_text_casual}{name}")
    elif (name == "Olabisi"):
      print(f"{greeting_text_formal}{name}")
    else:
      print(f"{greeting_text_standard}{name}")

greet_people_special(["Elissavet", "Noorina", "Chinonso", "Queensly"], "Hello ", "Wassup, ", "Good day to you, miss ")