"""Author Arianna Delgado
Created on May 15, 2020
"""


"""Write a Python program to display the current date and time."""
import datetime 
from math import pi


now = datetime.datetime.now()

print("Current date and time: ")
print(now.strftime("%Y-%M-%D  %H:%M:%S"))




"""Write a Python program which accepts the radius of a circle from the 
user and compute the area of the circle."""
print()
print()
r= float(input("Please, enter the radius of the circle:") )
print("The radius entered is r = "+ str(r)+"." +" The area of the circle is: "+ str(pi * (r**2)))




""" Write a Python program which accepts a sequence of comma-separated numbers
 from the user and generates a list and a tuple with those numbers. 
 Sample data: 3, 5, 7, 23"""
print()
print()
numbers = str(input("Please enter the numbers: "))
list1 = numbers.split(",")
tuple1 = tuple(list1)
print(list1)
print(type(tuple1))




"""Write a Python program to test whether a number is within 100 of 1000 or 2000"""
print()
print()
n = int(input("Please enter a number to test if the number is within 100 of 1000 or 2000: "))

if ((abs(1000 - n) <= 100) or (abs(2000-n) <= 100)):
    print("True")
else:
    print("False")





"""Write a Python program to check whether a specified value is contained in a group of values. 
Test Data:"""
print()
print()
list1 = [1, 5, 8, 3]
value = int(input("Please enter an value to check if it in the list: " ))

if value in list1:
    print("Yes, the value is in the list.")
else: 
    print("No, the value  is not in the list.")    
    




"""Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference."""
print()
print()
number1= int(input("Please enter a number: "))
difference = number1 - 17
abs_num = 0
if difference > 17:
    difference = difference * 2
    abs_num = abs(difference)
    print(abs_num)
else:
    abs_num = abs(difference)
    print(abs_num)












