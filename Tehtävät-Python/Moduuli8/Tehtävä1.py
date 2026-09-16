import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user='dbuser',
         password='qwerty',
         autocommit=True
         )

icao = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()

def hae_lentokenttä(icao):
    sql = f"SELECT airport.name FROM airport WHERE ident = '{icao}';"
   
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(rivi)
    return


hae_lentokenttä(icao)