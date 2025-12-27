# Program to demonstrate that int 18 and string '18' are treated as different values in a set


s = set()

s.add(18)

s.add('18')

print(s)