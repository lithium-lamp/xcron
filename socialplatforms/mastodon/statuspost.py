import psycopg2 # type: ignore
import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv(".env")
load_dotenv("./socialplatforms/mastodon/.env")

MASTODON_ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = http.client.HTTPSConnection("mastodon.social")
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + MASTODON_ACCESS_TOKEN
}

f = open("./socialplatforms/data.txt", "r")

# POST body data
payload = json.dumps({
"status": f.read()
})

f.close()

conn.request("POST", "/api/v1/statuses", payload, headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")
#print(decoded_data)

statusdata = json.loads(decoded_data)

content = statusdata.get('content')
statusid = statusdata.get('id')

connection = psycopg2.connect(database=f"{DB_NAME}", user=f"{DB_USERNAME}", password=f"{DB_PASSWORD}", host="xcronpostgres", port=5432)

cursor = connection.cursor()

cursor.execute(f"INSERT INTO mastodonstatus(statusid, content) VALUES ('{statusid}', '{content}');")

connection.commit()