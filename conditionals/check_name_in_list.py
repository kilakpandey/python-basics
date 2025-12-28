# Program to check whether a given name is present in a list

Top10students = ["Kilak", "Raman", "Krishna", "Ravi", "Divya", "Bhawna", "Samistha", "Arjun", "Prateek", "Aman"]

name = input("Enter your name to check if you are is top 10 or not : ")

if(name in Top10students):
    print("Hurray! you are among the top 10 rank holders")

else:
    print("Sorry you are not in the list")