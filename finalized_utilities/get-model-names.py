import json, fitz

statics = [
    "يلع ينورتكلإ رابتخإ",
    "عقوم",
    "بسوحملا عيمجت",
    "011%"
]

replaceables = [
    'ـ',
    '011%',
    '011 %',
]

with open('./model-pages.json', 'r') as file:
    pages = json.loads(file.read())

#TODO: Use PDF Plumber
doc = fitz.open('./original.pdf')
# x = "دهلاوةي011%"

# print(x.replace(''))
# x.replace('')

def clean_line(line):
    for replaceable in replaceables:
        line = line.replace(replaceable, '')

    return line

for page in pages:
    text = doc.load_page(page).get_text()
    statics_copy = statics.copy()
    statics_copy.append(str(page))

    lines = list(filter(lambda e: e not in statics_copy and e != "", map(lambda e: e.strip(), text.split('\n'))))
    lines = list(map(clean_line, lines))
    print(lines)
    print(page)
    # print(text)
    # for line in lines:
        # print(f'"{line.strip()}"')