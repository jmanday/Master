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
from util import transpose
import math
import numpy as np


PATH_OUTPUTS_FEATURE_EXTRACTION = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/feature_extraction/Lip-vireo/prueba/"
PATH_DATABASE_CASIAV4 = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/CASIA_V4/"

class Imagen:
    quadrants = []
    features = []
    points = []


    def __init__(self, features, points):
         self.features = features
         self.points = points


# método que devuelve los nombres de las carpetas y ficheros que se encuentran
#   en el path especificado por parámetro
def obteinFolders(path):
    direc = os.chdir(path)
    cmd = ("ls")
    res = commands.getstatusoutput(cmd)

    if res[0] == 0:
        names = res[1].split()

    return names


# método que lee los ficheros de descriptores de las imagenes y las almacena en una estructura general
#   donde se separan por detectores, es decir, hay 3 grupos de imagenes donde cada imagen almacena en
#   en una matriz los valores de sus descriptores (128x128) (puntos x caracteristicas por cada punto)
def readFeatures(foldersFeaturesSIFT):
    cont = 1
    num_rows = 0
    imagenes_by_detector = []
    imagenes = []
    features = []
    vfeature = []
    points = []

    for fold in foldersFeaturesSIFT:
        path = PATH_OUTPUTS_FEATURE_EXTRACTION + fold + "/"
        cmd = ("ls " + path)
        res = commands.getstatusoutput(cmd)

        if res[0] == 0:
            nameFiles = res[1].split()

        for nFile in nameFiles:
            with open(path + nFile) as f:
                lines = f.read().split("\n")

            for l in lines:
                if ((cont > 2) and (cont <= len(lines))):
                    if (num_rows == 11):
                        features.append(vfeature)
                        num_rows = 0
                        vfeature = []
                        aux = l.split()
                        if (len(aux) > 0):
                            points.append(aux[0])
                            points.append(aux[1])
                    else:
                        vfeature = vfeature + l.split()
                        num_rows += 1
                else:
                    if(cont == 2):
                        aux = l.split()
                        points.append(aux[0])
                        points.append(aux[1])
                cont += 1

            img = Imagen(features, points)
            imagenes.append(img)
            features = []
            points =[]

        imagenes_by_detector.append(imagenes)
        imagenes = []
        cont = 1

    return imagenes_by_detector


# método que calcula la distancia de Lowe entre dos imagenes
#   comparando los puntos de interés que se encuentren en el
#   mismo cuadrante de una imagen con la otra
def getResultComparison(img1, img2):
    timg2 = np.transpose(img2.features)
    resultV = []
    resultTotal = []
    i = 0
    j = 0
    sum = 0

    while i < img1.features:
        while j < img2.features:
            if (img1.quadrants[i] == img2.quadrants[j]):
                v1 = img1.features[i]
                v2 = img2.features[j]
                k = 0

                while k < len(v1):
                    sum += v1[k] * v2[k]
                    k += 1
                sum = math.sqrt(sum)
                resultV.apped(sum)
                sum = 0

            j += 1

        i += 1
        j = 0
        resultTotal.append(sorted(resultV))
        resultV = []

    return resultTotal


# método que va recibiendo los conjuntos de imágenes por cada detectores
#   y va obtiendo el resultado de compararlas 2 a 2
def comparison(images):
    i = 0
    result = []

    while i < (len(images)-1):
        j = i + 1
        while j < len(images):
            img1 = images[i]
            img2 = images[j]
            result = getResultComparison(img1, img2)
            j += 1
        i += 1


# método que le establece a cada punto de interés de la imagen el cuadrante al que
#   pertenece, dependiendo del centro de cada imagen que es extraído de los ficheros
#   de la base de datos
def setQuadrant(allImages, datasImages):
    cont = 0
    cX = cY = r = -1
    pX = pY = -1
    dImage = []
    i = 0
    j = 0
    vquadrant = []

    for imgsDet in allImages:
        i = 0
        for img in imgsDet:
            cX = datasImages[i][0]
            cY = datasImages[i][1]
            r = datasImages[i][2]
            j = 0
            print "cX: "+ cX + "  " + "cY: " + cY + "  " + "r: " + r
            while j < (len(img.points)-1):
                pX = img.points[j]
                pY = img.points[j+1]
                print "pX: "+ pX + "  " + "pY: " + pY
                if ((int(pX) >= int(cX)) and (int(pY) >= int(cY))):
                    vquadrant.append(1)
                else:
                    if ((int(pX) >= int(cX)) and (int(pY) <= int(cY))):
                        vquadrant.append(4)
                    else:
                        if ((int(pX) <= int(cX)) and (int(pY) <= int(cY))):
                            vquadrant.append(3)
                        else:
                            if ((int(pX) <= int(cX)) and (int(pY) >= int(cY))):
                                vquadrant.append(2)

                j += 2

            img.quadrants = vquadrant
            vquadrant = []
            i += 1



# método que obtiene los datos de cada imagen de la base de datos. La coordenada X e Y
#   del centro de la imagen y el radio del límite exterior
def getDatasImages(files):
    datasImage = []
    mdatasAllImages = []

    for file in files:
        ext = file.split(".")
        if (ext[1] == "txt"):
            with open(PATH_DATABASE_CASIAV4 + file) as f:
                line = f.read().split("\n")
                line = line[0].split(" ")
                datasImage.append(line[0])
                datasImage.append(line[1])
                datasImage.append(line[5])
            mdatasAllImages.append(datasImage)
            datasImage = []

    return mdatasAllImages



if __name__ == "__main__":

    foldersFeaturesSIFT = obteinFolders(PATH_OUTPUTS_FEATURE_EXTRACTION)
    allImages = readFeatures(foldersFeaturesSIFT)
    files = obteinFolders(PATH_DATABASE_CASIAV4)
    datasImages = getDatasImages(files)
    setQuadrant(allImages, datasImages)
    #print allImages[0][0].features
    #print allImages[0][0].points
    print allImages[0][0].quadrants
    #print allImages[1][0].features
    #print allImages[1][0].points
    print allImages[1][0].quadrants
    #print len(allImages[0][0].quadrants)
    #for images in allImages:
    #    comparisonLowe(images)
