import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        self.nopeus = max(0, min(self.nopeus, self.huippunopeus))

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä


def main():
    autot = []
    for numero in range(1, 11):
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(f"ABC-{numero}", huippunopeus))

    while not any(auto.kuljettu_matka >= 10_000 for auto in autot):
        for auto in autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    otsikot = ("Rekisteritunnus", "Huippunopeus (km/h)", "Nopeus (km/h)", "Kuljettu matka (km)")
    rivit = [
        (auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, f"{auto.kuljettu_matka:.1f}")
        for auto in autot
    ]
    sarakeleveydet = [max(len(str(rivi[i])) for rivi in [otsikot, *rivit]) for i in range(len(otsikot))]

    print(" | ".join(str(otsikko).ljust(sarakeleveydet[i]) for i, otsikko in enumerate(otsikot)))
    print("-+-".join("-" * leveys for leveys in sarakeleveydet))
    for rivi in rivit:
        print(" | ".join(str(arvo).ljust(sarakeleveydet[i]) for i, arvo in enumerate(rivi)))


if __name__ == "__main__":
    main()