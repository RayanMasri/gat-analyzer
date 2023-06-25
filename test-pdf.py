import fitz, subprocess, os, json
import arabic_reshaper
from bidi.algorithm import get_display
import psutil, signal

# IBM Plex Font Size to Height ratio: (5:8)
# IBM Ple Font Size to Point to Pixel ratio: (50:4.61)

arabic = fitz.Font(fontfile='arabic-font.ttf')
for proc in psutil.process_iter():
   # Get process detail as dictionary
    info = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
    if info["name"] == 'Acrobat.exe':
        os.kill(info["pid"], signal.SIGTERM)

class Handler:
    def __init__(self, page):
        self.page = page

    def text(self, text, x, y, width, height, highlight, **kwargs):
        rect = fitz.Rect(x, y, x + width, y + height)

        if highlight:
            shape = self.page.new_shape()
            shape.draw_rect(rect)
            shape.finish(width = 0.3, color = (1, 0, 0), fill = (0, 1, 0))
            shape.commit()

        self.page.insert_textbox(rect, text, **kwargs)  # Black text color (RGB)

def get_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
    bidi_text = get_display(reshaped_text)    
    return bidi_text
# Load the PDF document

doc = fitz.open()
page = doc.new_page(-1,
                    width = 595,
                    height = 842)






with open("duplicated.json", "r", encoding="utf8") as file:
    data = json.loads(file.read())

# data = []
# for i in range(90, 100):
#     data.append('ا' * i)

# 128 > x < 130.6
# 110.8800034224987
scale = 4
conversion = 4.61 / scale
size = 50 / scale
line_height = 1.5

page.insert_font(fontname="arabic", fontfile='arabic-font.ttf')

handler = Handler(page)
handler.text(get_arabic('عدد تكرار القطع'), 0, 0, page.rect.width, 80, False, fontsize=50, fontname="arabic", color=(0, 0, 0), align=fitz.TEXT_ALIGN_CENTER)


def work_page(page, index, total=0):
    page.insert_font(fontname="arabic", fontfile='arabic-font.ttf')

    total = total
    print(page)
    handler = Handler(page)
    for i in range(index, len(data)):
        item = data[i]
        item[0] = item[0].replace('اإل', 'الإ')
        item[0] = item[0].replace('األ', 'الأ')
        text = get_arabic(f'{item[0]} - {item[1]}')
        # text = get_arabic(item)
        width = arabic.text_length(text) * conversion
        # scale = 1
        font_size = size

        if width > page.rect.width:
            scale = width / page.rect.width
            font_size /= scale
            print(width)

        height = font_size * line_height
        if total + height > page.rect.height:
            # doc.new_page(-1, width = 595, height = 842)
            work_page(doc.new_page(-1, width = 595, height = 842), i)
            # work_page(doc.new_page(-1,
            #         width = 595,
            #         height = 842), i)
            break

        handler.text(text, 0, total, page.rect.width, height, False, fontsize=font_size, fontname="arabic", color=(0, 0, 0), align=fitz.TEXT_ALIGN_RIGHT)
        total += height

work_page(page, 0, 80)


os.remove('./organized.pdf')
doc.save('organized.pdf')
doc.close()

os.system('organized.pdf')
print('hi')


