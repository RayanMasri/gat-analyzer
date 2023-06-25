import json
from rapidfuzz import process, fuzz
import fitz
import cv2 as cv
import numpy as np


with open('./paragraphs-pages.json', 'r', encoding='utf8') as file:
    data = json.loads(file.read())

search = input("Title: ")
include = input("Substring match? (y/n) ") == "y"
paragraphs = list(map(lambda e: e["paragraphs"], data))
paragraphs = [paragraph for model in paragraphs for paragraph in model]

paragraphs = list(filter(lambda e: search in e["name"] if include else fuzz.ratio(e["name"], search) > 90, paragraphs))

pages = list(map(lambda e: e["page"], paragraphs))
print(f'Found {len(pages)} instance(s) of "{search}"')
print(sorted(pages))

# print(pages)

pdffile = "models.pdf"
doc = fitz.open(pdffile)


for page_number in pages:
    page = doc.load_page(page_number - 1)  # number of page
    pix = page.get_pixmap()
    raw_bytes = pix.pil_tobytes('JPEG')
    cv2_image = cv.imdecode(np.frombuffer(bytearray(raw_bytes), dtype=np.uint8), cv.IMREAD_COLOR)
    cv.imshow(f'{search} - {page_number}', cv2_image)

    # print(cv2_image)
    # cv.imshow('images', cv2_image)
cv.waitKey(0)
cv.destroyAllWindows()
    # output = "outfile.png"
    # pix.save(output)
    # doc.close()
