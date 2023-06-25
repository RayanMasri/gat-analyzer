import fitz, json, sys

doc = fitz.open('./original.pdf')

# keyword =""" يلع ينورتكلإ رابتخإ\nعقوم\nبسوحملا عيمجت """

# Matches for non-model pages
exceptions = [
    lambda lines: any(list("لحلا" in line for line in lines))
]

# Matches for model pages
matches = [
    lambda lines: any(list("011%" in line for line in lines))
]

with open('model-pages.json', 'r', encoding='utf8') as file:
    pages = json.loads(file.read())

def get_empty_neighbours(array, index):
    reverse_index = len(array) - 1 - index
    left = array[::-1][reverse_index + 1:]
    right = array[index + 1:]

    enum_left = list(map(lambda e: e[0], filter(lambda e: e[1] != '', enumerate(left))))
    enum_right = list(map(lambda e: e[0], filter(lambda e: e[1] != '', enumerate(right))))

    return [min(enum_left) if len(enum_left) > 0 else len(left), min(enum_right) if len(enum_right) > 0 else len(right)]

def is_page_model(index):
    text = doc.load_page(index).get_text()
    lines = list(map(lambda e: e.strip(), text.split('\n')))

    string_index = lines.index(str(index))
    neighbours = get_empty_neighbours(lines, string_index)

    anti_results = [exception(lines) for exception in exceptions]
    results = [match(lines) for match in matches]
    # print(results)

    if index in [911]:
        print(lines)
        print(results)
        print(neighbours)

    # If none of the results match a non-model, get outcome based on line neighbours
    # Otherwise, it's a non-model, so return False
    return True if any(results) else min(neighbours) >= 1 if not any(anti_results) else False


keyword = [' يلع ينورتكلإ رابتخإ', 'عقوم ', 'بسوحملا عيمجت ',]
keyword = '\n'.join(keyword)

# page number might be earlier in lines in model name pages than model content pages 

_matches = 0
_pages = []
for page in range(5, doc.page_count):
    

    if is_page_model(page):
        _pages.append(page)
        # print(page)
        # print(doc.load_page(page).get_text().split('\n'))
        _matches += 1

print(_pages)
print(list(pages.values()))
print(_matches)

# print(doc.load_page(7).get_text())
# print(doc.load_page(14).get_text())
# print(doc.load_page(15).get_text())
# print(doc.load_page(84).get_text())
# print('john')
# print(doc.load_page(83).get_text())
# print("84" in doc.load_page(84).get_text())
sys.exit()

def parse_text(text):
    lines = list(filter(lambda e: e != '', map(lambda e: e.strip(), text.split('\n'))))
    return len(lines)
    # if len(lines) <= 10:
        # print(text)
    # print()

matches = 0

for index in range(doc.page_count):
    page = doc.load_page(index)
    text = page.get_text()


    # print(str(index) in text)
    if parse_text(text) <= 10 and str(index) not in text:
        matches += 1

print(matches)

# page = doc.load_page(7)
# print(page.get_text())
# print(parse_text(page.get_text()))
# page = doc.load_page(14)
# print(page.get_text())
# print(parse_text(page.get_text()))

# page = doc.load_page(70)
# print(page.get_text())
# print(keyword in page.get_text())
# page = doc.load_page(84)
# print(f'"{page.get_text()}"')
# print(page.get_text().split('\n'))
# print(keyword in page.get_text())

# matches = 0 
# for index in range(doc.page_count):
#     page = doc.load_page(index)
#     text = page.get_text()
#     if keyword in text:
#         # print(text)
#         matches += 1

# print(matches)

# print(doc.page_count)
# with open('model-pages.json', 'r', encoding='utf8') as file:
#     pages = json.loads(file.read())

# items = list(pages.items())
# models = {}
# for i in range(len(items)):
#     [model, page] = items[i]
    

#     # models[]
#     print(item)
#     print(items[i + 1])

sys.exit()

skills = ['يظفللا رظانتلا ']

solution_keyword = "لحلا"
explanation_keyword = "ةقلاعلا"

first_line = ' ب أ '
second_line = ' د ـج '


page = doc.load_page(11)

text = page.get_text()

lines = text.split('\n')
skill_indices = {}
active_skill = None
active_question = {
    "solution": None,
    "explanation": None,
    "answers": {
        "a": None, "b": None, "c": None, "d": None
    }
}

def is_question_applicable():
    empty_values = list(filter(lambda e: e == None, list(active_question.values())))
    return len(empty_values) == 0

questions = []

for i in range(len(lines)):
    line = lines[i]
    skill = next((skill for skill in skills if skill == line), None)
    print(line)

    if skill != None:
        skill_indices[skills.index(skill)] = i
        active_skill = skill

    if active_skill != None:
        if solution_keyword in line:
            if is_question_applicable():
                questions.append(active_question)
                active_question = {
                    "solution": line,
                    "explanation" : None,
                    "answers": {
                        "a": None, "b": None, "c": None, "d": None
                    }
                }
            else:
                active_question["solution"] = line
            continue
        

        if explanation_keyword in line:
            if is_question_applicable():
                questions.append(active_question)
                active_question = {
                    "solution": None,
                    "explanation" : line,
                    "answers": {
                        "a": None, "b": None, "c": None, "d": None
                    }
                }
            else:
                active_question["explanation"] = line
            continue

        if first_line in line:
            [b, a] = line.split(first_line)
            active_question["answers"]["a"] = a
            active_question["answers"]["b"] = b

        if second_line in line:
            [d, c] = line.split(second_line)
            active_question["answers"]["d"] = d
            active_question["answers"]["c"] = c

        

        # print(line)
        # print(answer in line)

        # print(active_question)

if is_question_applicable():
    questions.append(active_question)

print(questions)
    