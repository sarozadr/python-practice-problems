"""Author Ariannna Delgado
Created on May 15, 2020
"""

"""Calculate how many unique elements in L1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9]"""

l1 = [2,3,4,5,8,4,3,5,2,1,8,8,6,3,4,5,7,9]
l3 = []
count = 0

#used sort method to organize the numbers
l1.sort()


#used set because they eliminate duplicate and 
#converted back to a list for easy manipulation
set1 = set(l1)
l2 = list(set1)

#a = len(l1)
#b = len(l2)

#nested loop to compare elements in each list
#for i in range(b):
    #for j in range(a):
        #compare element in the l1 with the l2
        #if there are equal a count variable will increase
        #if l2[i] == l1[j]:
            #count = count + 1
        #here we ask if the variable count is grater than 1 
        #if grater it mean there duplicates in the list 
        #reset count variable to zero and get out of the inner loop    
        #if count > 1:
            #count = 0
            #break
        #if this is true means we reach the end of the l1 and 
        #the count variable is not grater that one 
        #which means the number is unique and I added to a new list
        #if  j == a-1:
            #l3.append(l2[i])
            #count = 0

c = len(l2)
print("There are only " + str(c) + " unique elements in " + str(l1))
print(l2)







  
"""After looking at the result of first step , print odd elements only."""
l4 = []
#a for loop to check the remainder in of each element in the list
for k in l2:
    if k % 2 == 1:
        l4.append(k)
print("Odd elements are: ", l4)



"""For string str1 replace “three” with “3” 
and save all words in some list where  all the character should be capital."""
str1 = "hello python three"

#replaced "there" for 3
str1 = str1.replace("three", "3")
#print(str1)

#capitalized each letter
str1 = str1.upper()
#print(str1)

#saved words in list1 representing 3 spaces in list2 
list1 = []
list1.append(str1[0:5])
list1.append(str1[5:12])
list1.append(str1[13:14])
print(list1)

#saved words in list2 all letter together representing one space in the list2
#list2 = []
#list2.append(str1[0:14])
#print(list2)


#saved words in list3 all letter separated representing one space each in the list2
#list3 = list(str1)
#print(list3)



"""Also explain in your own words that how tuple are immutable(using list L1). (BONUS QUESTION)"""
""" Tuple are an ordered collection of items and  are unchangeable you can not remove items from tuple"""





















        