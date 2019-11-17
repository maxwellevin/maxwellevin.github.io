import sys
from os import listdir
from os.path import isfile, join



if __name__ == "__main__":
    folder_path = sys.argv[1]
    srcs = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    tags = [f"<img src='{'/' + folder_path + src}'>" for src in srcs]
    for tag in tags:
        print(tag)
    # print(srcs)