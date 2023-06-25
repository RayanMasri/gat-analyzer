# FIXME: This utility extracts pages only excluding names, they are not extracted with the page number

import fitz, json, sys, pyperclip

doc = fitz.open('./original.pdf')

# SUPER SPECIAL EXCEPTIONS: 333, HAS INVISIBLE EMBEDDED TEXT

# Matches for non-model pages
exceptions = [
    lambda lines: any(list("لحلا" in line for line in lines))
]

# Matches for model pages
matches = [
    lambda lines: any(list("011%" in line for line in lines))
]

# with open('model-pages.json', 'r', encoding='utf8') as file:
#     pages = json.loads(file.read())

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

    methods = [
        "Matched through model special matches",
        "Cancelled through non-model special matches",
        "Matched through neighbouring empty lines",
        "Cancelled through neighbouring empty lines"
    ]

    outcomes = [any(results), any(anti_results), min(neighbours) >= 1]

    outcome_index = next((outcome for outcome in list(enumerate(outcomes)) if outcome[1]), None)

    final_outcome = methods[-1];
    if outcome_index != None:
        final_outcome = methods[outcome_index[0]]

    # If none of the results match a non-model, get outcome based on line neighbours
    # Otherwise, it's a non-model, so return False
    return [
        True if any(results) else min(neighbours) >= 1 if not any(anti_results) else False,
        final_outcome
    ]


# page number might be earlier in lines in model name pages than model content pages 

pages = []
reasons = {}
for page in range(5, doc.page_count):

    [result, reason] = is_page_model(page)

    if reason not in list(reasons.keys()):
        reasons[reason] = 1
    else:
        reasons[reason] += 1


    if result:
        pages.append(page)


print(f'Successfully found {len(pages)} model page(s)')
for [reason, amount] in list(reasons.items()):
    initial = reason.split(' ')[0]
    rest = ' '.join(reason.split(' ')[1:])
    print(f'{initial} {amount} page(s) {rest}')

pyperclip.copy(json.dumps(pages, ensure_ascii=False))


