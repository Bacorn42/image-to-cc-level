from enum import Enum


class Tile(Enum):
    FLOOR = 0x00
    WALL = 0x01
    WATER = 0x03
    FIRE = 0x04
    BLOCK = 0x0A
    DIRT = 0x0B
    ICE = 0x0C
    EXIT = 0x15
    BLUE_DOOR = 0x16
    RED_DOOR = 0x17
    GREEN_DOOR = 0x18
    YELLOW_DOOR = 0x19
    FAKE_WALL = 0x1E
    GRAVEL = 0x2D
    RECESSED_WALL = 0x2E
    PINK_BALL = 0x48
    TANK = 0x4C
    BLOB = 0x5C
    BLUE_KEY = 0x64
    RED_KEY = 0x65
    GREEN_KEY = 0x66
    YELLOW_KEY = 0x67

    def isTransparent(self):
        return self.value >= 0x48
