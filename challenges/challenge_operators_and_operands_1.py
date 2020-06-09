"""Author Ariannna Delgado
Created on May 28, 2020
"""



math,phys,comp,engl,art = [int(x) for x in (input("Please, enter the score of each subject following the order Math, Physics, Computer, English, Art: Separated by comma: " ).split(',')) ]

avg = (math + phys + comp + engl + art)/5


if (avg >= 90):
    print("Grade is 'A'")
elif (avg >= 80 and avg< 90):
    print("Grade is 'B' ")
elif (avg >= 70 and avg< 80):
    print("Grade is 'C' ")
elif (avg >= 60 and avg< 70):
    print("Grade is 'D' ")
else:
    print("Garde is 'F'")
    

