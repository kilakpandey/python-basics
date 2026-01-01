# Program to convert Celsius to Fahrenheit using a function
# Formula: F = C × 9/5 + 32

c = int(input("Enter the temp.(in Clecius) : "))

def conversion(c):
   return c * 9/5 + 32

print(f"{conversion(c)}°F")