import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Spec file")
args = parser.parse_args()
if args.file:
    with open(args.file, "r+") as f:
        data = f.readlines()
        data[1] = "from kivy_deps import sdl2, glew\n"
        data[24] = data[24].replace("[]", "*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + ['resource'])]")
        f.seek(0)
        f.write("".join(data))
        f.truncate()
