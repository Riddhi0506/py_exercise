# # 1. Create a list of given structure and get the Access list as provided below:
# # x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# # Access list: [1, 2, 3, 4]Access list: [600, 700]
# # Access list: [100, 300, 500, 600, 800]
# # Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# # Access list: [10]
# # Access list: [ ]


# # 2. Create a list of thousand numbers using range and xrange and see the difference between each other. (For reference:https://www.techbeamers.com/python-xrange-range/)
# list1 = range(1,1001)
# print(list1)
# print(type(list1))

# list2 = xrange(1,1001)
# print(list2)
# print(type(list2))
# # xrange is not supported in python 3.7. Error: name 'xrange' is not defined


# # 3. How Tuple is beneficial as compared to the list?
# # Tuple is immutable. It is faster than list. It makes code safer. It is used as key in dictionary. It is used in string formatting. It is used in function arguments.


# # 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and is a multiple of 2.
# list3 = range(1,101)
# for i in list3:
#     if i%3 == 0 and i%2 == 0:
#         print(i)


# # 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.
# inputString = "Consultadd Training"
# vowels = ['a','e','i','o','u']
# inputString = inputString.lower()
# inputString = inputString[::-1]
# print(inputString)
# for i in range(len(inputString)):
#     if inputString[i] in vowels:
#         print(inputString[i],i)


# # 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an even length.
# inputString = "hello my name is abcde"
# inputString = inputString.split()
# for word in inputString:
#     if len(word)%2 == 0:
#         print(word)

# # 7. Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8. x=[1,2,3,4,5,6,7,8,9,-1]
# sum = 8
# x=[1,2,3,4,5,6,7,8,9,-1]
# for i in range(len(x)):
#     for j in range(len(x)):
#         if x[i] + x[j] == sum:
#             print(x[i],x[j])

# # 8. Write a program in Python to complete the following task:
# # Create two lists such as even_list and odd_list
# # Ask user to enter a number in the range of 1,50 and make sure if the entered number is even, append it to the even_list and if the entered number is odd append it to the odd_list.
# # Keep that in mind you can only add 5 items in each list
# # Make sure once you enter all the 5 elements, calculate the sum of the list and return the maximum of the list.
# even_list = []
# odd_list = []
# while True:
#     num = int(input("Enter 5 numbers in the range of 1,50 \n"))
#     if num in range(1,51):
#         if num%2 == 0:
#             if len(even_list) < 5:
#                 even_list.append(num)
#             else:
#                 break

#         else:
#             if len(odd_list) < 5:
#                 odd_list.append(num)
#             else:
#                 break
#     else:
#         print("You have entered a number out of range")

# if len(even_list) == 5:
#     print(sum(even_list), "is the sum of even numbers and maximum number is", max(even_list))
# if len(odd_list) == 5:
#     print(sum(odd_list), "is the sum of odd numbers and maximum number is", max(odd_list))


# # 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# # Sample input: 12abcbacbaba344ab
# # Expected output: a=5 b=5 c=2
# # NOTE: Make sure to avoid counting the occurrence of numeric values in the string.
# inputString = "12abcbacbaba344ab"
# inputString = inputString.lower()
# res=dict()
# for i in inputString:
#     if i.isalpha():
#         res[i]=inputString.count(i)

# for key,value in res.items():
#     print(key,"=",value)

# # 10. Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# tuple2 = tuple()
# for i in tuple1:
#     if i%2 == 0:
#         tuple2 = tuple2 + (i,)

# print(tuple2)
# # print(type(tuple2))