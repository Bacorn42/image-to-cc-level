import sys


# TODO: possibly multiple levels in a set
def save_level(tiles):
    filename = "level.dat" if len(sys.argv) < 3 else sys.argv[2]
    file = open(filename, "wb")
    write_set(file, tiles)
    file.close()


def write_set(file, tiles):
    write_set_data(file)
    write_level(file, tiles)


def write_set_data(file):
    file.write((0x0002AAAC).to_bytes(4, byteorder="little"))  # magic number
    # number of levels = 1
    file.write((0x0001).to_bytes(2, byteorder="little"))


def write_level(file, tiles):
    write_level_info(file)
    write_layers(file, tiles)
    write_level_data(file)


def write_level_info(file):
    # size of level TODO: use RLE
    file.write((0x042F).to_bytes(2, byteorder="little"))
    file.write((0x0001).to_bytes(2, byteorder="little"))  # level number = 1
    file.write((0x0000).to_bytes(2, byteorder="little"))  # time = 0
    file.write((0x0000).to_bytes(2, byteorder="little"))  # chips = 0


def write_layers(file, tiles):
    file.write((0x0001).to_bytes(2, byteorder="little"))  # map detail
    file.write((0x0400).to_bytes(2, byteorder="little"))  # first layer
    for tile in tiles:
        file.write(tile.value.to_bytes(1, byteorder="little"))
    file.write((0x000F).to_bytes(2, byteorder="little"))  # second layer
    # empty bg layer
    file.write((0xFFFF00FFFF00FFFF00FFFF00FF0400).to_bytes(
        15, byteorder="big"))


def write_level_data(file):
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
