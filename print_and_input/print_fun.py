"""Author Arianna Delgado
Created on May 15, 2020
"""


print()
print("Hello"*3)
print("This is a new line:")
print("This is a  different \n new line:")


a,b = 10,20

# can put anything inside'' and it will print it
print(a,b, sep=',')
print(a,b, sep='++++')


name = "John"
mark = 95.5

print("Name is",name,"mark are",mark)
print("Name is %s, mark are %.2f" %(name,mark))
print("Name is {}, mark are {}" .format(name,mark))
print("Name is {0}, mark are {1}" .format(name,mark))