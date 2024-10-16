import psycopg2 # type: ignore
import http.client
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(".env")
load_dotenv("./api/leetcode/.env")

COOKIE = os.getenv("LEETCODE_COOKIE")
CORS = os.getenv("LEETCODE_CORS")
username = os.getenv("LEETCODE_USERNAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = http.client.HTTPSConnection("leetcode.com")

s1 = 'query {\n'
s2 = 'recentSubmissionList(username: \"{username}\", limit: 20)'.format(username=username)
s3 = """{
        titleSlug
        statusDisplay
    }
}
"""

payload = json.dumps({
    "query": s1 + s2 + s3
    })

headers = {
    'Content-Type': 'application/json',
    }

conn.request("POST", "/graphql", payload, headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")

json_data = json.loads(decoded_data)

itemdata = json_data.get('data')
recentsubmissions = itemdata.get('recentSubmissionList')

titleSlug = ""

for i in range(0, 20):
    if recentsubmissions[i].get('statusDisplay') == "Accepted":
      titleSlug = recentsubmissions[i].get('titleSlug')
      break

s1 = 'query {\n'
s2 = 'submissionList(offset: 0, limit: 1, questionSlug: \"{slug}\")'.format(slug=titleSlug)
s3 = """{
  submissions {
    lang
    timestamp
    runtime
    memory
    }
  }
"""
s4 = 'question(titleSlug: \"{slug}\")'.format(slug=titleSlug)
s5 = """{
        title
        difficulty
    }
}
"""

payload = json.dumps({
    "query": s1 + s2 + s3 + s4 + s5
    })

headers = {
    'Content-Type': 'application/json',
    'Cookie': f"LEETCODE_SESSION={COOKIE}; csrftoken={CORS}"
    }

conn.request("POST", "/graphql", payload, headers)
res = conn.getresponse()
data = res.read()

decoded_data = data.decode("utf-8")

json_data = json.loads(decoded_data)
data = json_data.get('data')
submission = data.get('submissionList').get('submissions')[0]

lang = submission.get('lang')
timestamp = submission.get('timestamp')
runtime = submission.get('runtime')
memory = submission.get('memory')

question = data.get('question')

title = question.get('title')
difficulty = question.get('difficulty')

time = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')

fullstring = f"Leetcode {difficulty} difficulty problem solved {time} using {lang}.\n"
fullstring += f"'{title}' was solved with {runtime} runtime and required {memory}s of memory."

f = open("./socialplatforms/data.txt", "w")
f.write(fullstring)
f.close()

connection = psycopg2.connect(database=f"{DB_NAME}", user=f"{DB_USERNAME}", password=f"{DB_PASSWORD}", host="xcronpostgres", port=5432)

cursor = connection.cursor()

EXECSTRING = "INSERT INTO solvedproblems(id, difficulty, completed_time_unix, lang, title, runtime, memory)"
EXECSTRING += f" VALUES ('{titleSlug}', '{difficulty}', {int(timestamp)}, '{lang}', '{title}', '{runtime}', '{memory}');"

cursor.execute(f"{EXECSTRING}")

connection.commit()