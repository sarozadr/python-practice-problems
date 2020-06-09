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


#Creates and initializes a list of countries.
countries_list = ["Cuba","US","Canada"]
print(countries_list)

#Adds a country to this list.
countries_list.append("Peru")
print(countries_list)

#Removes country by index.
del countries_list[1]
print(countries_list)

#Calculates length of this country list divided by two.
countries_list_len = len(countries_list)
countries_list_len = int(countries_list_len /2)

#Adds a country in the middle of this list.
countries_list.insert( countries_list_len, "Mexico")
print(countries_list)

#Creates and initializes a set.
countries_set = {"Brazil","Argentina", "France"}
print(countries_set)

#Adds a country to this set.
countries_set.add("Peru")
print(countries_set)

#Casts the set to a list to perform more operations.
list_of_countries = list(countries_set)

#Removes country by index.
del list_of_countries[1]
print(list_of_countries)

#Calculates length of this country list divided by two.
countries_len = len(list_of_countries)
countries_len = int(countries_len/2)

#Inserts an element in the middle of this list and casts this list to a set.
list_of_countries.insert(countries_len, "Italy")
print(set(list_of_countries))








