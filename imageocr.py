#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Zhang
#
# Created:     09/11/2013
# Copyright:   (c) Zhang 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from PIL import *
from pytesser import *
def testing(x):
    filename = x
    im = Image.open(filename)

    text = image_to_string(im)
    return text
def main():
    print testing("justinimage.jpg")


if __name__ == '__main__':
    main()
