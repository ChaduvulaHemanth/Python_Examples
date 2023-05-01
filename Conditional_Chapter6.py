# a=4
# if (a>3):
#     print("The value of a is greater than 3")    
# elif (a>7):
#     print("The value of a is greater than 7")
# else:
#     print("The value is neither greater than 3 nor 7")

# age=int(input("Enter age"))

# if (age>25 and age<50):
#     print("yes")
# else:
#     print("No")

# a=2
# if (a is 2):
#     print("Yes")
# else:
#     print("No")

# a=[25,78,98]
# if(35 in a):
#     print("Yes")
# else:
#     print("No")

#### Practise Test

# Program-1

# a=int(input("Enter the a value:"))
# b=int(input("Enter the b value:"))
# c=int(input("Enter the c value:"))
# d=int(input("Enter the d value:"))

# if (a>b):
#     if (a>c and a>d):
#         print("a is greater")
#     elif(a>c and a<d):
#         print("d is greater")
#     else:
#         print("c is greater")   
# else:
#     if (b>c and b>d):
#         print("b is greater")
#     elif (b>c and b<d):
#         print("d is greater")
#     else:
#         print("c is greater")

# # Program-2

text=input("Enter the text\n")
if ("smart grid" in text):
    spam=True
elif("energy management" in text):
    spam=True
elif("electricty markets" in text):
    spam=True
elif("python with harry" in text):
    spam=True
else:
    spam=False

if (spam): 
    print("This text is spam")
else:
    print("This text is not spam")

### program-3

# marks=int(input("Enter the total marks\n"))

# if (marks>=90):
#    grade="Ex"
# elif (marks>=80):
#    grade="A"
# elif (marks>=70):
#     grade="B"
# elif (marks>=60):
#     grade="C"
# elif (marks>=50):
#     grade="D"
# else:
#     grade="F"

# print("The grade is", grade)