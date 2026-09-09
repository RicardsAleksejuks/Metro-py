
lentoasemat = {}

while True:
    print("Valitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")

    valinta = input("Valintasi (1-3): ").strip()

    if valinta == "1":
        icao = input("Syötä ICAO-koodi: ").strip() .upper()
        nimi = input("Syötä Lentoaseman nimi: ").strip()

        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) lisätty.")
    elif valinta == "2":
        icao = input("Syötä Haettava ICAO-koodi: ").strip() .upper()

        if icao in lentoasemat:
            print(f"Lentoasema {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "3":
        print("Ohjelma Lopetetaan.")
        break
    else:
        print("Virheellinen valinta, yritä uudelleen.")