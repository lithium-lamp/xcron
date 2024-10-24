import psycopg2 # type: ignore
import http.client
import argparse
import os
from dotenv import load_dotenv

load_dotenv(".env")
load_dotenv("./socialplatforms/x/.env")

parser = argparse.ArgumentParser()

parser.add_argument('--tweetid', action="store", dest='tweetid', default='')

args = parser.parse_args()

AUTHORIZATION_HEADER = os.getenv("AUTHORIZATION_HEADER")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = http.client.HTTPSConnection("api.twitter.com")
headers = {
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION_HEADER
}

# DELETE post
conn.request("DELETE", f"/2/tweets/{args.tweetid}", '', headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

connection = psycopg2.connect(database=f"{DB_NAME}", user=f"{DB_USERNAME}", password=f"{DB_PASSWORD}", host="xcronpostgres", port=5432)

cursor = connection.cursor()

cursor.execute(f"DELETE FROM tweets WHERE tweetid = {args.tweetid};")

connection.commit()