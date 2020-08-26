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
    format = get_format(args)
    tiles = make_tiles(args.images, format)
    save_levels(args.o, tiles)


def get_format(args):
    if args.rgb:
        return "RGB"
    elif args.ycbcr:
        return "YCbCr"
    elif args.gray:
        return "L"
    else:
        return "HSV"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", help="image files")
    parser.add_argument("-o", help="output file", metavar="output")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--hsv", help="HSV format (default)",
                       action="store_false")
    group.add_argument("--rgb", help="RGB format", action="store_true")
    group.add_argument("--ycbcr", help="YCbCr format", action="store_true")
    group.add_argument("--gray", help="Grayscale format", action="store_true")
    args = parser.parse_args()

    if verify(args):
        run(args)
