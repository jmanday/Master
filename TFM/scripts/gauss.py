# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### gauus.py
### @Descripcion: script to remove noise and apply blur the images
#########################################################################

import numpy as np
import cv2
import os
import commands
import sys

PATH_INPUT_IRIS = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/CASIA_V4/"
PATH_OUTPUTS_IRIS_GAUSS = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/gauss_filter/15/"
PATH_OUTPUTS_IRIS_SEGMENTATION_GAUSS = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/improved_iris(clahe)/"
PATH_OUTPUTS_FEATURE_EXTRACTION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/gauss_filter_iris_segmentation/"

METHODS_SEGMENTATION = ['caht', 'wahet']


# method to apply a gaussian filter to the images
def gauss_filter(iris_CASIAV4):
    for path_img in iris_CASIAV4:
        img = cv2.imread(path_img,0)

        # apply Gaussian filter (Arguments are optional).
        blur = cv2.GaussianBlur(img,(5,5),15,15)

        vaux = path_img.split('/')
        name = vaux[len(vaux)-1].split('-')[0]
        name = name.split('.')[0]
        print PATH_OUTPUTS_IRIS_GAUSS + name + '-gauss.png'
        cv2.imwrite(PATH_OUTPUTS_IRIS_GAUSS + name + '-gauus.png',blur)


# method to apply a gaussian filter to the images from segmentation's iris
def gauss_filter_iris_segmentation(iris_segmentation):
    for key, value in iris_segmentation.iteritems():
        for path_img in value:
            img = cv2.imread(path_img,0)

            # apply Gaussian filter (Arguments are optional).
            blur = cv2.GaussianBlur(img,(5,5),0)

            vaux = path_img.split('/')
            name = vaux[len(vaux)-1].split('-')[0]
            print PATH_OUTPUTS_FEATURE_EXTRACTION + key + '/' + name + '-gauss.png'
            cv2.imwrite(PATH_OUTPUTS_FEATURE_EXTRACTION + key + '/' + name + '-gauss.png',blur)


# method to obtein the textures from iris after that method CLAHE has been applied
def getIrisCLAHE():
    vnames_images = []
    images_seg = {}

    for type_seg in METHODS_SEGMENTATION:
        direc = os.chdir(PATH_OUTPUTS_IRIS_CLAHE + "/" + type_seg)
        cmd = ("ls")
        res = commands.getstatusoutput(cmd)
        if res[0] == 0:
            vnames_images = res[1].split()

        aux_name = []
        for name_file in vnames_images:
            cmd = ("find $PWD -type f -name " + name_file)
            res = commands.getstatusoutput(cmd)
            if res[0] == 0:
                aux_name.append(res[1])

        images_seg[type_seg] = aux_name

    return images_seg


# method to obtein the textures from iris
def getIrisCASIAV4():
    vnames_images = []

    direc = os.chdir(PATH_INPUT_IRIS)
    cmd = ("ls")
    res = commands.getstatusoutput(cmd)
    if res[0] == 0:
        vnames_images = res[1].split()

    aux_name = []
    for name_file in vnames_images:
        vname_file = name_file.split('.')
        if (vname_file[1] != 'txt'):
            cmd = ("find $PWD -type f -name " + name_file)
            res = commands.getstatusoutput(cmd)
            if res[0] == 0:
                aux_name.append(res[1])

    return aux_name


if __name__ == "__main__":

    #iris_image_CLAHE = getIrisCLAHE()
    #gauss_filter_iris_segmentation(iris_image_CLAHE)
    iris_CASIAV4 = getIrisCASIAV4()
    gauss_filter(iris_CASIAV4)
