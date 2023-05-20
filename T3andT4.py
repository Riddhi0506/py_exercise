# # TASK THREE - DATA STRUCTURES

# # 1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
# list1 = [1, 3.14, 2+3j, "Hello", 5, 6.28, 4+5j, "World", 7, 14.42]
# print(list1)

# # 2. Create a list of size 5 and execute the slicing structure
# list2 = [1, 2, 3, 4, 5]
# # printing first 3 elements
# print(list2[0:3])

# # 3. Write a program to get the sum and multiply of all the items in a given list.
# list3 = [1, 2, 3, 4, 5]
# sum = 0
# multiply = 1
# for i in list3:
#     sum += i
#     multiply *= i
# print('Sum of all the items in the list is: ', + sum, 'and multiply is : ', + multiply)


# # 4. Find the largest and smallest number from a given list.
# list4 = [1, 2, 3, 4, 5]
# print('Largest number in the list is: ', + max(list4))
# print('Smallest number in the list is: ', + min(list4))

# # 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
# list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list6 = []
# for i in list5:
#     if i % 2 != 0:
#         list6.append(i)
# print(list6)

# # 6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
# list7 = []
# for i in range(1, 31):
#     list7.append(i**2)
# print(list7[:5])
# print(list7[-5:])

# # 7. Write a program to replace the last element in a list with another list.
# # Sample input: [1,3,5,7,9,10], [2,4,6,8]
# # Expected output: [1,3,5,7,9,2,4,6,8]
# list8 = [1, 3, 5, 7, 9, 10]
# list9 = [2, 4, 6, 8]
# list8[-1:] = list9
# print(list8)

# # 8. Create a new dictionary by concatenating the following two dictionaries:
# # Sample input: a={1:10,2:20} b={3:30,4:40}
# # Expected output: {1:10,2:20,3:30,4:40}
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# a.update(b)
# print(a)

# # 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
# # Sample input: n=5
# # Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
# n = int(input('Enter a number: '))
# dict1 = {}
# for i in range(1, n+1):
#     dict1[i] = i*i
# print(dict1)

# # 10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
# # Sample input: 34,67,55,33,12,98
# # Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
# values = input('Enter comma separated numbers: ')
# list10 = values.split(',')
# tuple10 = tuple(list10)
# print(list10)
# print(tuple10)

# ================================================================================================================

# # TASK FOUR - TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS & HIGHER ORDER FUNCTIONS
# # 1. Write a program to reverse a string.
# # Sample input: “1234abcd”
# # Expected output: “dcba4321”
# string = input('Enter a string: ')
# print(string[::-1])


# # 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# # letters.
# # Sample input: “abcSdefPghijQkl”
# # Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
# string = input('Enter a string: ')
# count1 = 0
# count2 = 0
# for i in string:
#     if i.isupper():   
#         count1 += 1
#     elif i.islower():
#         count2 += 1
# print('No. of Uppercase characters : ', + count1, '\nNo. of Lower case Characters : ', + count2)

# # 3. Create a function that takes a list and returns a new list with unique elements of the first list.
# list1 = [1, 2, 3, 4, 5, 6, 7, 2, 8, 9]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# # 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# string = input('Enter a hyphen-separated sequence of words: ')
# list3 = string.split('-')
# list3.sort()
# print('-'.join(list3))


# # 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# # Sample input: Hello world Practice makes man perfect
# # Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
# string = input('Enter a sequence of lines: ')
# print(string.upper())


# # 6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
# def sum(a, b):
#     return int(a) + int(b)    
# print(sum('2', '3'))


# # 7. Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function should print both the strings line by line.
# def max_length(a, b):
#     if len(a) > len(b):
#         print(a)
#     elif len(a) < len(b):
#         print(b)
#     else:
#         print(a)
#         print(b)
# max_length('hello', 'world3')

# # 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
# def square():
#     list4 = []
#     for i in range(1, 21):
#         list4.append(i*i)
#     print(tuple(list4))
# square()

# # 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# # Sample input: show Numbers(3) (where limit=3)
# # Expected output:
# # 0 EVEN
# # 1 ODD
# # 2 EVEN
# # 3 ODD
# def showNumber(limit):
#     for i in range(0, limit+1):
#         if i%2 ==0:
#             print(i, 'Even')
#         else:
#             print(i, 'Odd')
# showNumber(5)

# # 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
# def even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False
# list5 = list(filter(even, range(1, 21)))
# print(list5)


# # 11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
# # Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the numbers in the filtered list. Use lambda() to define anonymous functions.
# list6 = list(filter(lambda x: x%2 == 0, range(1, 11)))
# list7 = list(map(lambda x: x*x, list6))
# print(list7)


# # 12. Write a function to compute 5/0 and use try/except to catch the exceptions
# def divide():
#     return 5/0
# try:
#     divide()
# except ZeroDivisionError:
#     print('A number by ZERO!!')

# # 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
# from functools import reduce
# list8 = [1,2,3,4,5,6,7]
# list9 = reduce(lambda x,y: 10*x+y, list8) 
# print(list9)



# # 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# # Make sure to use only higher order functions.
# list10 = list(filter(lambda x: x%3 != 0 and x%7 == 0, range(1, 100)))
# print(list10)


# # 15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
# list11 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def multiply(x):
#     return x*x
# list12 = list(map(multiply, list11))
# print(list12)


# # 16. What is the output of the following codes:
# # (i) 
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

# # Output: 2

# # (ii) 
# def a():
#   try:
#       f(x, 4)
#   finally:
#       print('after f')
#       print('after f?')
# a()

# # Output: NameError: name 'f' is not defined