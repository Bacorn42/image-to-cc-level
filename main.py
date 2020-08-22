import sys
from PIL import Image


def verify():
    if len(sys.argv) < 2:
        print("Please input an image path.")
        return False
    return True


def run():
    img = Image.open(sys.argv[1])
    resized = img.resize((32, 32))
    # TODO: convert resized image to level


if __name__ == '__main__':
    if verify():
        run()
