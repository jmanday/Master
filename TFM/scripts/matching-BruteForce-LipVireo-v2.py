# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### matching-BruteForce-LipVireo-v2.py
### @Description: script para calcular el matching entre dos conjuntos de
###             de descriptores de dos imágenes usando el algoritmo 
###             fuerza bruta en el que por cada descriptor en el primer
###             conjunto busca el descriptor más cercano en el segundo
###             conjunto probando uno a uno. Usando el detector SIFT. Esta
###             variante presenta que se han utilizado los detectores de 
###             puntos de interés que se encuentran dentro de la
###             librería Lip-Vireo junto con el descriptor SIFT.
###
### @Params: en los parámetros para la ejecución hay que indicarle el path 
###             relativo donde se almacenan dos carpetas "test" y "train" cada
###             una de ellas con los respectivos ficheros ".pkeys" donde se 
###             encuentra la información de las características de cada punto
###             de interés
###
### @Output: la salida genera un fichero csv donde se indicará por cada imagen
###             del conjunto de test es clasificada por su distancia
#########################################################################

import os
import sys
import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import csv

PATH_OUTPUTS_DES_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/lip-vireo-des-images/"

class Descriptor:
    def __init__(self, numkp, m, d):
        self.numkp = numkp
        self.m = m
        self.d = d
        

def getNameFile(file):
    fileName = ""
    
    if (len(file.split("R")) > 1):
            fileName = file.split("R")[0]
    else:  
        if (len(file.split("L")) > 1):
            fileName = file.split("L")[0] 
    
    return fileName


def generateDescriptorFromFile(nameFile):
    nLine = 0
    features = []
    descriptors = []

    with open(nameFile, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')   
        for row in spamreader:
            if (nLine == 0):
                res = row[0].split(" ")
                des = Descriptor(int(res[0]), int(res[1]), int(res[2]))
            else:
                if (nLine >= 2):
                    feature = row[0].split(" ")
                    
                    if (len(features) < des.d):
                        for f in feature:
                            if (f != ''):
                                features.append((float(f)))
                    else:
                        descriptors.append(features)
                        features = []
            
            
            nLine += 1  
        
        descriptors.append(features)
        return descriptors
    
    
def matchingBruteForce(desFilesTestImages, desFilesTrainImages, path, det):
  
    valuesDataMatching = []
    results = []
    
    desFilesTestImages.sort()
    desFilesTrainImages.sort()
    
    for desImgTest in desFilesTestImages:
        nMatch = 0
        index = 0
        firstImage = ""
        imageMatching = ""
    
        nameImgTest  = getNameFile(desImgTest)
        des1 = generateDescriptorFromFile(path + "/test/" + desImgTest)
        
        for desImgTrain in desFilesTrainImages:
            nameImgTrain  = getNameFile(desImgTrain)
            des2 = generateDescriptorFromFile(path + "/train/" + desImgTrain)
            
            # BFMatcher with default params
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(np.asarray(des1,np.float32), np.asarray(des2,np.float32), k=2)
         
            # Apply ratio test
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
            print(nameImgTest + "-------" + nameImgTrain + "------" + str(len(good)))
            if (len(good) > nMatch):
                nMatch = len(good)
                imageMatching = nameImgTrain
            
            
        results.append({"nameImgTest": nameImgTest, "imageMatching": imageMatching, "value": nMatch}) 
        nMatch = 0
        imageMatching = ""
        
    
    nameCSV = "results-BruteForce-LipVireo-" + det + ".csv"
    with open(nameCSV, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Image Test', 'Image Matching', "Value matching"])
        
        for rs in results:
            filewriter.writerow([rs['nameImgTest'], rs['imageMatching'], rs['value']])
        
        

def getFilesFromDescriptor(path):
    desFilesImages = []
    path = PATH_OUTPUTS_DES_IMAGES + path
    direc = os.listdir(path)
    direc.sort()
    det = path.split("/")[len(path.split("/"))-1]
    nPath = ""
 
    for d in direc:
        nPath = path + "/" + d
        files = os.listdir(nPath)
        desFilesImages.append(files)

    matchingBruteForce(desFilesImages[0], desFilesImages[1], path, det)
   


if __name__ == "__main__":
    path = sys.argv[1]
    getFilesFromDescriptor(path)