# Program to check whether a username contains less than 10 characters

username = input("Enter your username here : ")

if(len(username)>10):
    print("Username can't have more then 10 characters")

else:
    print(username)