import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', action="store", dest='name', default='')
parser.add_argument('--db', action="store", dest='db', default='')

args = parser.parse_args()

list = os.listdir("./migrations/up")

number = "000001"

largestfilename = ""

if len(list) != 0:
    largestfilename = list[len(list) - 1]
    number = largestfilename[:6]
    number = int(number) + 1
    number = f"{number:06d}"

filename = args.name
db = args.db

f = open(f"./migrations/down/{number}_{filename}_{db}.sql", "w")
f.write("")
f.close()

f = open(f"./migrations/up/{number}_{filename}_{db}.sql", "w")
f.write("")
f.close()