import os
import shutil
import time
from os import listdir


def is_file_or_directory(content_path):
    isDirectory: bool = os.path.isdir(content_path)
    isFile: bool = os.path.isfile(content_path)
    if isDirectory:
        return "directory_content"
    elif isFile:
        return "file_content"


def movement(current_path_s, path_to_move_s, number_of_movements=0, ):
    current_files = listdir(current_path)

    for x in range(0, len(current_files) if number_of_movements == 0 else number_of_movements):
        current_transfering_file = current_files[x]
        print("Counter", x)
        current_transfering_file_path = f"{current_path}/{current_transfering_file}"
        shutil.move(current_transfering_file_path, path_to_move)  # might be some trouble here
        if x == len(current_files):
            print("Taşıma işlemi başarılı.")
            break
        else:
            pass
        time.sleep(0.5)


def advancedSettings(): #birden fazla parametre girilebilmesi sağlanacak
    print("")



while True:
    current_path = str(input("Klasör yolunu giriniz:"))
    if is_file_or_directory(current_path) == "directory_content":
        number_of_file = listdir(current_path)
        print(number_of_file)
        while True:
            path_to_move = str(input("Klasör içerisindeki dosyaların taşınacağı yolu girin"))
            # if path_to_move mevcut değilse oluştur.
            if is_file_or_directory(path_to_move) == "directory_content":
                if len(listdir(path_to_move)) == 0:  # No trouble
                    print(f"{path_to_move}, klasöründe herhangi bir dosya mevcut değil")
                    print(f"{current_path}, yolu içerisindeki bütün dosyalar: {path_to_move} adlı değişkene taşınacaktır.")
                    advanced_settings_options = input("Taşınma işlemi için gelişmiş seçenekleri görmek ister misiniz? 0:Hayır 1: Evet")
                    if advanced_settings_options == '0':
                        print("Advenced Settings will be here soon...")
                        advanced_settings_dic = {
                            1   : movement(current_path, path_to_move, deger_sayi),

                        }
                        advanced_settings = \
                            [
                                "Seçili sayıda dosya taşımak",
                                f"Dosya adlarını 0-{len(listdir(current_path))}'e şeklinde değiştirmek.",
                                "Taşınacak dosyaların uzantılarını değiştirmek.",
                                "Sadece belirli dosya türlerini taşımak",
                                " "
                            ]  # Birden fazla seçeneğin seçilmesi sağlanacak
                        print(advanced_settings)
                        #kaç dosyanın taşınması gerektiğini yaptırmak

                        secim = input("Hangisini seçmek istiyorsunuz:")
                        movement(current_path, path_to_move, deger_sayi)
                        advanced_settings_dic[secim]
                    else:
                        movement(current_path, path_to_move)

                            # loading satırı eklenebilir.
                    break


                else:  # Might be some trouble
                    print("Sorun başlıyor")
                    print(f"{path_to_move}, klasöründe {len(listdir(path_to_move))} ad")
            else:
                print("Hatalı giriş yaptınız")

    elif is_file_or_directory(current_path) == "file_content":
        print("Dosya yolu girdiniz.")
    else:
        print("Hatalı giriş. Programdan çıkmak için ESC tuşlayınız.")



