"""Author Ariannna Delgado
Created on May 15, 2020
"""


"""Collection Assignment
1. Create a list of countries
2. Initialize the list with three countries
3. Add a country at the end of the list 
4. Remove a country by index 
5. Add a county in the middle of the list
6. Repeat operations with a set"""



#create a list
countries_list = ["Cuba", "US","Canada"]
print(countries_list)


#add a country
countries_list.append("Peru")
print(countries_list)


#remove by value another way
#countries_list.remove("Cuba")
#print(countries_list)

#remove by index, another way
#del countries_list[0]
#print(countries_list)

#remove at the position 
countries_list.pop(0)
print(countries_list)


#length for the middle of the list
countries_list_len = len(countries_list)
countries_list_len = int(countries_list_len /2)

#add in the middle of the list
countries_list.insert( countries_list_len, "Mexico")
print(countries_list)





#create set
countries_set = {"Brazil","Argentina", "France"}
print(countries_set)
#add a country to the set
countries_set.add("Peru")
print(countries_set)

#create a list and add the set to the list 
#to be able to perform more operations
list_of_countries = list(countries_set)

#eliminate the first element in the list
list_of_countries.pop(0)
print(list_of_countries)

#length for the middle of the list
countries_len = len(list_of_countries)
countries_len = int(countries_len/2)

#insert an element in the middle of the list
list_of_countries.insert(countries_len, "Italy")
print(set(list_of_countries))








