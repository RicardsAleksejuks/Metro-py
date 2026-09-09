import random

arpaa = int(input("Syötä arpakuutioiden määrä: "))
summa = 0

for i in range(arpaa):
    heitto = random.randint(1, 6)
    summa += heitto
print(f"Silmälukujen summa on: {summa}")