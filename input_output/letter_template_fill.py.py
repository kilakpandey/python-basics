a = input("Enter your name : ")

b = input("Enter the date : ")

print(f"Dear {a}, \nYou are selected! \n{b}") # a simple code to format a letter if the data is given

letter = '''Dear |<Name>|,
You are selected!
|<Date>|'''

print(letter.replace("|<Name>|","Kilak Pandey").replace("|<Date>|","24-12-2025")) # a simple code to format a letter if the data is already provided
