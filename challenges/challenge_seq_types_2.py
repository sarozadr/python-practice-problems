"""Author Arianna Delgado
Created on May 15, 2020
"""

"""Input a list of strings “str_list” separated by spaces and a character “ch”.
For each unique string in str_list, count the number of occurrences of the character “ch” in that
string and append the string that many times to the answer list and Print the answer list."""




str_list = [ str(x) for x in (input("Please, enter a list of strings, separated by spaces: ").split())]
ch = input("Please enter character: ")

print(str_list)

l = len(str_list) 

list2 =[]



#loop through the list of words from  position 0 to l-1
for i in range(0,l):
    var = str_list[i].count(ch)                                  
    for j in range(0,var):    
        list2.append(str_list[i])
          
                  

print(list2)

