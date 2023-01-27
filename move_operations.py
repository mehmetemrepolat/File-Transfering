import os
import heapq
import random


def rename_files(folder_path):
    i = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                new_filename = str(i) + ".jpg"
            elif filename.endswith(".png"):
                new_filename = str(i) + ".png"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            i += 1

def change_extension(folder_path, old_extension, new_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(old_extension):
            new_filename = filename.replace(old_extension, new_extension)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

def move_largest_files(src_folder, dst_folder, top_n):
    files = [(os.path.join(src_folder, file), os.path.getsize(os.path.join(src_folder, file))) for file in os.listdir(src_folder)]
    largest_files = heapq.nlargest(top_n, files, key=lambda file: file[1])
    for file in largest_files:
        os.rename(file[0], os.path.join(dst_folder, os.path.basename(file[0])))


def move_random_files2(src_folder, dst_folder, num_files):
    files = [os.path.join(src_folder, file) for file in os.listdir(src_folder)]
    random_files = random.sample(files, num_files)
    for file in random_files:
        os.rename(file, os.path.join(dst_folder, os.path.basename(file)))

def move_random_files(src_folder, dst_folder, num_files, file_extension=None):
    """
    Move random files from one folder to another.
    src_folder:     The source folder where files are located.
    dst_folder:     The destination folder where files will be moved to.
    num_files:      Number of files to move.
    file_extension: The extension of files that will be moved.
    """
    if not os.path.exists(src_folder):
        raise ValueError(f"Source folder {src_folder} does not exist.")
    if not os.path.exists(dst_folder):
        raise ValueError(f"Destination folder {dst_folder} does not exist.")
    if not os.path.isdir(src_folder):
        raise ValueError(f"{src_folder} is not a folder.")
    if not os.path.isdir(dst_folder):
        raise ValueError(f"{dst_folder} is not a folder.")
    if num_files <= 0:
        raise ValueError(f"num_files({num_files}) can't be less than 1.")
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f)) and (file_extension is None or f.endswith(file_extension))]
    if num_files > len(files):
        raise ValueError(f"num_files({num_files}) can't be greater than number of files({len(files)}).")
    selected_files = random.sample(files, num_files)

    for file in selected_files:
        src_file = os.path.join(src_folder, file)
        dst_file = os.path.join(dst_folder, file)
        os.rename(src_file, dst_file)

# change_extension(input("File Path:"), input("Enter the extensions that need to be changed:"), input("Enter the extension to be changed:"))
# move_largest_files('Person2','Person1' , 15)
# move_random_files('Person1', 'Person2', 20)
