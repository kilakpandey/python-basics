# Program to check whether a post mentions Harry

post = input("Enter your post : ")

if("Harry".lower() in post.lower()):
    print("This post is talking about Harry")

else:
    print("This post is not talking about Harry")
