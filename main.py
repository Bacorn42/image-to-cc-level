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
    hsv = resized.convert('HSV')

    tiles = getTiles(hsv)
    saveLevel(tiles)


def getTiles(img):
    tiles = [None] * img.width * img.height
    for x in range(img.width):
        for y in range(img.height):
            tiles[y * img.width + x] = getClosestTile(img.getpixel((x, y)))
    return tiles


def getColorDiff(c1, c2):
    # TODO: improve this hack
    s = 0 if c2[1] < 30 else 255

    dh = min(abs(c1[0] - c2[0]), 255 - abs(c1[0] - c2[0]))
    ds = c1[1] - s
    dv = c1[2] - c2[2]

    if s == 0:
        dh = 170

    return (dh**2 * 0.15) + (ds**2 * 0.8) + (dv**2 * 0.05)


def getClosestTile(imgColor):
    bestDiff = sys.maxsize
    bestTile = None
    for color in colorsToTile:
        diff = getColorDiff(HSLtoHSV(color), imgColor)
        if diff < bestDiff:
            bestDiff = diff
            bestTile = colorsToTile.get(color)
    return bestTile


def HSLtoHSV(hsl):
    h, s, l = (hsl[0] * 255/240, hsl[1]/240, hsl[2]/240)

    newH = h
    newV = l + s * min(l, 1 - l)
    newS = 0 if newV == 0 else 2 * (1 - l/newV)

    return (newH, newS * 255, newV * 255)


def saveLevel(tiles):
    filename = "level.dat" if len(sys.argv) < 3 else sys.argv[2]

    file = open(filename, "wb")
    file.write((0x0002AAAC).to_bytes(4, byteorder="little"))  # magic number
    # number of levels = 1
    file.write((0x0001).to_bytes(2, byteorder="little"))
    # size of level TODO: use RLE
    file.write((0x042F).to_bytes(2, byteorder="little"))
    file.write((0x0001).to_bytes(2, byteorder="little"))  # level number = 1
    file.write((0x0000).to_bytes(2, byteorder="little"))  # time = 0
    file.write((0x0000).to_bytes(2, byteorder="little"))  # chips = 0
    file.write((0x0001).to_bytes(2, byteorder="little"))  # map detail
    file.write((0x0400).to_bytes(2, byteorder="little"))  # first layer
    for tile in tiles:
        file.write(tile.value.to_bytes(1, byteorder="little"))
    file.write((0x000F).to_bytes(2, byteorder="little"))  # second layer
    # empty bg layer
    file.write((0xFFFF00FFFF00FFFF00FFFF00FF0400).to_bytes(
        15, byteorder="big"))
    # bytes to end of level
    file.write((0x0012).to_bytes(2, byteorder="little"))
    file.write((0x03).to_bytes(1, byteorder="little"))  # field 3
    file.write((0x06).to_bytes(1, byteorder="little"))  # bytes in title
    file.write(b"Image\0")  # level title
    file.write((0x07).to_bytes(1, byteorder="little"))  # field 7
    file.write((0x01).to_bytes(1, byteorder="little"))  # hint length
    file.write(b"\0")  # hint
    file.write((0x06).to_bytes(1, byteorder="little"))  # field 6
    file.write((0x05).to_bytes(1, byteorder="little"))  # password length
    file.write((0xDBDDD1C900).to_bytes(5, byteorder="big"))  # password BDHP
    file.close()


if __name__ == '__main__':
    if verify():
        run()
