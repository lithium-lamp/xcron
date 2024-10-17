import psycopg2 # type: ignore
import http.client
import argparse
import os
from dotenv import load_dotenv

load_dotenv(".env")
load_dotenv("./socialplatforms/mastodon/.env")

parser = argparse.ArgumentParser()

parser.add_argument('--statusid', action="store", dest='statusid', default='')

args = parser.parse_args()

MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = http.client.HTTPSConnection("mastodon.social")
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + MASTODON_ACCESS_TOKEN
}

conn.request("DELETE", f"/api/v1/statuses/{args.statusid}", '', headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")

connection = psycopg2.connect(database=f"{DB_NAME}", user=f"{DB_USERNAME}", password=f"{DB_PASSWORD}", host="xcronpostgres", port=5432)

cursor = connection.cursor()

cursor.execute(f"DELETE FROM mastodonstatus WHERE statusid = {args.statusid};")

connection.commit()