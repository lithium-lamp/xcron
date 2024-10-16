import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_BEARER = os.getenv("SPOTIFY_ACCESS_TOKEN")

conn = http.client.HTTPSConnection("api.spotify.com")

payload = ''

headers = {
    'Authorization': f"Bearer {SPOTIFY_BEARER}"
    }

conn.request("GET", f"/v1/me/top/tracks?time_range=short_term&limit=3", payload, headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")
#print(decoded_data)

json_data = json.loads(decoded_data)
all_items = json_data.get('items')

fulltext = "My top 3 tracks right now 😁🎶:"

for i in range(0, 3):
    currentitem = all_items[i]

    artists = currentitem.get('artists')

    fulltext += "\n" + currentitem.get('name') + " - " + artists[0].get('name')

    for j in range(1, len(artists)):
        fulltext += ", " + artists[j].get('name')
    
    fulltext += "\n"
    #fulltext += "\n" + currentitem.get('external_urls').get('spotify')

print(fulltext)

if len(fulltext) > 280:
    print("Too long")
    exit(1)

f = open("./socialplatforms/data.txt", "w")
f.write(fulltext)
f.close()