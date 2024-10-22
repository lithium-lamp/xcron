import http.client
import os
import json
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("NEWSDATA_TOKEN")

conn = http.client.HTTPSConnection("newsdata.io")

payload = ''
headers = {}

conn.request("GET", f"/api/1/latest?apikey={TOKEN}&country=se&category=science,top,politics,technology,world&language=en&size=1", payload, headers)
res = conn.getresponse()

data = res.read()

decoded_data = data.decode("utf-8")

news_data = json.loads(decoded_data)
results_arr = news_data.get('results')
 
fulltext = f"The article of the day is:\n{results_arr[0].get('title')}:\n{results_arr[0].get('link')}"

f = open("./socialplatforms/data.txt", "w")
f.write(fulltext)
f.close()
