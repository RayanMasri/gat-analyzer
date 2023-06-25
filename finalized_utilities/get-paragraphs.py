import pdfplumber, json, pyperclip

match = '( هذا النص مشابه لالختبار وليس هو الذي في االختبار )'

# FIXME:
# Page 465 failed to extract some paragraphs, even in previous pages
# All paragaraphs of model in page 317 weren't extracted

paragraphs = []
with pdfplumber.open(r'./original.pdf') as pdf:
    pages = len(pdf.pages)


    for index in range(pages):
        page = pdf.pages[index]
        text = page.extract_text()
        lines = list(map(lambda e: e[::-1], text.split('\n')))

        for i in range(len(lines)):
            if match in lines[i]:
                paragraphs.append({
                    "page": index,
                    "paragraph": lines[i - 1]
                })


        if index + 1 == pages:
            print(f'100% done ({pages}/{pages})')
            continue

        if index % 10 == 0:
            progress = round((index + 1) / pages * 100, 2)
            print(f'{progress}% done ({pages}/{index + 1})')

pyperclip.copy(json.dumps(paragraphs, ensure_ascii=False))
        


