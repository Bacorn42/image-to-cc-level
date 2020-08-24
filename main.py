import sys
from os import path
import argparse
from tiles_maker import make_tiles
from level_maker import save_levels


def verify(args):
    for image in args.images:
        if(not path.exists(image)):
            print("File %s does not exist" % image)
            return False
    return True


def run(args):
    tiles = make_tiles(args.images)
    save_levels(args.o, tiles)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", help="image files")
    parser.add_argument("-o", help="output file", metavar="output")
    args = parser.parse_args()

    if verify(args):
        run(args)
