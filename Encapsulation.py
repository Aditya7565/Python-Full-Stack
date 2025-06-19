
# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name     #public
#         self._age=age      #protected
#         self.__marks=marks    #private
#     def display_info(self):
#         print(f"Name of the student is : {self.name}")
#         print(f"Student age is : {self._age}")
#     def get_marks(self):
#         print(f"Marks of the student : {self.__marks}")
#     def set_marks(self,new_marks):
#         if 0<=new_marks<=100:
#             self.__marks=new_marks
#             print("New Mark has been assigned")
#         else:
#             print("Invalid")
        
# s1=Student("Ravi",23,50)
# s1.display_info()
# s1.get_marks()
# s1.set_marks(89)
# s1.get_marks()
# try:
#     print("praivate: ",s1.__marks)
# except AttributeError:
#     print("Private attribute can not be accessed")
    






# Create a class Account with a private attribute __balance. Create:
# A getter method get_balance()
# A setter method set_balance() that ensures balance cannot be negative
#   Create an object, try to access balance directly, then use methods instead.

# class Account:
#     def __init__(self,__balance):
#         self.__balance=__balance
#     def get_balance(self):
#         print(f"Balance is : {self.__balance}")
        
#     def set_balance(self,__newbalance):
#         if __newbalance>0:
#             self.__balance=__newbalance
#             print("new balance updated")
        
# s2=Account(1000)
# s2.get_balance()
# s2.set_balance(20000)
# s2.get_balance()
        
        
# Design a class ATM:
# Private balance
# Method Withdraw (if sufficient balance)
# Method to deposit
# Method to check balance
#   Use proper validation inside deposit and withdraw methods.  

class ATM:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        if self.balance>self.withdraw:
            print("you can withdraw")
            self.balance-=self.withdraw
        else:
            print("Amount is not sufficient")
    def deposit(self,deposit):
        self.deposit=deposit
        self.balance+=self.deposit
    def check_balance(self):
        print(f"Avaialble balance is :{self.balance}")
obj1=ATM(20000)
obj1.check_balance()
obj1.withdraw(5000)
obj1.check_balance()
obj1.deposit(6000)
obj1.check_balance()