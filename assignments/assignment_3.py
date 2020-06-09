"""Author Ariannna Delgado
Created on May 27, 2020
"""

"""Grading Application"""

"""1. Three subjects (math, physics, chemistry)
2. Check if student pass exam: >= 35/100
3. If the student fails any exam the program will stop!
4. If the student pass the exams calculate the average of 3 subjects
5. If the average of the 3 subject is 
<=59 grade = C
<=69 grade = B
>69  grade = A"""


#Declares variables, receives input and casts the input to an integer.
math = int(input("Enter Math grade of student please: "))
physics =  int(input("Enter Physics grade of student please: "))
chemistry =  int(input("Enter Chemistry grade of student please: "))


#Checks conditions.
if math >= 35:
    print("Student passed the Math exam!")
else:
    print("Student did not pass the the Math exam.")
if physics >= 35:
    print("Student passed the Physics exam!")
else:
    print("Student did not pass the the Physics exam.")
if chemistry >= 35:
    print("Student passed the Chemistry exam!")
else:
    print("Student did not pass the the Chemistry exam.")

#Calculates average.
avg = (math + physics + chemistry)/3

#Checks conditions to print answer.
if avg <= 59:
    print("Student got a 'C' grade")
elif avg <= 69:
    print("Student got a 'B' grade")
else:
    print("Student got a 'A' grade")       
    
    
    
    
    
    
