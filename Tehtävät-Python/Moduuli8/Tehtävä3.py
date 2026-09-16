import mysql.connector
from getpass import getpass
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user='dbuser',
         password='qwerty',
         autocommit=True
         )

koodi1 = input("Syötä ensimmäinen ICAO koodi: ")
koodi2 = input("Syötä toinen ICAO koodi: ")

cursoori = connection.cursor()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(sql, (koodi1,))
coords1 = cursor.fetchone()

cursor.execute(sql, (koodi2,))
coords2 = cursor.fetchone()

if coords1 is not None and coords2 is not None:
    distance = geodesic(coords1, coords2).km
    print(f"Distance: {distance:.2f} km")
else:
    print("Lentökenttä ei löydy")

cursor.close()
connection.close()