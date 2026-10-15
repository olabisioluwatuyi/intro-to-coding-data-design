#Create a list of even numbers from 2 to 20 (inclusive) using a loop.
#Print the list.
#range (start, stop, step), start at 2, stop before 21 (20 inclusive), move forward by 2 every time
even_numbers =[]
for number in range(2, 21, 2):
    even_numbers.append(number)
print("The even numbers are", even_numbers)
