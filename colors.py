from tiles import Tile


def RGB_to_HSV(color):
    r_norm = color[0] / 255
    g_norm = color[1] / 255
    b_norm = color[2] / 255

    c_max = max(r_norm, g_norm, b_norm)
    c_min = min(r_norm, g_norm, b_norm)
    d = c_max - c_min

    h = 0
    if d != 0:
        if c_max == r_norm:
            h = 60 * ((g_norm - b_norm)/d)
        elif c_max == g_norm:
            h = 60 * ((b_norm - r_norm)/d + 2)
        else:
            h = 60 * ((r_norm - g_norm)/d + 4)

    s = 0
    if c_max != 0:
        s = d/c_max

    v = c_max

    return (h * 255/360, s * 255, v * 255)


color_to_tile_rgb = {
    (255, 255, 255): Tile.FLOOR,
    (192, 192, 192): Tile.FLOOR,
    (128, 128, 128): Tile.WALL,
    (0, 192, 255): Tile.WATER,
    (255, 192, 0): Tile.FIRE,
    (128, 128, 0): Tile.BLOCK,
    (128, 0, 0): Tile.DIRT,
    (128, 255, 255): Tile.ICE,
    (0, 128, 255): Tile.EXIT,
    (64, 192, 192): Tile.BLUE_DOOR,
    (192, 64, 64): Tile.RED_DOOR,
    (64, 192, 64): Tile.GREEN_DOOR,
    (192, 192, 64): Tile.YELLOW_DOOR,
    (32, 96, 96): Tile.FAKE_WALL,
    (0, 0, 0): Tile.GRAVEL,
    (160, 160, 160): Tile.RECESSED_WALL,
    (255, 0, 255): Tile.PINK_BALL,
    (0, 0, 255): Tile.TANK,
    (0, 128, 0): Tile.BLOB,
    (80, 255, 255): Tile.BLUE_KEY,
    (255, 80, 80): Tile.RED_KEY,
    (80, 255, 80): Tile.GREEN_KEY,
    (255, 255, 80): Tile.YELLOW_KEY,
}

# TODO: better balance background layer usage
for c, tile in list(color_to_tile_rgb.items()):
    if(tile.isTransparent()):
        avg = (c[0] + c[1] + c[2])/3
        color_to_tile_rgb[tuple(
            [v + (avg - v)/2 for v in c])] = (tile, Tile.WALL)
        color_to_tile_rgb[tuple([v/6 for v in c])] = (tile, Tile.GRAVEL)


color_to_tile_hsv = {}
for c, tile in list(color_to_tile_rgb.items()):
    color_to_tile_hsv[RGB_to_HSV(c)] = tile
