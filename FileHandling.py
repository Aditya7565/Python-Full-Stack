
# f=open("test.txt")
# read_txt=f.read()
# print(read_txt)
# f.close()

# f=open("test.txt")
# read_txt=f.readline()
# print(read_txt)
# f.close()


# f=open("test.txt")
# read_txt=f.readlines()
# print(read_txt)
# f.close()


# f=open("C:\Users\HP\OneDrive\Desktop\file1.txt","r") it is wrong
# f=open("C:/Users/HP/OneDrive/Desktop/file1.txt","r")

# read_txt=f.read()
# print(read_txt,"\n")
# f.close()



# f=open("test.txt")
# write_txt=



# f=open("test.txt")
# read_txt=f.readlines()
# for i in read_txt:
#     print(i)
# print(read_txt)
# f.close()

# with open("test.txt","w") as f:
#     f.write("python\n")
#     f.write("java")
# f=open("test.txt")
# read_txt=f.read()
# print(read_txt)
# f.close()

# with open("test.txt","r") as f:
#      con=f.read()
#      print(con)


# with open("test.txt","a") as f:
#      f.write("\n python is fantastic ")

# import os
# if os.path.exists("test.txt"):
#     print("File exist")
# else:
#     print("File does not exist ")
    
# deleting a file
# import os 
# os.remove("test.txt")


# try:
#     with open("test.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found ")
    
    


# with open("user.txt","a") as f:
#     name=input("Enter name: ")
#     # f.write(name+"\n")
#     f.append(name+"\n")
    




# with open("user.txt","r") as f:
#     for pro in f:
#         print(pro.strip())


# writting or logs 

# from datetime import datetime
# with open("log.txt","a" ) as log:
#     log.write(f"logged at {datetime.now()}\n")



# # reading configuartion File
# setting={}
# with open("config.txt","r") as f:
#     for line in f:
#         key,value=line.strip().split("=")
#         setting[key]=value
# print(setting)


# 1. Accept 3 lines from user and save to user_input.txt
# 2. Read and display content of user_input.txt
# 3. Append data in the file to log.txt




# with open("user_input.txt","w") as f:
#     for i in range(3):
#         user=input("Enter user name: ")
#         f.write(user+"\n")
# with open ("user_input.txt","r") as f:
#     con=f.read()
#     print(con)
# with open("user_input.txt","a") as log_file:
#     log_file.write(con)
    
# Write a Python program that:
# Accepts student names, marks (out of 100), and subjects from the user.
# Stores them in a file named report.txt in the format ( Name: Alice, Subject: Math, Marks: 88 )
# Reads the file and displays:
# All entries
# The total number of students
# The average marks
# n = int(input())
# with open("report.txt", "w") as f:
#     for _ in range(n):
#         name = input("Enter name:")
#         subject = input("Enter Subject: ")
#         marks = int(input("Enter Marks: "))
#         f.write(f"Name: {name}, Subject: {subject}, Marks: {marks}\n")

# with open("report.txt", "r") as f:
#     entries = f.readlines()
# for entry in entries:
#     print(entry.strip())

# print("Total Students:", len(entries))

# total_marks = 0
# for entry in entries:
#     parts = entry.strip().split(", ")
#     for part in parts:
#         if part.startswith("Marks:"):
#             total_marks += int(part.split(":")[1])

# average = total_marks / len(entries) if entries else 0
# print("Average Marks:", average)











# f = open("report.txt", "w")
# count = int(input("Enter number of students: "))
# for i in range(count):
#     name = input("Enter name: ")
#     subject = input("Enter subject: ")
#     marks = input("Enter marks: ")
#     f.write("Name: " + name + ", Subject: " + subject + ", Marks: " + marks + "\n")
# f.close()

# f = open("report.txt", "r")
# lines = f.readlines()
# f.close()

# print("\nAll Entries:")
# for line in lines:
#     print(line.strip())

# print("Total Students:", len(lines))

# total = 0
# for line in lines:
#     parts = line.strip().split(", ")
#     for part in parts:
#         if "Marks" in part:
#             total += int(part.split(": ")[1])

# print("Average Marks:", total / len(lines))





# try:
#     file=open("abc.txt","r")
#     data=file.read()
#     print(data)
# except FileNotFoundError:
#     print("File does not exist")
# finally:
#     print("Execution End")  
    
    
    
# try:
#     num=int(input("Enter number:"))
#     result=10/num
# except ZeroDivisionError:
#     print("you can't divide ")
# except ValueError:
#     print("Invalid input ")
# finally:
#     print("Done")

# Simulate a bank withdrawal system:
# Ask for balance and withdrawal amount
# Use try-except-finally to handle it gracefully and always show final balance   

# balance = float(input("Enter your current balance: "))

# try:
#     amount = float(input("Enter amount to withdraw: "))
#     if amount > balance:
#         raise ValueError("Insufficient balance.")
#     balance -= amount
#     print("Withdrawal successful.")
# except ValueError as e:
#     print("Error:", e)
# finally:
#     print("Final Balance:", balance)


# Ask the user to input an index
# Access that index from a predefined list
# Handle IndexError and ValueError using nested try blocks
# Print “End of program” using finally


# l1=['Apple','banana','guava','grapes']
# try:
#     index1=int(input("Enter index: "))
#     print(l1[index1])
# except ValueError:
#     print("invalid input ")
# except IndexError:
#     print("out of index")
# finally:
#     print("End of  program ")


# class AgeToLowError(Exception):
#     def __init__(self, age):
#         self.age=age
#         super().__init__(f"Age {age} is too low to register")
        # print("Age is to low to register")
        # print(age)

# age=int(input("Enter Age:"))
# if age<18:
#     raise AgeToLowError(age)
# else:
#     print("Registration successfull")
# try:
#     raise AgeToLowError(age)

# except AgeToLowError as e:
#     print("custom Excepition: ",e)



  

# Error logging

# import logging

# logging.basicConfig(filename="app.log", level=logging.INFO,
#                     format="%(asctime)s - %(levelname)s - %(message)s")

# logging.info("Program started")

# try:
#     x = 10 / 0
# except ZeroDivisionError as e:
#     logging.error("Error occurred: %s", e)
    

import logging
class LoginError(Exception):
    pass
logging.basicConfig(filename="login.log",level=logging.ERROR)
username=input("Enter username : ")
if username!="admin":
    error=LoginError("Unauthorized access attempt")
    logging.error("login failed:%s",error)
    raise error
    
else:
    print("Welcome admin") 
    