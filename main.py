import os as os
import shutil

#şimdi benim iki
import shutil
from os.path import isfile, join
import os as os
from os import listdir

#fotolar = "/home/mehmetemrepolat/Desktop/deneme/dataset/train/images"
#txt = "txt/"

txt_list = listdir(txt)

print(txt_list)
print(len(txt_list))
dosya_isim = txt_list[15]

print(dosya_isim)
uzantisiz_isim = os.path.splitext(dosya_isim)[0]
print(uzantisiz_isim)
print("-----------------")
def uzantisiz(_fileName):
    uzantisiz = os.path.splitext(_fileName)[0]
    return uzantisiz



#deneme içerisindeki jpg dosyasınının aynı ismiyle
#txt dosyasında bir dosyanın mevcut olup olmadığını
#kontrol edip yazdırılacak
v2 = os.listdir('deneme')[0]

yeni_isim = f'{uzantisiz(v2)}.txt'
print('yeni isim', yeni_isim)
print('boşluksuz:', yeni_isim.replace(" ", ""))
bosluksuz = yeni_isim.replace(" ", "")
if bosluksuz in txt_list:
    print("mevcut")

print(v2)


shutil.move(f'txt/{bosluksuz}', f'deneme/')
