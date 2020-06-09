"""Author Ariannna Delgado
Created on May 27, 2020
"""

""" Enter a min number and a max number
    Display odd numbers between those numbers """
    

min = int(input("Please, enter a minimum number: "))
max = int(input("Please, enter a maximum number: "))




while min < max:
    if min >1:
        odd = (min+1)%2
        if odd == 0:
            print(min)
            min = min +1  
        else:    
            min = min +1
    else:
         min = min +1  
   
    
