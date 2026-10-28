class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0


def main():
    auto = Auto("ABC-123", 142)
    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka} km")


if __name__ == "__main__":
    main()