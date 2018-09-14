# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### medianBlur.py
### @Descripcion: script to remove noise and apply blur the images
###
### @Params: the image to process
###
### @Output: the image with the operations applied
###
### @Execute: python segmentation-iris.py name-Image
#########################################################################

import numpy as np
import cv2
import os
import sys
import argparse

# create the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'Path to the input image')
args = vars(ap.parse_args())

# read the image
image = cv2.imread(args['image'])

# apply the 3x3 median filter on the image
processed_image = cv2.medianBlur(image, 3)

# display image
cv2.imshow('Median Filter Processing', processed_image)

# save image to disk
cv2.imwrite('processed_image.png', processed_image)

# pause the execution of the script until a key on the keyboard is pressed
cv2.waitKey(0)
