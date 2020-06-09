"""Author Ariannna Delgado
Created on May 15, 2020
"""

s="You are awesome"
print(s)

s1= """You are 
the created of
 your destiny"""
 
print(s1)

print(s[0])

print(s*3) 

#the length of s
print(len(s))
#Slicing an string, it does not include the last element 
print(s[0:5])
#Start from zero to the end
print(s[0:15])
#-1 always represent the last element (-3) the third position from the back of the array
#does not include the last position of the array
print(s[-3:-1])
#count the first element that printed 1,2 and move to next one to print,
#every other character
print(s[0:15:2])

#Steps in Slicing
#this represent from the end (15) to the beginning (::) and -1 represent in reverser order
print(s[15::-1])

#from back to beginning but does not include the position (0); -1 represent in reverse order
print(s[15:0:-1])
""" Please, can you explain why it does not include the value in the position zero?  """


#eliminate spaces at the beginning and at the end
print(s.strip())
#eliminate the left space
print(s.lstrip())
#eliminate the right space
print(s.rstrip())

#the first position of the letters
print(s.find("aw"))
print(s.find("w"))
#first number where you want to start the search; last number where you want the search to stop
#if it can not find the value position will return -1
print(s.find("aw"),0,len(s))

#count how many time is (e) in the string
print(s.count("e"))
#replace an string
print(s.replace("awesome", "super",))

#capital Letters
print(s.upper())
print(s.lower())
print(s.title()) 

