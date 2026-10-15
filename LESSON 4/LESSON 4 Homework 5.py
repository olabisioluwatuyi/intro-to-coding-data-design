#Write a program that takes a list of numbers as input and
#prints the largest and smallest numbers in the list. numbers = [12, 3, 5, 19, 7, 3, 1, 5]
#largest = numbers[0], smallest = numbers[0] to Start with the first value in the list
numbers = [19, 23, 5, 9, 37, 103, 4, 7]
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest: 
        smallest = number
print("The largest number is", largest)
print("The smallest number is", smallest)