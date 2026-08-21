leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat_yhteensa = (luodit * 13.3) + (naulat * 32 * 13.3) + (leiviskat * 20 * 32 * 13.3)

kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000

print(f"Massa nykymittojen mukaan: {kilogrammat}kg ja {grammat:.2f}g")