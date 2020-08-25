import sys
from math import sqrt
from PIL import Image
from colors import color_to_tile_rgb, color_to_tile_hsv
from tiles import Tile


def make_tiles(img_paths, format):
    tiles = []
    for index, img_path in enumerate(img_paths, start=1):
        img = Image.open(img_path)
        resized = img.resize((32, 32))
        converted = resized.convert(format)

        tiles.append(get_tiles(converted, format))
        print("%d/%d" % (index, len(img_paths)))

    return tiles


def get_tiles(img, format):
    return [get_closest_tile(img.getpixel((x, y)), format)
            for y in range(img.height)
            for x in range(img.width)]


def get_closest_tile(img_color, format):
    best_diff = sys.maxsize
    best_tile = None
    color_to_tile = get_color_to_tile(format)
    for color in color_to_tile:
        diff = get_color_diff(color, img_color, format)
        if diff < best_diff:
            best_diff = diff
            best_tile = color_to_tile.get(color)
    if type(best_tile) == tuple:
        return best_tile
    return (best_tile, Tile.FLOOR)


def get_color_to_tile(format):
    if format == "RGB":
        return color_to_tile_rgb
    elif format == "HSV":
        return color_to_tile_hsv
    else:
        print("Error: Unknown format")
        sys.exit()


def get_color_diff(color, img_color, format):
    if format == "RGB":
        return get_color_diff_rgb(color, img_color)
    elif format == "HSV":
        return get_color_diff_hsv(color, img_color)
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
    s = 0 if c2[1] < 25 else (128 if c2[1] < 100 else 255)

    dh = min(abs(c1[0] - c2[0]), 255 - abs(c1[0] - c2[0]))
    ds = c1[1] - s
    dv = c1[2] - c2[2]

    # no saturation means hue is unimportant
    if s == 0:
        dh = 0

    return (dh**2 * 0.17) + (ds**2 * 0.8) + (dv**2 * 0.03)
