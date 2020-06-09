"""Author Ariannna Delgado
Created on May 27, 2020
"""

"""Even or odd?"""

x = int(input("Enter a number: "))

if x==0:
    print(x,"the number is zero!")
elif x % 2 ==0:
    print(x, "is even")
else:
    print(x, "is odd")