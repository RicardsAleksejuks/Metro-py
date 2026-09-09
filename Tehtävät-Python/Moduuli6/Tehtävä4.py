
def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

luku_lista = [1, 2, 3]
tulos = laske_summa(luku_lista)
print(f"Kokonais Summa on: {tulos}")