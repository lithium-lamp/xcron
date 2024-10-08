import subprocess
import http.client
import json
import os
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("MARKETSTACK_TOKEN")

conn = http.client.HTTPSConnection("api.marketstack.com")
payload = ''
headers = {}
conn.request("GET", f"/v1/eod/latest?access_key={KEY}&symbols=AAPL,GOOGL,TSLA,AMZN,NFLX,META,NVDA", payload, headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")

market_data = json.loads(decoded_data)
data_arr = market_data.get('data')

fulltext = "Market changes"

for i in range(0, len(data_arr)):
    open = data_arr[i].get('open')
    close = data_arr[i].get('close')
    symbol = data_arr[i].get('symbol')
    ratio = (close/open - 1) * 100
    ratio = round(ratio, 2)

    text = ""

    if ratio >= 0:
        text += "+"

    text += str(ratio) + "%"

    fulltext += "\n" + symbol + " " + text

f = open("./tweets/data.txt", "w")
f.write(fulltext)
f.close()