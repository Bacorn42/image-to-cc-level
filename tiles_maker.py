import sys
from math import sqrt
from PIL import Image
from colors import get_color_to_tile
from tiles import Tile


def make_tiles(img_paths, format):
    tiles = []
    color_to_tile = get_color_to_tile(format)
    for index, img_path in enumerate(img_paths, start=1):
        img = Image.open(img_path)
        resized = img.resize((32, 32))
        converted = resized.convert(format)

        tiles.append(get_tiles(converted, format, color_to_tile))
        print("%d/%d" % (index, len(img_paths)))

    return tiles


def get_tiles(img, format, color_to_tile):
    return [get_closest_tile(img.getpixel((x, y)), format, color_to_tile)
            for y in range(img.height)
            for x in range(img.width)]


def get_closest_tile(img_color, format, color_to_tile):
    best_diff = sys.maxsize
    best_tile = None
    for color in color_to_tile:
        diff = get_color_diff(color, img_color, format)
        if diff < best_diff:
            best_diff = diff
            best_tile = color_to_tile.get(color)
    if type(best_tile) == tuple:
        return best_tile
    return (best_tile, Tile.FLOOR)


def get_color_diff(color, img_color, format):
    if format == "RGB":
        return get_color_diff_rgb(color, img_color)
    elif format == "HSV" or format == "L":
        return get_color_diff_hsv(color, img_color)
    elif format == "YCbCr":
        return get_color_diff_ycbcr(color, img_color)
    else:
        print("Error: Unknown format")
        sys.exit()


# https://www.compuphase.com/cmetric.htm
def get_color_diff_rgb(c1, c2):
    rmean = (c1[0] + c2[0]) / 2
    dr = c1[0] - c2[0]
    dg = c1[1] - c2[1]
    db = c1[2] - c2[2]
    return sqrt((((512+rmean)*dr**2) / 2**8) + 4*dg**2 + (((767-rmean)*db**2) / 2**8))


# TODO: improve this hack
def get_color_diff_hsv(c1, c2):
    c2 = get_tuple(c2)
    s = 0 if c2[1] < 25 else (128 if c2[1] < 100 else 255)

    dh = min(abs(c1[0] - c2[0]), 255 - abs(c1[0] - c2[0]))
    ds = c1[1] - s
    dv = c1[2] - c2[2]

    # no saturation means hue is unimportant
    if s == 0:
        dh = 0

    return (dh**2 * 0.17) + (ds**2 * 0.8) + (dv**2 * 0.03)


def get_tuple(c):
    if type(c) == int:
        return (0, 0, c)
    return c


def get_color_diff_ycbcr(c1, c2):
    dy = c1[0] - c2[0]
    dcb = c1[1] - c2[1]
    dcr = c1[2] - c2[2]

    return dy**2 + dcb**2 + dcr**2
