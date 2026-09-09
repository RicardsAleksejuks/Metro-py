
def galoonit_litroiksi(galoonit):
    return galoonit * 3.785

while True:
    syote = float(input("Syötä Galooni määrä: "))
    if syote <= 0:
        break
    litra = galoonit_litroiksi(syote)
    print(f"{syote} Galoonia on {litra:.2f} Litraa.")