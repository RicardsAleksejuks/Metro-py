import random
Karvaus = random.randint(1, 10)

while True:
    syote = int(input("Arvaa luku 1-10: "))
    if syote == Karvaus:
        print("Oikein")
        break
    elif syote < Karvaus:
        print("Liian pieni arvaus")
    elif syote > Karvaus:
        print("Liian suuri arvaus")