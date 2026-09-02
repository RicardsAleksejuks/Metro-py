yritykset = 0
login = "python"
salasana = "rules"

while yritykset < 5:
    SyotaL = input("Syötä login: ")
    SyotaS = input("Syötä salasana: ")
    if SyotaL == login and SyotaS == salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
if yritykset == 5:
    print("Pääsy evätty.")