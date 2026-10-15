#Create a list with 4 students. 
# Append one student to the end of your list students. 
# Edit the third student in your list, with a new name. 
# Delete the first student in your list.
#  Print how many items are in your list. 
# Sort your list.
names = ["Olabisi", "Lilian", "Noor", "Margret"]
print(names)
names.append("Maria")
print(names)
names[2]= "Queensly"
print(names)
names.remove("Olabisi") # names.pop(0)
print(names)
print(len(names))
names.sort()
print(names)