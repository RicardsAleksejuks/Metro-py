while True:
    tuumi = float(input("Syötä Tuumi:"))
    if tuumi < 0:
        break
    cm = tuumi *2.54
    print(cm)