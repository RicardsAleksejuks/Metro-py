Sukupuoli = input("Syötä Sukupuoli M/W:")
hemoglobiiniarvo = int(input("Syötä hemoglobiiniarvon g/l:"))

if Sukupuoli =="M" and hemoglobiiniarvo < 134:
    print("hemoglobiiniarvo alhainen")
elif Sukupuoli =="M" and 134 <= hemoglobiiniarvo <= 195:
    print("hemoglobiiniarvo normaali")
elif Sukupuoli =="M" and hemoglobiiniarvo > 195:
    print("hemoglobiiniarvo korkea.")

if Sukupuoli =="W" and hemoglobiiniarvo < 117:
    print("hemoglobiiniarvo alhainen")
elif Sukupuoli =="W" and 117 <= hemoglobiiniarvo <= 175:
    print("hemoglobiiniarvo normaali")
elif Sukupuoli =="W" and hemoglobiiniarvo > 175:
    print("hemoglobiiniarvo korkea.")