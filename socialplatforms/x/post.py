import psycopg2 # type: ignore
import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv(".env")
load_dotenv(".socialplatforms/x/.env")

AUTHORIZATION_HEADER = os.getenv("AUTHORIZATION_HEADER")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = http.client.HTTPSConnection("api.twitter.com")
headers = {
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION_HEADER
}

f = open("./socialplatforms/data.txt", "r")

# POST body data
payload = json.dumps({
"text": f.read()
})

f.close()

conn.request("POST", "/2/tweets", payload, headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")
#print(decoded_data)

tweetdata = json.loads(decoded_data)
data = tweetdata.get('data')
tweettext = data.get('text')
tweetid = data.get('id')

connection = psycopg2.connect(database=f"{DB_NAME}", user=f"{DB_USERNAME}", password=f"{DB_PASSWORD}", host="xcronpostgres", port=5432)

cursor = connection.cursor()

cursor.execute(f"INSERT INTO tweets(tweetid, tweettext) VALUES ('{tweetid}', '{tweettext}');")

connection.commit()