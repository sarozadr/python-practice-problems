"""Author Ariannna Delgado
Created on May 28, 2020
"""



"""Ask the user to enter a number 
Display all the numbers up to that number
Skip the multiples of 10 (used continuous)
Stop is the number is greater that 100 (break)"""


num = int(input("Please enter a number:"))
#print(num)

while num <= 100 and num > 0:
    if num % 10 != 0:
        print(num)
        num = num -1 
    else:
        num = num -1
        

