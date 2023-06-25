import PyPDF2
import json

def is_utf8(string):
    try:
        string.decode('utf-8')
        return True
    except Exception:
        return False

def try_utf8(string):
    try:        
        return string.decode('utf-8')
    except Exception:
        return None

#with open('arabic.json'

with open("one.pdf", "rb") as file:
    #binary = "11011000 10100111 11011001 10000100 11011001 10000010 11011000 10110111 11011000 10111001"
    # b'\xd8\xa7\xd9\x84\xd9\x82\xd8\xb7\xd8\xb9'
    #full = ""
    #for i in binary.split(' '):
        #full += str(hex(int(i, 2)))[1:]
        #full += '\\'
        ##print(str(hex(int(i, 2)))[1:])
    #print(full)
    #print('ا'.encode('utf-8'))
    unicode = "القطع".encode('utf-8')
    #print(b'\xd9\x84'.decode('utf-8'))
    # b'\xd8\xa7\xd9\x84\xd9\x82\xd8\xb7\xd8\xb9'
    #print(unicode)
    #print(int(unicode[0]
    #print(unicode)
    #print(list(unicode))
    result = file.read()[0:2000]

    #print(result)
    #print(str(result).find(str(unicode)[2:-1]))
    #print(result[2000])
    full = ""
    for i in range(0, len(result)):
        first = i
        last = i + 2
        if last >= len(result):
            break

        chunk = try_utf8(result[first:last])
        if chunk:
            full += chunk
            #print(chunk)
    #print(full)
    #print(unicode)
    # key, has to be even, two hexes for each arabic cahracter
    #print(unicode[0:2].decode('utf-8'))
    #print(hex(unicode[0]))
    #x = str(hex(2))
    #print(x)
    #print(bytes.fromhex(x))
    #print(str(unicode[0]))
    #print(int(str(unicode[0]), 16))

    #with open("john", "wb") as bro:
        #bro.write(file.read())
    spaces = []
    #print(result[18])
    #print(result[0:20])
    for i in range(0, len(result)):
        if result[i] == 32:
            spaces.append(i)

    for i in range(0, len(spaces)):
        first = 0 if i == 0 else spaces[i - 1]
        last = spaces[i]
        chunk = result[first:last]
        if is_utf8(chunk):
            #print(chunk)
            pass
            #print(chunk)
            #print(chunk.decode('utf-8'))
        #spaces[max(i - 1, 0)]
        #spaces[i]
    #print(spaces)
        #print(i)
    
    #print(is_utf8(unicode))
    #print()

    #for i in str(file.read()[0:2000]).split(' '):
        #if is_utf8(i):
            #print(i)
    
    #print(file.read()[0:2000])
    
    #print(file.read()[0:2000].decode('ascii'))
    #read_pdf = PyPDF2.PdfFileReader(pdf_file)
    #number_of_pages = read_pdf.getNumPages()
    #page = read_pdf.pages[0]
    #page_content = page.extractText()

#page_content = '\n'.join(list(map(lambda e: e[::-1], page_content.split('\n'))))
#print(page_content.encode('utf-8'))
