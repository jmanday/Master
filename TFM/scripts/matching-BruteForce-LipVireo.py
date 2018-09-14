# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### matching-BruteForce-LipVireo.py
### @Descripcion: script para calcular el matching entre dos conjuntos de
###             de descriptores de dos imágenes usando el algoritmo 
###             fuerza bruta en el que por cada descriptor en el primer
###             conjunto busca el descriptor más cercano en el segundo
###             conjunto probando uno a uno. Usando el detector SIFT. Esta
###             variante presenta que se han utilizado los detectores de 
###             puntos de interés de Harris-Laplace, Hessian-Laplace y
###             Fast-Hessian dentro de la librería Lip-Vireo.
#########################################################################

import os
import sys
import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import csv

PATH_OUTPUTS_DES_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/lip-vireo-des-time/"

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
    
    
def matchingBruteForce(desFilesTrainImages, desFilesQueryImages, descriptor, detector):
    print(descriptor, "---", detector)
  
    valuesDataMatching = []
    results = []
    
    desFilesQueryImages.sort()
    desFilesTrainImages.sort()
    
    for desImgQuery in desFilesQueryImages:
        nMatch = 0
        index = 0
        firstImage = ""
    
        nameImgQuery  = getNameFile(desImgQuery)
        des1 = generateDescriptorFromFile(PATH_OUTPUTS_DES_IMAGES + descriptor + "/" + detector + "/query-images/" + desImgQuery)
        
        for desImgTrain in desFilesTrainImages:
            nameImgTrain  = getNameFile(desImgTrain)
            des2 = generateDescriptorFromFile(PATH_OUTPUTS_DES_IMAGES + descriptor + "/" + detector + "/train-images/" + desImgTrain)
            
            # BFMatcher with default params
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(np.asarray(des1,np.float32), np.asarray(des2,np.float32), k=2)
         
            # Apply ratio test
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
            
            if ((nameImgTrain == firstImage) or (firstImage == "")):
                nMatch = nMatch + len(good)
            else:
                valuesDataMatching.append({"imageQuery": nameImgQuery, "imageTrain": firstImage, "value": nMatch})        
                nMatch = len(good)
                
            firstImage = nameImgTrain
            
        firstImage = ""
        nMatch = 0
        
        valM = max(valuesDataMatching, key=lambda item:item['value'])
        print(valM)
        results.append(valM)
        valuesDataMatching = []
        
    
    nameCSV = "results-BruteForce-" + descriptor + "-" + detector + ".csv"
    with open(nameCSV, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Image Query', 'Image Train', "Value matching"])
        
        for rs in results:
            filewriter.writerow([rs['imageQuery'], rs['imageTrain'], rs['value']])
        

def getFilesFromDescriptor(descriptor):
    desFilesImages = []
    path = PATH_OUTPUTS_DES_IMAGES + descriptor
    direc = os.listdir(path)
    direc.sort()
    nPath = ""
    
    for d in direc:
        nPath = path + "/" + d
        dirs = os.listdir(nPath)
        print(nPath)
                
        for d2 in dirs:
            files = os.listdir(nPath + "/" + d2)
            desFilesImages.append(files)
         
        matchingBruteForce(desFilesImages[0], desFilesImages[1], descriptor, d) 
        desFilesImages.clear()
        
        
if __name__ == "__main__":
    nameDesc = sys.argv[1]
    getFilesFromDescriptor(nameDesc)