"""Author Arianna Delgado
Created on July 14, 2020
"""

"""Input and Output Functions"""
"""1. Write a program to input your name, and your marks in 3 subjects. 
2. Display the marks with your name, as shown in the sample output. 
3. Do not use more than 2 input statements in your program.
Sample Input: 
Enter your name: Anita
Enter your marks: 80,70,60"""

#Asks inputs.
name = input("Please, enter your name: ")
marks = list(input("Please, Enter your marks: ").split(","))

#Prints inputs
print( name, "your marks are", marks)




