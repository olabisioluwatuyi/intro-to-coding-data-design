chapter = 0
while chapter < 10:
    page = 0
    while page < 20:
        print(f"Chapter {chapter} Page {page}")
        page = page + 1
    print(f"Chapter finished {chapter}")
    chapter = chapter + 1
    
integer = int(input("Please enter a positive integer"))
counter = 1
sum = 0
while counter <= integer:
    sum = sum + counter
    counter = counter + 1 
print("The sum is", sum)

password = "ABCDE"
while True:
    P = str(input("Please enter the correct password"))
    if P == "exit":
        print("Program Stopped!,Thank you.")
        break
    if P == password:
        print("Welcome, Access accepted!")
        break
    else:
        print("Access Denied, Please enter the correct password.")
#Write a program that calculates and prints the sum of digits of a positive
#integer entered by the user. For example, if the user enters 123, the program
#should print 6 (which is 1 + 2 + 3)
integer = int(input("Please enter a positive integer"))
counter = 0
for counter in range (integer):
    print(f"counter{counter}")
    sum = 0
    sum
    print(f"counter {counter}")

