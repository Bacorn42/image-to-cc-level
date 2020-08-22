from enum import Enum


class Tile(Enum):
    FLOOR = 0x00
    WALL = 0x01
    WATER = 0x03
    FIRE = 0x04
    BLOCK = 0x0A
    DIRT = 0x0B
    ICE = 0x0C
