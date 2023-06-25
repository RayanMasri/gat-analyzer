import json, fitz, os

with open('paragraphs-pages.json', 'r', encoding='utf8') as file:
    data = json.loads(file.read())



os.remove('./organized.pdf')

doc = fitz.open()
page = doc.new_page(-1,
                    width = 595,
                    height = 842)

page.insert_textbox((50, 50, 100, 100), "bye", align=fitz.TEXT_ALIGN_CENTER, fontsize=50, color=(0, 0, 0))
doc.save('organized.pdf')
