import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user='dbuser',
         password='qwerty',
         autocommit=True
         )

icao = input("Syötä Maan koodi: ").strip().upper()

def hae_lentokenttä(icao):
    sql = f"SELECT airport.type , COUNT(*) FROM airport WHERE airport.iso_country = '{icao}' GROUP BY airport.type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f"In the area under the code of '{icao}' there are: ")
        for row in tulos:
            print(f"type: {row[0]} amount: {row[1]}")
    return


hae_lentokenttä(icao)