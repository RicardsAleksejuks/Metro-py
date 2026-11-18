import os

import mariadb
from flask import Flask, jsonify

app = Flask(__name__)
app.json.sort_keys = False


@app.route("/kenttä/<icao>", methods=["GET"])
def airport_info(icao: str):
    password = os.getenv("DB_PASSWORD")
    if password is None:
        raise RuntimeError("Set the DB_PASSWORD environment variable.")

    connection = mariadb.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME", "ihmiset"),
        user=os.getenv("DB_USER", "dbuser"),
        password=password,
        autocommit=True,
    )
    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT ident, name, municipality FROM airport WHERE ident = ?",
                (icao.strip().upper(),),
            )
            airport = cursor.fetchone()
        finally:
            cursor.close()
    finally:
        connection.close()

    if airport is None:
        return jsonify({"error": "Airport not found"}), 404

    return jsonify(
        {
            "ICAO": airport[0],
            "Name": airport[1],
            "Municipality": airport[2],
        }
    )


if __name__ == "__main__":
    app.run(port=3000)