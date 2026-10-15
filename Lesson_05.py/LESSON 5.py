#Create a list of dictionary items, where each dictionary represents a book with
#keys like "title", "author", and "year". Print the details of all books.
list_of_dic = [
    {"Title": "My First German Word", "Author": "Anna Becker","year": "1980"}, 
    {"Title": "The shadow of wealth", "Author": "Anita Blake", "year": "2025"},
    
]
print(list_of_dic)
for item in list_of_dic:
    print(item)
for item in list_of_dic:
    print(f"{item["Title"]} by {item["Author"]} published in {item["year"]}")
