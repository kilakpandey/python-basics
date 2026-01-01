# Program to find the greatest of three numbers using a function

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>b and c>a):
        return c

a = int(input("Enter a no. : "))
b = int(input("Enter a no. : "))
c = int(input("Enter a no. : "))

print(f"The greates value is {greatest(a,b,c)}")
