pieni = None
suuri = None

while True:
    syote = input("Syötä Luku: ")
    if syote == "":
        break
    luku = float(syote)
    if pieni is None or luku < pieni:
        pieni = luku
    if suuri is None or luku > suuri:
        suuri = luku
print(f"Pienin Luku on: {pieni}")
print(f"Suurin Luku on: {suuri}")