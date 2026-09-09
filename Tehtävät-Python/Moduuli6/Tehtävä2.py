import random

def arvo_luku(max_arvo):
    return random.randint(1, max_arvo)

maksimi = int(input("Syötä Tahkojen Arvo: "))
while True:
    saatu = arvo_luku(maksimi)
    print(saatu)
    if saatu == maksimi:
        print(f"Suurin Luku on: {saatu}")
        break