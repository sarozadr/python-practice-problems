"""Author Ariannna Delgado
Created on May 15, 2020
"""
# Integer Type:
# no need to define the type
a=5
b=10
c=15
print(a,b,c)


# Float Type:
x=2.1
y=-98.53
z=200.0
# For z to be a floating variable you need to add .0 at the end of the number
print(x,y,z)
# Print the type of x type is a function in Python
#In Python everything is an object in this case x is an object of class float
print(type(x))


#Complex Type:
d=5+1j
print(type(d))

#Binary Type:
#A Binary number start with 0B
e=0B1010
print(e)


#For Hexadecimal Type:
#An Hexadecimal number start with 0X
f= 0XFF
print(f)


#For Octal Type:
#An Hexadecimal number start with 0O
o= 0O11
print(o)


#Boolean Type
#Two values true or false
w= True
print(type(w))
print(9>8)




#Type conversion Function
#How to convert a type into another
'''I will use the function type (int) 
in front of the values that I like to make the conversion
and it will convert the number or string to integer numbre'''
h=int(x)
print(h)
print(type(h))

n= float("33.3")
print(type(n))
print(n)

b= bin(10)
print(b)
print(bin(10))
print(hex(10))
print(oct(10))




