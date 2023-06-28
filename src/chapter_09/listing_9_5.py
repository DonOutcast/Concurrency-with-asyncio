import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)
conn_info = "dbname=products user=lymondgl host=127.0.0.1"
db = psycopg2.connect(conn_info)


@app.route("/brands")
def brands():
    cur = db.cursor()
    cur.execute("""SELECT brand_id, brand_name FROM brand;""")
    rows = cur.fetchall()
    cur.close()
    return jsonify([{"brand_id": row[0], "brand_name": row[1]} for row in rows])

