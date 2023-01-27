import os as os
import shutil
from os.path import isfile, join
from os import listdir


wants_to_change = input("Dosya Yolunu giriniz:")
target_path = input("Taşımak istediğiniz yolu giriniz:")

List_wants_to_change = listdir(wants_to_change)
List_target_path = listdir(target_path)

if listdir(wants_to_change) is not None:
    print(List_target_path)
else:
    print("Unkown path")

print("---")
print(List_wants_to_change)

