# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### feature-extraction.py
### @Descripcion: script para realizar la extracción de las características
###             de las imágenes del iris y obtener un vector en forma de
###             imagen con las propiedades de cada uno. Se realizará la extracción
###             con cada uno de los algoritmos que que proporciona la librería USIT
#########################################################################

import os
import commands
import sys

PATH_EXECUTABLE = "/Users/jesusgarciamanday/Documents/Master/TFM/USITv1.0.3/"
PATH_OUTPUTS_SEGMENTATION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/segmentation/"
PATH_OUTPUTS_FEATURE_EXTRACTION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/feature\ extraction/"

# realiza la extraccion de características de la textura del iris con los algoritmos que proporciona la librería USIT
def feature_extraction(iris_segmentation_images):
        print 'features extracting'
        direc = os.chdir(PATH_EXECUTABLE)
        for type_extraction in METHODS_FEATURE_EXTRACTION:
            print "Algorithm " + type_extraction
            for key, value in iris_segmentation_images.iteritems():
                for path_img in iris_segmentation_images[key]:
                    vaux = path_img.split('/')
                    name = vaux[len(vaux)-1].split('-')[0]
                    cmd = ("./" + type_extraction + " -i " + path_img + " -o " + PATH_OUTPUTS_FEATURE_EXTRACTION + type_extraction + "/" + key + "/" + name + "-vector-feature.png")
                    res = commands.getstatusoutput(cmd)

                    if res[0] != 0:
                        print "ERROR AL EJECUTAR"


# realiza la extraccion de características de la textura del iris con el algoritmo "gfcf" proporcionado por la librería USIT
def algorithm_gfcf(iris_segmentation_images):
        print 'features extracting'
        direc = os.chdir(PATH_EXECUTABLE)

        print "Algorithm gfcf"
        for key, value in iris_segmentation_images.iteritems():
            for path_img in iris_segmentation_images[key]:
                vaux = path_img.split('/')
                name = vaux[len(vaux)-1].split('-')[0]
                cmd = ("./gfcf -i " + path_img + " -o " + PATH_OUTPUTS_FEATURE_EXTRACTION + "/" + key + "/" + name + "-face.png " + name + "-left-eye.png " + name + "-right-eye.png ")
                res = commands.getstatusoutput(cmd)
                
                if res[0] != 0:
                    print "ERROR AL EJECUTAR"


METHODS_SEGMENTATION = ['caht', 'wahet']
ALGORITHMS_FEATURE_EXTRACTION = {'lg': feature_extraction, 'qsw': feature_extraction, 'ko': feature_extraction, 'cr': feature_extraction, 'cb': feature_extraction, 'dct': feature_extraction, 'gfcf': algorithm_gfcf}


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

    nameFile = sys.argv[1]
    print nameFile
    #iris_segmentation_CASIAV4 = getIrisSegmentationCASIAV4()
    #feature_extraction(iris_segmentation_CASIAV4)
    #ALGORITHMS_FEATURE_EXTRACTION[mode_seg](iris_segmentation_CASIAV4)
