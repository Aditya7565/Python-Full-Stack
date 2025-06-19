# class Car:
#     def __init__(self,name,brand,speed):
#         self.name=name
#         self.brand=brand
#         self.speed=speed
#     def get_details(self):
#         print(f"Car name: {self.name}")
#         print(f"Brand: {self.brand}")
#         print(f"speed: {self.speed}")
        
# obj1=Car('BMW','AA',300)
# print(obj1.name)
# obj1.get_details()             


# class Emp:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def emp_details(self):
#         print(f"Employee name: {self.name}")
#         print(f"Employee age: {self.age}")
#         print(f"Employee salary: {self.salary}")
        
# obj2=Emp("Arun",20,50000)
# obj2.emp_details()



# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         if(b!=0):
#             return a/b
#         else:
#             return "not divide"
# a=int(input("Enter value 1: "))
# b=int(input("Enter b:"))
# obj1=Calculator(a,b)
# print(obj1.add(a,b))
# print(obj1.sub(a,b))
# print(obj1.mul(a,b))
# print(obj1.div(a,b))


      
      
      
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def cal_Area(self,length,breadth):
#         return length*breadth
#     def cal_peri(self,length,breadth):
#         return 2*(length+breadth)
        
# l=float(input("Enter length: "))
# b=float(input("Enter width:"))   
# obj2=Rectangle(l,b)
# print(obj2.cal_Area(l,b))

# print(obj2.cal_peri(l,b))








# class Student:
#     def __init__(self,name,roll,marks):
#         self.name=name
#         self.roll=roll
#         self.marks=marks
#     def get_result(self):
#         if(self.marks>40):
#             print("Pass")
#         else:
#             print("Fail")
# obj1=Student("Adi",1,55)
# obj2=Student('Shubham',2,33)
# obj3=Student("Ravi",4,55)

# obj1.get_result()
# obj2.get_result()
# obj3.get_result()



# Create a class Book with attributes title, author, and price. Create a list of 5 Book objects. Write a method to:
# Print the Title of all the books above price of 500

# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
        
#     def print_t(self):
#         if(self.price>500):
#             print(f"{self.title}")
# books=[
#     Book('The rise','Sunny',505),
#     Book('The Eagle','Ravi',400),
#     Book('The Lion','Sashi',600),
#     Book('The Hindu','Pintu',405),
#     Book('To kill','Amresh',1000)
# ]
# for book in books:
#     book.print_t()






# Create a class Movie with name, rating, genre. Create a function
# filter_movies(movies, genre) that takes list of movie objects and prints only
# the movies of the given genre.
    
class Movie:
    def __init__(self, name, rating, genre):
        self.name = name
        self.rating = rating
        self.genre = genre

def filter_movies(movies, genre):
    for movie in movies:
        if movie.genre.lower() == genre.lower():
            print(movie.name, movie.rating)

movies = [
    Movie("Inception", 8.8, "Sci-Fi"),
    Movie("The Lion", 4.4, "Action"),
    Movie("The Rise", 6.6, "Comedy")
]

filter_movies(movies, "Comedy")
