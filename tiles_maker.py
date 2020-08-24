import sys
from PIL import Image
from colors import color_to_tile


def make_tiles(img_paths):
    tiles = []
    for index, img_path in enumerate(img_paths, start=1):
        img = Image.open(img_path)
        resized = img.resize((32, 32))
        hsv = resized.convert('HSV')

        tiles.append(get_tiles(hsv))
        print("%d/%d" % (index, len(img_paths)))

    return tiles


def get_tiles(img):
    return [get_closest_tile(img.getpixel((x, y)))
            for y in range(img.height)
            for x in range(img.width)]


def get_closest_tile(img_color):
    best_diff = sys.maxsize
    best_tile = None
    for color in color_to_tile:
        diff = get_color_diff(HSL_to_HSV(color), img_color)
        if diff < best_diff:
            best_diff = diff
            best_tile = color_to_tile.get(color)
    return best_tile


def get_color_diff(c1, c2):
    # TODO: improve this hack
    s = 0 if c2[1] < 30 else 255

    dh = min(abs(c1[0] - c2[0]), 255 - abs(c1[0] - c2[0]))
    ds = c1[1] - s
    dv = c1[2] - c2[2]

    if s == 0:
        dh = 170

    return (dh**2 * 0.15) + (ds**2 * 0.8) + (dv**2 * 0.05)


def HSL_to_HSV(hsl):
    h, s, l = (hsl[0] * 255/240, hsl[1]/240, hsl[2]/240)

    new_h = h
    new_v = l + s * min(l, 1 - l)
    new_s = 0 if new_v == 0 else 2 * (1 - l/new_v)

    return (new_h, new_s * 255, new_v * 255)
