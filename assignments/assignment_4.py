"""Author Ariannna Delgado
Created on May 28, 2020
"""

"""Loop"""

"""Ask the user to enter a number 
Display all the numbers up to that number
Skip the multiples of 10 (used continuous)
Stop is the number is greater that 100 (break)"""

#Declares variables and receives input and casts the input to an integer.
num1 = int(input("Please enter a number:"))
num2 = 0

#Checks conditions
while num2 != num1 and num1 <= 100:
    num2 = num2 +1
    if num2 % 10 != 0:
        print(num2)