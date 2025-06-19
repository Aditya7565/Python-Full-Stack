
# Write a function get_max(num1, num2) that returns the maximum of the two numbers.



# def get_max(num1,num2):
#     if(num1>num2):
#         return num1
#     else:
#         return num2
# x=int(input("Enter value 1: "))
# y=int(input("Enter value 2: "))
# a=get_max(x,y)
# print(a)


# Write a function count_vowels(s) that returns the number of vowels in the given string.
# Input: "Hello World"
# Output: 3




# def count_vowel(s):
#     count=0
#     v=['A','E','I','O','U','a','e','i','o','u']
#     for i in s:
#         if i in v:
#             count+=1
#     return count
    
# s=input("Enter string: ")
# t=count_vowel(s)
# print(t)








# Write a function sum_numbers(lst) that returns the sum of all numbers in a list.

# Input : [1,2,3,4,5]
# Output : 15

# l=[]
# n=int(input("Enter no of element: "))
# for i in range(n):
#     s=int(input(f"Enter value  {i+1}: "))
#     l.append(s)
# def sum_numbers(l):
#     sum=0
#     for i in l:
#         sum=sum+i
#     return sum
# t=sum_numbers(l)
# print(t)



# Write a function get_min_max(lst) that returns the minimum and maximum of the list .
# Input: [3, 5, 1, 9, 7]
# Output: (1, 9)
# l=[]
# n=int(input("Enter no of element: "))
# for i in range(n):
#     s=int(input(f"Enter value  {i+1}: "))
#     l.append(s)
# def get_min_max(l):
#     max=l[0]
#     min=l[0]
#     for i in l:
#         if(i>max):
#             max=i
#         if(i<min):
#             min=i
#     return max,min
# s=get_min_max(l)
# print(s)




# Write a function word_frequency(sentence) that returns a dictionary with word frequency.
# Input: "this is a test this is not fun"
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 1, 'not': 1, 'fun': 1}

          
         
# def word_frequency(sentence):
#     freq = {}
#     words = sentence.split()
#     for word in words:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#     return freq

# sentence = input("Enter sentence: ")
# t = word_frequency(sentence)
# print(t)

      
            










# Write a python function to remove duplicates from a dictionary

#   data = [
# {"id": 1, "name": "Alice"}, 
#   {"id": 2, "name": "Bob"},
#  {"id": 1, "name": "Charlie"}, 
#  {"id": 3, "name": "Alice"}
#  ]

# def remove_duplicates_by_id(data):
#     unique_ids = set()
#     result = []
#     for item in data:
#         if item['id'] not in unique_ids:
#             unique_ids.add(item['id'])
#             result.append(item)
#     return result

# data = []
# n = int(input("Enter number of entries: "))
# for i in range(n):
#     print(f"\nEntry {i+1}")
#     id_val = int(input("Enter ID: "))
#     name_val = input("Enter Name: ")
#     data.append({"id": id_val, "name": name_val})

# print("\nOriginal Data:")
# print(data)

# cleaned_data = remove_duplicates_by_id(data)

# print("\nAfter Removing Duplicates by ID:")
# print(cleaned_data)








# Write a Python code to print the factorial 
# Formula : n! = n*(n-1)*....*1(base : 0! = 1)

# Take the input from the user as n , 

# Example : 
# Input : 5
# Output : 120



# def fact(n):
#     f=1
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter value: "))
# t=fact(n)
# print(f"Factorial of {n} is : ",t)





  