# # TASK SEVEN - CLASSES AND OBJECTS
# # 1. Write a program that calculates and prints the value according to the given formula:Write a program in Python to find out the character in a string which is uppercase using list comprehension.
# # Q= Square root of [(2*C*D)/H]   
# # Following are the fixed values of C and H: C is 50. H is 30.
# # D is the variable whose values should be input to your program in a comma-separated sequence.

# import math
# C = 50
# H = 30
# D = input('Enter comma separated values: ')
# D = D.split(',')
# Q = []
# for i in D:
#     Q.append(round(math.sqrt((2*C*int(i))/H)))
# print(Q)

# # 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape’s area is 0 by default.
# class Shape:
#     def __init__(self):   
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, length):
#         Shape.__init__(self)
#         self.length = length
#     def area(self):
#         return self.length*self.length
# square = Square(5)
# print(square.area())

# # 3. Create a class to find three elements that sum to zero from a set of n real numbers
# # Input array: [-25,-10,-7,-3,2,4,8,10]
# # Expected output: [[-10,2,8],[-7,-3,10]]
# class Sum:
#     def __init__(self, list1):    
#         self.list1 = list1    
#     def sum(self):    
#         list2 = []
#         for i in range(len(self.list1)-2):
#             for j in range(i+1, len(self.list1)-1):
#                 for k in range(j+1, len(self.list1)):
#                     if self.list1[i] + self.list1[j] + self.list1[k] == 0:
#                         list2.append([self.list1[i], self.list1[j], self.list1[k]])
#         return list2
# list1 = [-25, -10, -7, -3, 2, 4, 8, 10]
# sum = Sum(list1)
# print(sum.sum())


# # 4. Create a Time class and initialize it with hours and minutes.
# # Create a method addTime which should take two Time objects and add them.
# # E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# # Create another method displayTime which should print the time.
# # Also create a method displayMinute which should display the total minutes in the Time.
# # E.g.- (1 hr 2 min) should display 62 minute.
# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#     def addTime(self, time1, time2):
#         self.hours = time1.hours + time2.hours
#         self.minutes = time1.minutes + time2.minutes
#         if self.minutes >= 60:
#             self.hours += 1
#             self.minutes -= 60  
#     def displayTime(self):
#         print('Total time is : ',self.hours, 'hr', self.minutes, 'min')
#     def displayMinute(self):
#         print('Time in minutes is : ', (self.hours*60)+self.minutes, 'minutes')
        
# time1 = Time(2, 50)
# time2 = Time(1, 20)
# time3 = Time(0, 0)
# time3.addTime(time1, time2)
# time3.displayTime()
# time3.displayMinute()


