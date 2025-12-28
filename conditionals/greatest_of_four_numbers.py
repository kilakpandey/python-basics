# Program to find the greatest of four numbers entered by the user

a = int(input("Enter number 1 : "))

b = int(input("Enter number 2 : "))

c = int(input("Enter number 3 : "))

d = int(input("Enter number 4 : "))

if(a>b and a>c and a>d):
    print("Greatest Value is : ",a)
    

elif(b>a and b>c and b>d):
    print("Greatest Value is : ",b)
    

elif(c>a and c>b and c>d):
    print("Greatest Value is : ",c)
    
elif(d>a and d>c and d>b):
    print("Greatest Value is : ",d)
    