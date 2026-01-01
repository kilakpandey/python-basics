# Program to find the sum of first n natural numbers using recursion

n = int(input("Enter a number : "))

def sum_of(n):
    if(n==1):
        return 1
    return sum_of(n-1)+n

print(sum_of(n))
