#Write a program that calculates and prints the sum of all numbers from 1 to a user-specified positive integer.  
count = 1
sum = 0
num = int(input("Please enter a positve integer "))
while count <= num:
    sum = sum + count
    count = count + 1
print("The sum of number is", sum)