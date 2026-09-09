luvut = []

while True:
    kysyy = input("Syötä luku: ")
    if kysyy == "":
        break
    luku = int(kysyy)
    luvut.append(luku)
luvut.sort(reverse=True)
print(luvut[:5])