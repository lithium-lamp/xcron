import psycopg2 # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

connection = psycopg2.connect(database=f"{DB_NAME}", user=f"{DB_USERNAME}", password=f"{DB_PASSWORD}", host="xcronpostgres", port=5432)

cursor = connection.cursor()

list = os.listdir("/code/migrations/down")

list.sort(reverse=True)

for filename in list:
    f = open(f"/code/migrations/down/{filename}", "r")
    sql = f.read()
    f.close()

    cursor.execute(sql)

connection.commit()