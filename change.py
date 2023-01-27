import shutil
import os as os
from os import listdir

def uzantisiz(_fileName):
    uzantisiz = os.path.splitext(_fileName)[0]
    return uzantisiz
def yeni_uzanti(_file):
    yeni = f'{uzantisiz(_file)}.jpg'
    yeni = yeni.replace(" ", "")
    return yeni

txt = "txt/"
txt_list = listdir(txt)

def tasima(dosya_s):
    shutil.move(f'', 'etiketliler/')


for x in range(0, len(txt_list)):

    begin = yeni_uzanti(txt_list[x])
    try:
        shutil.move(f'images/{begin}', 'etiketliler')
    except:
        print("Hata")
    print(x,'.taşındı')
