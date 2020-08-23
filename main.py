import sys
from os import path
from tiles_maker import make_tiles
from level_maker import save_level


def verify():
    if len(sys.argv) < 2:
        print("Usage: main.py image [output]")
        return False
    if(not path.exists(sys.argv[1])):
        print("File %s does not exist" % sys.argv[1])
        return False
    return True


def run():
    tiles = make_tiles(sys.argv[1])
    save_level(tiles)


if __name__ == '__main__':
    if verify():
        run()
