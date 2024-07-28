from os import getcwd, path, mkdir
from barcode import generate as gn
from barcode.writer import SVGWriter, ImageWriter


root_dir = getcwd()


def generate(code, output, filename, filetype="PNG"):
    output = "/downloads" if not output else path.join("/" + output)

    filename = path.join("/" + filename)

    path_new_file = root_dir + output

    if not path.exists(path_new_file):
        mkdir(path_new_file)
        print("directory created: " + path_new_file)

    writer = SVGWriter() if filetype != "PNG" else ImageWriter()

    gn(
        "ean",
        code,
        writer,
        path_new_file + filename,
        {"format": False if filetype != "PNG" else "PNG"},
        text=code,
    )
