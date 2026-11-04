
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, kilometrimaara, autot):
        self.nimi = nimi
        self.kilometrimaara = kilometrimaara
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi}")
        print("-" * 65)
        print(f"{'Rekisteri':<15}{'Huippunopeus':<18}{'Nopeus':<15}{'Matka (km)':<15}")
        print("-" * 65)

        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<15}"
                f"{auto.huippunopeus:<18}"
                f"{auto.nopeus:<15}"
                f"{auto.kuljettu_matka:<15.1f}"
            )

        print("-" * 65)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.kilometrimaara:
                return True

        return False


autot = []

for i in range(10):
    rekisteritunnus = f"ABC-{i + 1}"
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

print(f"\nKilpailu päättyi! Aikaa kului {tunnit} tuntia.")

kilpailu.tulosta_tilanne()
