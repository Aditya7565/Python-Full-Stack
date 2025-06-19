# Problem:
# A library wants to manage its books using Python. 


# Each book has:
# Title
# Author
# Genre
# Year of publication

# Tasks:
# Take input for 5 books and store them using a list of dictionaries.
# Create a set of all unique genres.
# Create a tuple of all authors.
# Print all books published after 2010.
# Add a new book and remove an old one based on title.



# data1={}
# for i in range(5):
#     input1=input("Enter books: ")
#     data1.append(input1)
# print(data1)
    
# data={'book_name':'A','Title':'The rising star','Author':'Adit','Genre':'Funny','Publish':2000}
# data1={'book_name':'B','Title':'The rising star','Author':'Adit','Genre':'Fight','Publish':2000}
# data2={'book_name':'C','Title':'The rising star','Author':'Adit','Genre':'Funny','Publish':2000}
# data3={'book_name':'D','Title':'The rising star','Author':'Adit','Genre':'super','Publish':2000}
# data4={'book_name':'E','Title':'The rising star','Author':'Adit','Genre':'Funny','Publish':2000}

# data5=[data,data1,data2,data3,data4]
# print(data5)
# print(data5['Genre'])
 
 
 
 
 
 
 
d1=[]
for i in range(2):
    
    title=input("Enter the title: ")
    author=input("Enter Author name: ")
    genre=input("Enter genre: ")
    year=int(input("Enter year: "))
    book={
        'Title':title,
        'Author':author,
        'Genre':genre,
        'Year':year
    }
    d1.append(book)
print(d1)
    

genres1 = set(book["Genre"] for book in d1)
print(genres1)
author1=tuple(book['Author'] for book in d1)
print(author1)

for book in d1:
    if book['Year']>2010:
        print(book)
title=input("Enter the title: ")
author=input("Enter Author name: ")
genre=input("Enter genre: ")
year=int(input("Enter year: "))

book1={
    'Title':title,
    'Author':author,
    'Genre':genre,
    'Year':year
}
d1.append(book1)
remove_title=input("Enter the title of the book to remove: ")
d1 =[book for book in d1 if book['Title'].lower()!= remove_title.lower()]
