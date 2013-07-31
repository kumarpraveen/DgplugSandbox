#!/usr/bin/env python
from sys import exit
import os
from os.path import join
from argparse import ArgumentParser
from PIL import ImageChops, Image


""" This function takes user folder arguments and
    make a list of image files"""


def image_file_list(path_list):
    image_files = []
    # Getting Image file details
    for directory in path_list:
        for root, dirs, files in os.walk(directory):
            for name in files:
                image_files.append(join(root, name))
    return image_files

""" This function takes image files to process compare """


def image_process(image_list):
    for i in range(len(image_list)):
        for j in range(i + 1, len(image_list)):
            if not image_compare(image_list[i], image_list[j]):
                print "%s is same as %s" % (image_list[i], image_list[j])

""" This function will use image file to compare """


def image_compare(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    return ImageChops.difference(image1, image2).getbbox()

if __name__ == "__main__":

    # User directory Arguments
    parser = ArgumentParser()
    parser.add_argument("-f", "--folder", nargs='+', help="Add directory \
                        which contain images")
    directory_list = parser.parse_args().folder
    if directory_list:
        image_list = image_file_list(directory_list)
        image_process(image_list)
    else:
        parser.print_help()
    exit(0)
