import json

with open('paragraphs-pages.json', 'r', encoding='utf8') as file:
    models = json.loads(file.read())

with open('duplicated.json', 'r', encoding='utf8') as file:
    duplicates_json = json.loads(file.read())

duplicates = {}

for [key, value] in duplicates_json:
    duplicates[key] = value

maximum = 14

scores = []
for model in models:
    name = model["model"]
    paragraphs = list(map(lambda e: e["name"], model["paragraphs"]))

    total = sum(list(map(lambda e: duplicates[e], paragraphs)))

    score = None if len(paragraphs) == 0 else total / (maximum * len(paragraphs)) * 100
    
    scores.append([name, score])

scores = list(sorted(scores, key=lambda e:  e[1] if e[1] != None else -1, reverse=True))
for score in scores:
    print(score)
# print(scores)