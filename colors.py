from tiles import Tile

colorsToTile = {
    (192, 192, 192): Tile.FLOOR,
    (128, 128, 128): Tile.WALL,
    (0, 255, 255): Tile.WATER,
    (255, 255, 0): Tile.FIRE,
    (128, 128, 0): Tile.BLOCK,
    (128, 0, 0): Tile.DIRT,
    (64, 255, 255): Tile.ICE
}
