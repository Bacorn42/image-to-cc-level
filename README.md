# Image to CC Level

A small program that converts an image into a CC1 level.

It works by resizing an image to size 32x32 and then it approximates the colors to specific CC1 tiles in the HSV color model (to prioritize finding similar hues).

## Usage

`usage: main.py [-h] [-o output] [--rgb | --hsv] images [images ...]`
