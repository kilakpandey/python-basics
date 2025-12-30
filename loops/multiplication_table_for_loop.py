# Program to print the multiplication table of a given number using a for loop

n = int(input("Enter the no. of which the tabe is desired : "))


for i in range(1,11):
    print(f"{n}x{i} = {n*i}")
