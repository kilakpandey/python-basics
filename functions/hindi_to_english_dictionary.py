# Program to translate Hindi words to English using a dictionary

D = {
    'Pratham':"First",
    "Laal":"Red",
    "Parvat":"Mountain",
    "Rangeen":"Colorfull",
    "Kursi": "Chair",
    "Pyar": "Love",
    "Kutta": "Dog"
}

word = input("Enter your word : ")

D.setdefault(word, "Word not found")

print(D[word])