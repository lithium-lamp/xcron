import http.client
import json
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

AUTHORIZATION_HEADER = os.getenv("AUTHORIZATION_HEADER")

conn = http.client.HTTPSConnection("api.twitter.com")
headers = {
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION_HEADER
}

f = open("./tweets/data.txt", "r")

# POST body data
payload = json.dumps({
"text": f.read()
})

f.close()

conn.request("POST", "/2/tweets", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
