import sys


def save_levels(filename, tiles):
    if filename == None:
        filename = "level.dat"
    file = open(filename, "wb")
    write_set(file, tiles)
    file.close()


def write_set(file, tiles):
    write_set_data(file, len(tiles))
    for level_number, level_tiles in enumerate(tiles, start=1):
        write_level(file, level_tiles, level_number)


def write_set_data(file, levels):
    file.write((0x0002AAAC).to_bytes(4, byteorder="little"))  # magic number
    file.write((levels).to_bytes(2, byteorder="little"))  # number of levels


def write_level(file, tiles, level_number):
    layer = get_layer(tiles)
    write_level_info(file, len(layer), level_number)
    write_layers(file, layer)
    write_level_data(file)


def get_layer(tiles):
    layer = []
    i = 0
    while i < len(tiles):
        count = 1
        tile = tiles[i]
        i += 1
        while i < len(tiles) and tile == tiles[i] and count < 255:
            i += 1
            count += 1
        if count > 3:
            layer.extend([0xFF, count, tile.value])
        else:
            layer.extend([tile.value] * count)
    return layer


def write_level_info(file, level_size, level_number):
    file.write((47 + level_size).to_bytes(2, byteorder="little"))
    file.write((level_number).to_bytes(2, byteorder="little"))  # level number
    file.write((0).to_bytes(2, byteorder="little"))  # time = 0
    file.write((0).to_bytes(2, byteorder="little"))  # chips = 0


def write_layers(file, layer):
    file.write((1).to_bytes(2, byteorder="little"))  # map detail
    file.write((len(layer)).to_bytes(2, byteorder="little"))  # first layer
    for byte in layer:
        file.write(byte.to_bytes(1, byteorder="little"))
    file.write((15).to_bytes(2, byteorder="little"))  # second layer
    # empty bg layer
    file.write((0xFFFF00FFFF00FFFF00FFFF00FF0400).to_bytes(
        15, byteorder="big"))


def write_level_data(file):
    # bytes to end of level
    file.write((18).to_bytes(2, byteorder="little"))
    file.write((3).to_bytes(1, byteorder="little"))  # field 3
    file.write((6).to_bytes(1, byteorder="little"))  # bytes in title
    file.write(b"Image\0")  # level title
    file.write((7).to_bytes(1, byteorder="little"))  # field 7
    file.write((1).to_bytes(1, byteorder="little"))  # hint length
    file.write(b"\0")  # hint
    file.write((6).to_bytes(1, byteorder="little"))  # field 6
    file.write((5).to_bytes(1, byteorder="little"))  # password length
    file.write((0xDBDDD1C900).to_bytes(5, byteorder="big"))  # password BDHP
