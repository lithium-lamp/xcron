import http.client
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--prompt', action="store", dest='prompt', default='')

args = parser.parse_args()

conn = http.client.HTTPConnection("llama", 11434)
payload = json.dumps({
  "model": "llama3.2",
  "prompt": f"{args.prompt}",
  "stream": False
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/generate", payload, headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")

json_data = json.loads(decoded_data)
response = json_data.get('response')

print(response + "\nGenerated with Llama3.2")

f = open("./socialplatforms/data.txt", "w")
f.write(response + "\nGenerated with Llama3.2")
f.close()