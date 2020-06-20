"""Author Arianna Delgado
Created on June 14, 2020
"""


#Defines a function to calculate average.
def average(a,b):
    #This variables get values as we send it.
    #The order is not important, the keywords are important for the values.
    print(a)
    print(b)
    return (a+b)/2


#Calls the function average() with passing values, 
#The return value of the function is aggregated to variable result and printed.
#result = average(a = 20, b = 10)  

#Switch the variables names.
result = average(b = 20, a = 10) 
print (result)  
