#Write a program that asks the user for their favorite colors (up to 5)
#and stores them in a list. Then, create a sentence that says,
#"Your favorite colors are: color1, color2, ..." using the .join() function.
colors = [] 
for counter in range(5):
    color = input("Please enter a favorite color or type 'done' to finish inputing:")
    if color == 'done':
     break
    colors.append(color)
favorite_colors = ", ".join(colors)
print("Your favorite colors are", favorite_colors)

