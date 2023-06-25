import arabic_reshaper
from bidi.algorithm import get_display
import pdfplumber
import json
import pprint
import time
import pyperclip

# todo:
# count all essays

# verbal analogy
# contextual error
# sentence completion

with open('./model_intermissions.json', 'r', encoding='utf8') as file:
    models = json.loads(file.read())

#models = dict(list(models.items())[:7])

def is_question(text):
    splitted = list(map(lambda e: e.strip(), text.split(':')))

    if len(splitted) != 2 and text.count(':') != 1:
        return False
    
    bare = splitted[0].count(' ') == 0 and splitted[1].count(' ') == 0
    prohibited = ['العالقة', 'الحل']
    mistaken = splitted[0] in prohibited or splitted[1] in prohibited
    
    return bare and not mistaken
    
def extract_text(page):
    content = page.extract_text()
    content = '\n'.join(map(lambda e: e[::-1], content.split('\n')))
    return content




def find(lst, match):
    return [i for i, x in enumerate(lst) if x==match]

start = time.time()
with pdfplumber.open(r'models.pdf') as pdf:
    end = time.time()
    print(f'Opened in {round(end - start, 2)}s')
    chunks = []

    model_values = list(models.values())
    for i in range(1, len(models)):
        chunks.append(pdf.pages[model_values[i - 1] + 1:model_values[i]])

    match = "( هذا النص مشابه لالختبار وليس هو الذي في االختبار )"



    all_para = []
    total = 0
    for i in range(len(chunks)):
        chunk = chunks[i]
        paragraphs = []
        model_name = list(models.keys())[i]
        for page in chunk:
            lines = extract_text(page).split('\n')
            for index in find(lines, match):
                print(f'{model_name}-{lines[index - 1]}')
                paragraphs.append({
                    "name": lines[index - 1],
                    "page": page.page_number
                })
            #print()
        all_para.append({
            "model": list(models.keys())[i],
            "paragraphs": paragraphs
        })
        total += 1

        print(f'{round(total/len(chunks) * 100, 2)}% {total}/{len(chunks)}')
        #print({)
    
    pyperclip.copy(json.dumps(all_para, ensure_ascii = False))
    #print(json.dumps(all_para, ensure_ascii = False))
            


    #full = ""
    #for page in chunks[0]:
        #full += f'{extract_text(page)}\n'

    


    #verbal_analogy = full.split('\n').index('التناظر اللفظي')

    #print('\n'.join(full.split('\n')[0:verbal_analogy]))

    
    #contextual_error = full.split('\n').index('الخطأ السياقي')
    #sentence_completion = full.split('\n').index('إكمال الجمل')

    #print('\n'.join(full.split('\n')[verbal_analogy+1:contextual_error]))
    #print('\n'.join(full.split('\n')[contextual_error+1:sentence_completion]))
    #print('\n'.join(full.split('\n')[sentence_completion+1:]))
    
        
        #print(models)
    #pprint.pprint(chunks)
        #model_transmissions[i]
    
    #for page in pdf.pages:
        #pass
        
    #for i in range
    
    #my_page = pdf.pages[28]

    # todo:
    # count every verbal analogy question, dont forget to only select those under
    # each section and stop when entering a new section
    
    #content = my_page.extract_text()
    #content = '\n'.join(map(lambda e: e[::-1], content.split('\n')))
    #print(content)
    
    #verbal_index = thepages.split('\n').index('التناظر اللفظي')
    #verbal = '\n'.join(thepages.split('\n')[verbal_index:])
    

    #print(verbal)

    #for item in thepages.split('\n'):
        #if is_question(item):
            #print(item)


    
    #print()
    #print(thepages)
    #thepages = '\n'.join(map(lambda e: e[::-1], thepages.split('\n')))
    #reshaped_text = arabic_reshaper.reshape(thepages)
    #bidi_text = get_display(reshaped_text)
    
    #print(bidi_text)
