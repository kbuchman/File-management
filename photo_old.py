import os
import shutil

src_folder = "d"
dst_folder = ""

if not os.path.exists(src_folder):
    os._exit(0)

if not os.path.exists(dst_folder):
    os.mkdir(dst_folder)

src_subfolders = os.listdir(src_folder)

for item in src_subfolders:
    item_path = os.path.join(src_folder, item)
    dst_path = dst_folder
    if not os.path.isfile(item_path):
        if "." in item:
            day, month, year = item.split(".")
            dst_path += "/20" + year + "/" + month + "/" + day
        else:
            dst_path += "/" + item
        shutil.copytree(item_path, dst_path, dirs_exist_ok=True)
    else:
        dst_path += "/others"
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.copy2(item_path, dst_path)
    