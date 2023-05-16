# # TASK ONE - NUMBERS AND VARIABLES

# '''
# 1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.
# '''

# a, b, c = 1, 2.01, "Riddhi"
# print(a, b, c)


# '''
# 2. Create a variable of type complex and swap it with another variable of type integer.
# '''
# a = 5 + 4j
# b = 2
# a, b = b, a
# print("a = " , a, " \nb = ", b)


# '''
# 3. Swap two numbers using a third variable and do the same task without using any third variable.
# '''
# a = 15
# b = 20
# temp = a
# a = b
# b = temp
# print("a = " , a, " \nb = ", b)

# a = 150
# b = 200
# a, b = b, a
# print("a = " , a, " \nb = ", b)


# '''
# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
# '''
# # Currently I am using python3 hence raw_input function is not working. However if we want to take user input in Python 2.x below code will work.
# # a = raw_input("Enter a string: ")
# # print("String is - " , a)

# # Python 3.x
# a = input("Enter a string: ")
# print("String is - " , a)


# '''
# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and print result as the final output.
# '''
# print("Enter any 2 numbers in between 1-10")
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a in range(1, 11) and b in range(1, 11):
#     z = a + b
#     result = z + 30
#     print("Result is - ", result)

# else:
#     print("Entered numbers are not in between 1-10")
#     exit()
    

# '''
# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say -  The input value data type is : int/float/string/etc
# '''
# user_input = input("Enter a value: ")

# if user_input.isdigit():
#     print("The data type of input value is: int")
# elif isinstance(user_input,str):
#     print("The data type of input value is: float")
# else:
#     print("The data type of input value is: " + type(user_input).__name__)


'''
7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
'''
# # Upper CamelCase
# UpperCamelCase = "Upper CamelCase"
# print(UpperCamelCase)

# # Lower CamelCase
# lowerCamelCase = "Lower CamelCase"
# print(lowerCamelCase)

# # SnakeCase
# snake_case = "SnakeCase"
# print(snake_case)

# # UPPERCASE
# UPPERCASE = "UPPERCASE"
# print(UPPERCASE)

# '''
# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?
# '''
# # Yes, it will change the value. Because python is a dynamically typed language because of which we do not need to mention the type of variable. 
# # Python itself identifies the type of variable based on the value assigned to it. Hence, if we assign a different data type value to a variable, it will overwrite and change the value.

# a = 10
# print("a = " , a, type(a))
# a = "Riddhi"
# print("a = " , a, type(a))

# #============================================================================================


# # TASK TWO - OPERATORS AND DECISION MAKING STATEMENT

# '''
# 1. Write a program in Python to perform the following operation:
# ● If a number is divisible by 3 it should print “Consultadd” as a string
# ● If a number is divisible by 5 it should print “Python Training” as a string
# ● If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
# '''

# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Consultadd - Python Training") 
# elif num % 5 == 0:
#     print("Python Training")
# elif num % 3 == 0:
#     print("Consultadd")
# else:
#     print("Number is not divisible by 3 or 5")

# '''  
# 2. Write a program in Python to perform the following operator based task:
# ● Ask user to choose the following option first:
# ○ If User Enter 1 - Addition
# ○ If User Enter 2 - Subtraction
# ○ If User Enter 3 - Division
# ○ If USer Enter 4 - Multiplication
# ○ If User Enter 5 - Average
# '''

# print("Choose from the following option: \n1 - Addition \n2 - Subtraction \n3 - Division \n4 - Multiplication \n5 - Average")
# choice = int(input("Enter your choice: "))
# if choice in range(1, 5):
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     if choice == 1:
#         result = num1 + num2
#         print("Addition is - ", result)
#     elif choice == 2:
#         result = num1 - num2
#         print("Subtraction is - ", result)
#     elif choice == 3:
#         result = num1 / num2
#         print("Division is - ", result)
#     elif choice == 4:
#         result = num1 * num2
#         print("Multiplication is - ", result)
# elif choice == 5:
#     first= int(input("Enter first number: "))
#     second = int(input("Enter second number: "))
#     result = (first + second) / 2
#     print("Average is - ", result)
# else:
#     print("Invalid choice")

# if result < 0:
#     print("NEGATIVE")

# '''
# 3. Write a program in Python to implement the given flowchart:
# '''
# a, b, c = 10, 20, 30
# avg = (a + b + c) / 3
# print("avg = ", avg)
# if avg > a and avg > b and avg > c:
#     print("avg is higher than a, b, c")
# elif avg > a and avg > b:
#     print("avg is higher than a and b")
# elif avg > a and avg > c:
#     print("avg is higher than a and c")
# elif avg > b and avg > c:
#     print("avg is higher than b and c")
# elif avg > a:
#     print("avg is higher than just a")
# elif avg > b:
#     print("avg is higher than just b")
# elif avg > c:
#     print("avg is higher than just c")

# '''
# 4. Write a program in Python to break and continue if the following cases occurs:
# ● If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
# '''
# while True:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("It's Over")
#         break
#     else:
#         print("Good Going")
#         continue

# '''
# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
# '''
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)

# '''
# 6. What is the output of the following code examples?
# '''
# x = 123
# for i in x:
#     print(i)
# Output:
# # TypeError: 'int' object is not iterable

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print("error")
# Output:
# # 0
# # error
# # 1
# # error
# # 2

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
# Output:
# # 0
# # 1
# # 2
# # 3
# # 4

# '''
# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
# '''
# for i in range(0, 7):
#     if i == 3 or i == 6:
#         continue
#     print(i)

# '''
# 8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2
# '''

# string = input("Enter a string: ")
# letters = 0
# digits = 0
# for i in string:
#     if i.isalpha():
#         letters += 1
#     elif i.isdigit():
#         digits += 1
# print("Letters ", letters, "Digits ", digits)

# '''
# 9. Read the two parts of the question below:
# ● Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
#  Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
# '''

# lucky_number = 5
# while True:
#     guess = int(input("Guess the lucky number: "))
#     if guess == lucky_number:
#         print("You guessed the correct number")
#         break
#     else:
#         print("You guessed the wrong number")
#         continue

# lucky_number = 5
# while True:
#     guess = int(input("Guess the lucky number: "))
#     if guess == lucky_number:
#         print("You guessed the correct number")
#         break
#     else:
#         answer = input("Do you want to guess again? ")
#         if answer == "no":
#             print("Good Bye")
#             break
#         else:
#             continue

# '''
# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
# ● While counter <= 5:
# ● print(“Type in the”, counter, “number”
# ● counter=counter+1
# The program asks for for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
# '''

# lucky_number = 5
# counter = 1
# while counter <= 5:
#     guess = int(input("Guess the lucky number: "))
#     if guess == lucky_number:
#         print("Good guess!")
#     else:
#         print("Try again!")
#     counter += 1
# print("Game over!")

# '''
# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.
# '''

# lucky_number = 5
# counter = 1
# while counter <= 5:
#     guess = int(input("Guess the lucky number: "))
#     if guess == lucky_number:
#         print("Good guess!")
#         break
#     else:
#         print("Try again!")
#     counter += 1
# else:
#     print("Sorry but that was not very successful")
# print("Game over!")
