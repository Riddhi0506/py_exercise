# # TASK FIVE - FILE HANDLING AND EXCEPTION HANDLING

# # 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# # HINT: Use SyntaxError
# try:
#     eval('x === x')
# except SyntaxError:
#     print('Syntax Error')

# # 2. Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
# from sys import argv
# script, filename = argv
# while True:
#     try:
#         file = open(filename, 'r')
#         print(file.read())
#         file.close()
#         break
#     except FileNotFoundError:
#         print('File not found')
#         filename = input('Enter the file name again: ')
# # Command line: python T5andT6.py T5andT6.py

# # 3. Write a program to handle an error if the user entered the number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
# while True:
#     try:
#         number = int(input('Enter a number: '))
#         if len(str(number)) > 4:
#             raise ValueError
#         else:
#             print('Number is', number)
#             break
#     except ValueError:
#         print('The length is too long !!! Please provide only four digits')

# # 4. Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
# import getpass
# username = input('Enter username: ')
# password = getpass.getpass('Enter password: ')
# for i in range(3):
#     if username == 'admin' and password == 'admin':
#         print('Welcome', username)
#         break
#     else:
#         if username != 'admin' and password != 'admin':
#             print('Wrong username and password')
#             username = input('Enter username: ')
#             password = getpass.getpass('Enter password: ')

#         elif username != 'admin' and password == 'admin':
#             print('Wrong username')
#             username = input('Enter username: ')
#             password = getpass.getpass('Enter password: ')
#         else:
#             print('Wrong password')
#             password = getpass.getpass('Enter password: ')            

# # 5. Go through the link provided below to understand finally and raise concept:
# # https://www.programiz.com/python-programming/exception-handling
# try:
#     x = int(input('Enter a number: '))
#     y = int(input('Enter a number: '))
#     print(x/y)
# except ValueError:
#     print('Value Error')
# except ZeroDivisionError:
#     print('Zero Division Error')
# finally:
#     print('Finally block - Thank You!')


# # 6. Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:
# # Hello I am a file
# # Where you need to return the data string
# # Which is of even length
# # Make sure you return the content in The same link as it is present.
# file = open('doc.txt', 'r')
# for line in file:
#     for word in line.split():
#         if len(word) % 2 == 0:
#             print(word)
# file.close()

# # ========================================================================================================


# # TASK SIX - GENERATORS, LIST COMPREHENSION AND DECORATORS
# # 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
# string = 'Hello World'
# uppercase = [char for char in string if char.isupper()]
# print(uppercase)

# # 2. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
# # HINT - Use Zip function also
# students = ['Smit', 'Jaya', 'Rayyan']
# subjects = ['CSE', 'Networking', 'Operating System']
# values = zip(students, subjects)
# dictionary = {key: value for key, value in values}
# print(dictionary)

# # 3. Learn More about Yield, next and Generators


# # 4. Write a program in Python using generators to reverse the string.
# # Input String = “Consultadd Training”
# def reverse(string): 
#     length = len(string)
#     for i in range(length - 1, -1, -1):
# #        print(i, string[i])
#         yield string[i]
# print(''.join(reverse("Consultadd Training")))

# # 5. Write an example on decorators.
# def decorator(func):
#     def wrapper():
#         print('Before function call')
#         func()
#         print('After function call')
#     return wrapper
# @decorator
# def function():
#     print('Inside function')
# function()



