    #    Single Inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name
#         print(f"{self.name} the name of Animal")
#     def speak(self):
#         print("A genric sound")

# class Dog(Animal):
#     def __init__(self,name, breed,color):
#         super().__init__(name)
#         self.breed=breed
#         self.color=color
        
#     def Make_sound(self):
#         print("Dog Barks  ")
# obj1=Dog("Leo","Labra","Black")
# obj1.speak()
# obj1.Make_sound()




# Create a class Appliance with brand and power consumption. Inherit Fan, AC,
# and Heater classes from it, each with a method show_details() displaying their 
# specific features and inherited ones.

# class Appliance:
#     def __init__(self,brand,power):
#         self.brand=brand
#         self.power=power
# class Fan(Appliance):
#     def __init__(self, name,brand, power):
#         self.name=name
#         super().__init__(brand, power)
        
#     def show_details(self):
#         print("Fan ")
#         print(f"name is: {self.name}")
#         print(f"power consumption: {self.power}")
        
# class Heater(Appliance):
#     def __init__(self,name, brand, power):
#         self.name=name
#         super().__init__(brand, power)
#     def show_details(self):
#         print("Heater ")
#         print(f"name is: {self.name}")
#         print(f"power consumption: {self.power}")
        
# obj1=Fan("Rajdoot","Tata",220)
# obj1.show_details()
# obj2=Heater("AD","jj",440)
# obj2.show_details() 
    
    
    

# Create a class Person with attributes name and age. Inherit a class Student 
# from Person that adds an attribute roll_number. Create an object of Student 
# and display all its details

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self, name, age,roll):
#         super().__init__(name, age)
#         self.roll=roll
#     def details(self):
#         print("Details of the Student ")
#         print(f"Name of the student is : {self.name}")
#         print(f"Student age is : {self.age}")
#         print(f"Roll no : {self.roll}")
# obj1=Student("Krishna",22,1)
# obj1.details()





            # MULTIPLE INHERITANCE


# class A:
#     def method_a(self):
#         print("Methoa a")

# class B:
#     def method_b(self):
#         print("Methoa B")

# class C(A,B):
#     def method_c(self):
#         print("Methoa C")
        
# test_obj=C()
# test_obj.method_c()



# Create a class Account with a constructor that initializes balance.
# Inherit a class SavingsAccount that uses super() to call the parent 
# constructor and adds interest_rate. Print all attributes.

class Account:
    def __init__(self,bal):
        self.bal=bal
class SavingAccount(Account):
    def __init__(self, bal,intrest_rate):
        super().__init__(bal)
        self.intrest_rate=intrest_rate
    def details(self):
        print(f"Bal is :{self.bal}")
        print(f"Intreset is : {self.intrest_rate}")
        
obj1=SavingAccount(10000,100)
obj1.details()