"""Author Ariannna Delgado
Created on May 28, 2020
"""

""" Given Number is Prime or Not"""

"""1. Ask the user to enter a number 
2. Use a boolean variable called prime_flag = true;
3. Loop from 2 to number -1
4. Check if the given number % i == 0 then prime_flag == false;
5. Check if (prime_flag) then print ("prime number")
5. Else print("not prime number")"""

"""A prime number is a natural number greater than 1 
that is not a product of two smaller natural numbers. 
A natural number greater than 1 that is not prime is called a composite number. 
For example, 5 is prime because the only ways of writing it as a product, 
1 × 5 or 5 × 1, involve 5 itself.'Wikipedia'"""


#Declares variables and receives input and casts the input to an integer.
num = int(input("Please enter a number: "))
prime_flag = True

if num > 2:
    for i in range(2,num):
        if num % i == 0:
            prime_flag = False  
               
if prime_flag:
    print("Prime Number")    
else:
    print("Not a Prime Number")
    
    
