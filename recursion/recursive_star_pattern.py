# Program to print a star pattern using recursion

n = int(input("Enter a number : "))

def starp(n):
    if(n==0):
        return
    print(n*"*")
    starp(n-1)

starp(n)