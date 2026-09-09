import random

def noppa_heitto():
    return random.randint(1, 6)

while True:
    tulos = noppa_heitto()
    print(f"Heitto: {tulos}")
    if tulos == 6:
        print("Kutonen")
        break