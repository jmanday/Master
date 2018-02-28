# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### clahe.py
### @Descripcion: script to improve texture from iris apply the
###              algorithm "CLAHE"
#########################################################################

import numpy as np
import cv2
import os
import commands
import sys

PATH_INPUT_IRIS = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/CASIA_V4/"
PATH_INPUT_SEGMENTATION_IRIS = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/images_Segmented/"
PATH_OUTPUTS_IRIS_CLAHE = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/iris_clahe/"
PATH_OUTPUTS_SEGMENTATION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/segmentation/"
PATH_OUTPUTS_CLAHE_SEGMENTATION_IRIS = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/iris_Segmented_Clahe/"
PATH_OUTPUTS_FEATURE_EXTRACTION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/iris_segmentation_clahe/"

METHODS_SEGMENTATION = ['caht', 'wahet']


# method to apply the algorithm CLAHE to improve the textures from iris
def clahe_iris(iris_CASIAV4):
    for path_img in iris_CASIAV4:
        img = cv2.imread(path_img,0)
        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        vaux = path_img.split('/')
        name = vaux[len(vaux)-1].split('-')[0]
        name = name.split('.')[0]
        print(PATH_OUTPUTS_IRIS_CLAHE + name + '-clahe.png')
        cv2.imwrite(PATH_OUTPUTS_IRIS_CLAHE + name + '-clahe.png',cl1)


# method to apply the algorithm CLAHE to improve the textures from segmentation' iris
def clahe_iris_segmentation(iris_segmentation):
    for key, value in iris_segmentation.iteritems():
        for path_img in value:
            img = cv2.imread(path_img,0)
            # create a CLAHE object (Arguments are optional).
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
            cl1 = clahe.apply(img)
            vaux = path_img.split('/')
            name = vaux[len(vaux)-1].split('-')[0]
            print(PATH_OUTPUTS_FEATURE_EXTRACTION + key + '/' + name + '-clahe.png')
            cv2.imwrite(PATH_OUTPUTS_FEATURE_EXTRACTION + key + '/' + name + '-clahe.png',cl1)


# method to obtein the textures from segmentation's iris that have been made with the algorithms "caht" and "wahet"
def getIrisSegmentationCASIAV4():
    vnames_images = []
    images_seg = {}

    for type_seg in METHODS_SEGMENTATION:
        direc = os.chdir(PATH_OUTPUTS_SEGMENTATION + "/" + type_seg)
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


# method to obtein the textures from segmentation's iris that have been made with the algorithm proposed
def getIrisSegmentationCASIA_V4():
    vnames_images = []
    images_seg = {}

    direc = os.chdir(PATH_INPUT_SEGMENTATION_IRIS)
    cmd = ("ls")
    res = commands.getstatusoutput(cmd)
    if res[0] == 0:
        vnames_images = res[1].split()
    print(res)
    #aux_name = []
    #for name_file in vnames_images:
    #    cmd = ("find $PWD -type f -name " + name_file)
    #    res = commands.getstatusoutput(cmd)
    #    if res[0] == 0:
    #        aux_name.append(res[1])

    #images_seg[type_seg] = aux_name

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

    #iris_segmentation_CASIAV4 = getIrisSegmentationCASIAV4()
    #clahe_iris_segmentation(iris_segmentation_CASIAV4)
    iris_CASIAV4 = getIrisSegmentationCASIA_V4()
    #clahe_iris(iris_CASIAV4)
