import pprint
import json
from fuzzywuzzy import fuzz
import pyperclip

with open('./paragraphs.json', 'r', encoding='utf8') as file:
    data = json.loads(file.read())

all_para = []
for item in data:
    all_para.append(item["paragraphs"])

all_para = [item for sublist in all_para for item in sublist]

organized = {}
print(fuzz.ratio('البرق والرعد', 'الرعد والبرق'))
for i in range(len(all_para)):
    item = all_para[i]

    organized[i] = {
        "names": [item],
        "occurences": 1
    }
    
    for j in range(len(all_para)):
        if j == i: continue

        if item == all_para[j]:
            organized[i]["occurences"] += 1
            continue

        if fuzz.ratio(item, all_para[j]) >= 80:
            organized[i] = {
                "names": organized[i]["names"] + [all_para[j]],
                "occurences": organized[i]["occurences"] + 1
            }

pyperclip.copy(json.dumps(organized, ensure_ascii=False))
            

#my_dict = {i:all_para.count(i) for i in all_para}
#
#my_dict = sorted(list(my_dict.items()), key=lambda x: x[1], reverse=True)

#for couple in my_dict:
    #print(f'{couple[0]} --- {couple[1]}')
#print(my_dict)
#pprint.pprint(my_dict)
