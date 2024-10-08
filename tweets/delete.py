import http.client
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument('--tweetid', action="store", dest='tweetid', default='')

args = parser.parse_args()

AUTHORIZATION_HEADER = os.getenv("AUTHORIZATION_HEADER")

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