import random
import itertools
from math import ceil
from datetime import datetime

def one_pass_skip(iterator, rng):
    index1 = 1
    result = None
    while True:
        try:
            result = next(iterator)
        except StopIteration:
            return result

        r = rng.random()
        offset = max(ceil(r * index1 / (1.0 - r)), 1)
        iterator = itertools.islice(iterator, offset - 1, None)
        index1 += offset


now = datetime.now()
timestamp = datetime.timestamp(now)

file_name = r"./api/llama/prompts/data.txt"
result = one_pass_skip(open(file_name), random.Random(timestamp))

f = open("./api/llama/prompt.txt", "w")
f.write(result + "The result can only at most contain 250 characters.")
f.close()