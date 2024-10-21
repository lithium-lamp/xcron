import http.client
import os
import json
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("NEWSDATA_TOKEN")

conn = http.client.HTTPSConnection("newsdata.io")

payload = ''
headers = {}

conn.request("GET", f"/api/1/latest?apikey={TOKEN}&country=se&category=science,top,politics,technology,world&language=en", payload, headers)
res = conn.getresponse()

data = res.read()

decoded_data = data.decode("utf-8")

news_data = json.loads(decoded_data)
results_arr = news_data.get('results')
 
fulltext = "Pick ONE of the following articles below and return the title of it along with the corresponding link.\n"

for i in range(0, len(results_arr)):
    title = results_arr[i].get('title')
    description = results_arr[i].get('description')
    link = results_arr[i].get('link')
    fulltext += f"Title: '{title}'\nDescription: '{description}'\nLink: '{link}'"

f = open("./api/llama/prompt.txt", "w")
f.write(fulltext)
f.close()