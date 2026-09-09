import math

def laske_yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    yksikkohinta = hinta_euro / pinta_ala_m2
    return yksikkohinta

d1 = float(input("Syötä ekan pizzan halkaisija cm: "))
h1 = float(input("Syötä ekan pizzan hinta euroa: "))

d2 = float(input("Syötä toisen pizzan halkaisija cm: "))
h2 = float(input("Syötä toisen pizzan hinta euroa: "))

ykskkohinta_1 = laske_yksikkohinta(d1, h1)
ykskkohinta_2 = laske_yksikkohinta(d2, h2)

print(f"Ensimmäinen pizzan yksikköhinta on: {ykskkohinta_1:.2f} Eur/neliömetri")
print(f"Toinen pizzan yksikköhinta on: {ykskkohinta_2:.2f} Eur/neliömetri")

if ykskkohinta_1 < ykskkohinta_2:
    print("Ensimmäinen pizza antaa paremman vastineen.")
elif ykskkohinta_2 < ykskkohinta_1:
    print("Toinen pizza antaa paremman vastineen.")
else:
    print("Pizzoilla on sama yksikköhinta.")