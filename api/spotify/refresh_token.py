import http.client
import json
from urllib.parse import urlencode, urlparse, parse_qs
import os
from dotenv import load_dotenv

load_dotenv("./.env")
load_dotenv("./api/spotify/.env")

CLIENTID = os.getenv("SPOTIFY_CLIENTID")
REFRESHTOKEN = os.getenv("SPOTIFY_REFRESH_TOKEN")


payload = {
    'grant_type': 'refresh_token',
    'refresh_token': REFRESHTOKEN,
    'client_id': CLIENTID
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

conn = http.client.HTTPSConnection("accounts.spotify.com")
conn.request("POST", "/api/token", urlencode(payload), headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")
access_data = json.loads(decoded_data)

access_token = access_data.get('access_token')
refresh_token = access_data.get('refresh_token')
expires_in = access_data.get('expires_in')

fulltext = f'SPOTIFY_ACCESS_TOKEN = "{access_token}"\n'
fulltext += f'SPOTIFY_REFRESH_TOKEN = "{refresh_token}"\n'
fulltext += f'SPOTIFY_TOKEN_EXPIRY_TIME = "{expires_in}"'

f = open("./api/spotify/.env", "w")
f.write(fulltext)
f.close()