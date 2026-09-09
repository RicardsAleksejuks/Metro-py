Kysyy = int(input("Syötä Kokonaisluku: "))

if Kysyy < 2:
    print(f"Luku {Kysyy} ei ole alkuluku.")
else:
    for i in range(2, Kysyy):
        if Kysyy % i == 0:
            print(f"Luku {Kysyy} ei ole alkuluku.")
            break
    else:
        print(f"Luku {Kysyy} on alkuluku.")