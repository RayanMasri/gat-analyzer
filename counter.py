import json
from rapidfuzz import process, fuzz
import fitz
import cv2 as cv
import numpy as np


with open('./paragraphs-pages.json', 'r', encoding='utf8') as file:
    data = json.loads(file.read())

# fuzz.ratio(a, b)

paragraphs = list(map(lambda x: list(map(lambda y: y["name"], x["paragraphs"])), data))
paragraphs = [paragraph for _paragraph in paragraphs for paragraph in _paragraph]

print(f'Total paragraphs: {len(paragraphs)}')

duplicates = {}

def in_keys(keys, paragraph):
    for key in keys:
        ratio = fuzz.ratio(paragraph, key)
        if ratio > 99:
            return key
    
    return None

for paragraph in paragraphs:
    keys = list(duplicates.keys())

    key = in_keys(keys, paragraph)

    if key == None:
        duplicates[paragraph] = 1
    else:
        duplicates[key] += 1



    # if paragraph not in list(duplicates.keys()):
    #     duplicates[paragraph] = 1
    # else:
    #     duplicates[paragraph] += 1
    
print(f'Total duplicate paragraphs: {len(list(duplicates.keys()))}')

print(f'Top 10 highest occuring paragraphs:')

items = list(duplicates.items())
items = sorted(items, reverse=True, key=lambda e: e[1])

with open('duplicated.json', 'w', encoding='utf8') as file:
    file.write(json.dumps(items, ensure_ascii=False))