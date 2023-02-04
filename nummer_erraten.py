import random

guess = input("Welche Nummer denkst du ist es?: ")

if not guess.isdigit() or int(guess) not in range(1, 11):
    print("Die Schätzung muss eine Zahl von 1 bis 10 sein.")
    exit()

number = random.randint(1,10)

if int(guess) == number:
    print(f"Korrekt! Die Nummer war {number}!")
else:
    print(f"Falsch, die Nummer war {number} 😢")
    