Kysyy = (input("Syötä hyttiluokan (LUX, A, B, C): "))
if Kysyy == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif Kysyy == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif Kysyy == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif Kysyy == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")