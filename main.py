import sys
from tiles_maker import make_tiles
from level_maker import save_level


def verify():
    if len(sys.argv) < 2:
        print("Please input an image path.")
        return False
    return True


def run():
    tiles = make_tiles(sys.argv[1])
    save_level(tiles)


if __name__ == '__main__':
    if verify():
        run()
