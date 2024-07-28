from os import getcwd, path, mkdir
from uuid import uuid4
from random import randint
from barcode import generate
from barcode.writer import SVGWriter, ImageWriter

root_dir = getcwd()
print("current directory: " + root_dir)

output = input("output directory:")
filename = input("filename:")
filetype = input("""filetype
[1] PNG 
[Any other] SVG
""")

output = "/downloads" if not output else path.join("/" + output)
filename = (
    path.join("/test_" + str(uuid4())) if not filename else path.join("/" + filename)
)

path_new_file = root_dir + output

if not path.exists(path_new_file):
    mkdir(path_new_file)
    print("directory created: " + path_new_file)

RANGE_INITIAL = 100000
RANGE_FINAL = 999999
random_code_1 = randint(RANGE_INITIAL, RANGE_FINAL)
random_code_2 = randint(RANGE_INITIAL, RANGE_FINAL)

hash = str(random_code_1) + str(random_code_2)

writer = SVGWriter() if filetype != "1" else ImageWriter()

bar_code = generate(
    "ean",
    hash,
    writer,
    path_new_file + filename,
    {"format": "PNG"},
    text=hash,
)

print(f"number printed on the qr code: {hash}")
print(f"created file in: {path}")
