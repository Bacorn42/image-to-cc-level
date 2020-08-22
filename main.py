import sys
from PIL import Image
from colors import colorsToTile


def verify():
    if len(sys.argv) < 2:
        print("Please input an image path.")
        return False
    return True


def run():
    img = Image.open(sys.argv[1])
    resized = img.resize((32, 32))
    tiles = getTiles(resized)
    # TODO: convert resized image to level


def getTiles(img):
    tiles = [[None] * img.height] * img.width
    for x in range(img.width):
        for y in range(img.height):
            tiles[x][y] = getClosestTile(img.getpixel((x, y)))
    return tiles


def getColorDiff(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2


def getClosestTile(imgColor):
    bestDiff = sys.maxsize
    bestTile = None
    for color in colorsToTile:
        diff = getColorDiff(color, imgColor)
        if diff < bestDiff:
            bestDiff = diff
            bestTile = colorsToTile.get(color)
    return bestTile


if __name__ == '__main__':
    if verify():
        run()
