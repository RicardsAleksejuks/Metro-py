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
    auto = Auto("ABC-123", 142)
    auto.nopeus = 60
    auto.kuljettu_matka = 2000
    auto.kulje(1.5)
    print(f"Kuljettu matka: {auto.kuljettu_matka} km")


if __name__ == "__main__":
    main()