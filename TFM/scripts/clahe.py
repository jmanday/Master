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

PATH_OUTPUTS_SEGMENTATION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/segmentation/"
PATH_OUTPUTS_FEATURE_EXTRACTION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/improved_iris(clahe)/"

METHODS_SEGMENTATION = ['caht', 'wahet']


# método que aplica el algoritmo "CLAHE" a las texturas del iris para mejorarlas
def clahe(iris_segmentation):
    for key, value in iris_segmentation.iteritems():
        for path_img in value:
            img = cv2.imread(path_img,0)
            # create a CLAHE object (Arguments are optional).
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
            cl1 = clahe.apply(img)
            vaux = path_img.split('/')
            name = vaux[len(vaux)-1].split('-')[0]
            print PATH_OUTPUTS_FEATURE_EXTRACTION + key + '/' + name + '-clahe.png'
            cv2.imwrite(PATH_OUTPUTS_FEATURE_EXTRACTION + key + '/' + name + '-clahe.png',cl1)


# método para obtener las texturas del iris realizadas con los algoritmos "caht" y "wahet"
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


if __name__ == "__main__":

    iris_segmentation_CASIAV4 = getIrisSegmentationCASIAV4()
    clahe(iris_segmentation_CASIAV4)
