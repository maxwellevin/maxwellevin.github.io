import sys
from os import listdir
from os.path import isfile, join



if __name__ == "__main__":
    post_date_title = sys.argv[1]
    folder_path = "images/blog/" + post_date_title
    srcs = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    tags = [f"<img src='{'/' + folder_path + src}'>" for src in srcs]
    for tag in tags:
        print(tag)
    # print(srcs)