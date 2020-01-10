"""
This file generates a bunch of lines like:
<img src='path/to/file.jpg'>

This is really helpful when using the Jekyll Journal Gallery element, as you need an <img> tag for every image in the gallery.
"""


import sys
from os import listdir
from os.path import isfile, join



if __name__ == "__main__":
    post_date_title = sys.argv[1]
    folder_path = "images/blog/" + post_date_title
    srcs = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    tags = sorted([f"<img src='{'/' + folder_path + '/' + src}'>" for src in srcs])
    for tag in tags:
        print(tag)
    # print(srcs)