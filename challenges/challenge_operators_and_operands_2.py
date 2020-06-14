"""Author Arianna Delgado
Created on May 29, 2020
"""

"""Input a list of numbers “num_list”.
All numbers in the list occur even times expect one number which occurs odd number of times. 
Find the number that occurs odd number of time in O(1) space complexity and O(n) time complexity.
Note: Use Bitwise operator."""


#Best solution
num_list =[1,2,2, 5, 5, 1, 3, 9, 3, 9, 6, 4, 4]
num = 0

for i in num_list:
    num = num ^ i

print("The number", num, "occurs 1 time odd." )


#Easy way to solve it
#for i in num_list:
    #count1 = num_list.count(i)
    #if count1 % 2 != 0: 
        #num = i
        #occurs = count1
             
#print("The number", num, "occurs", occurs,"time odd." )