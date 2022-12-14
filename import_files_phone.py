import os
import shutil
import fnmatch
from datetime import datetime


def sort(src_path, des_path):
    if not os.path.exists(src_path):
        print("Invalid source path!")
        os._exit(0)

    if not os.path.exists(des_path):
        os.mkdir(des_path)

    dir_item_list = os.listdir(src_path)

    for i in dir_item_list:
        item = i.lower()
        item_path = os.path.join(src_path, i)

        if not os.path.isfile(item_path):
            sort(item_path, des_path)
        else:
            path = ""
            if item.endswith(".mp4"):
                path = "/videos"
            elif item.endswith(".gif"):
                path = "/gifs"
            elif item.endswith(".pdf"):
                path = "/pdfs"
            elif fnmatch.fnmatch(item, "*screenshot*") and (item.endswith(".jpg") or item.endswith(".jpeg")):
                path = "/screenshots"
            elif item.endswith(".jpg") or item.endswith(".jpeg"):
                if fnmatch.fnmatch(item, "*img*") or os.path.getsize(item_path) > 1024.0:
                    dt = str(datetime.fromtimestamp(os.path.getmtime(item_path)))
                    date = (dt[0:4], dt[5:7], dt[8:10])
                    path = f"/photos/{date[0]}/{date[1]}/{date[2]}"
                else:
                    path = "/images"

            if path == "":
                continue
            else:
                if not os.path.exists(des_path + path):
                    os.makedirs(des_path + path, exist_ok=True)
                    
                shutil.copy2(item_path, des_path + path)
                print(f"{item} copied to {path}")


def main():
    src_folder = ""
    des_folder = ""
    sort(src_folder, des_folder)


if __name__ == '__main__':
    main()
