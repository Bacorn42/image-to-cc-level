from tiles import Tile

# colors in HSL format with values from 0 to 240 (MS Paint lul)
color_to_tile = {
    (160, 0, 180): Tile.FLOOR,
    (160, 0, 120): Tile.WALL,
    (130, 240, 120): Tile.WATER,
    (30, 240, 120): Tile.FIRE,
    (40, 240, 60): Tile.BLOCK,
    (0, 240, 60): Tile.DIRT,
    (120, 240, 180): Tile.ICE,
    (140, 240, 120): Tile.EXIT,
    (120, 120, 100): Tile.BLUE_DOOR,
    (0, 120, 100): Tile.RED_DOOR,
    (80, 120, 100): Tile.GREEN_DOOR,
    (40, 120, 100): Tile.YELLOW_DOOR,
    (120, 120, 60): Tile.FAKE_WALL,
    (160, 0, 0): Tile.GRAVEL,
    (160, 0, 150): Tile.RECESSED_WALL,
    (200, 240, 120): Tile.PINK_BALL,
    (160, 240, 120): Tile.TANK,
    (80, 240, 80): Tile.BLOB,
    (120, 240, 160): Tile.BLUE_KEY,
    (0, 240, 160): Tile.RED_KEY,
    (80, 240, 160): Tile.GREEN_KEY,
    (40, 240, 160): Tile.YELLOW_KEY,
}

for c, tile in list(color_to_tile.items()):
    if(tile.isTransparent()):
        color_to_tile[(c[0], c[1] - 120, c[2] - 20)] = (tile, Tile.WALL)
        color_to_tile[(c[0], c[1] - 120, 30)] = (tile, Tile.GRAVEL)
