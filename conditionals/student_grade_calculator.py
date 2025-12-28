# Program to calculate grade based on marks

marks = int(input("Enter your marks (out of 100) : "))

if marks < 0 or marks > 100:
    print("Invalid marks entered")

elif(marks<=100 and marks>90):
    print("Your grade is : Ex")

elif(marks<=90 and marks>80):
    print("Your grade is : A")

elif(marks<=80 and marks>70):
    print("Your grade is : B")

elif(marks<=70 and marks>60):
    print("Your grade is : C")

elif(marks<=60 and marks>=50):
    print("Your grade is : D")

elif(marks<50):
    print("Your grade is : F")

