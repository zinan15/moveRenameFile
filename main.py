import os
import shutil

file_dir = "./files"
file_list = os.listdir(file_dir)

for file in file_list:
    if '.' in file:
        filename, extension = file.rsplit('.', 1)
    else:
        continue

    dest_folder = os.path.join(file_dir, extension)

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    src_path = os.path.join(file_dir, file)
    dst_path = os.path.join(dest_folder, file)
    shutil.move(src_path, dst_path)
