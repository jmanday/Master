# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### matching-BruteForce.py
### @Descripcion: script para calcular el matching entre dos conjuntos de
###             de descriptores de dos imágenes usando el algoritmo 
###             fuerza bruta en el que por cada descriptor en el primer
###             conjunto busca el descriptor más cercano en el segundo
###             conjunto probando uno a uno. Usando el detector ORB.
#########################################################################

import os
import sys
import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import csv

PATH_DATABASES_TRAIN_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/train-images4/" #fuente de datos de imágenes segmentadas para comparar
PATH_DATABASES_QUERY_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/query-images4/" #fuente de datos de imágenes a clasificar

class DataMatching:
    
    def __init__(self, imageSegmented, imageClassifier):
        self.imageSegmented = imageSegmented
        self.imageClassifier = imageClassifier
      
    
def getNameFile(file):
    fileName = ""
    
    if (len(file.split("R")) > 1):
            fileName = file.split("R")[0]
    else:  
        if (len(file.split("L")) > 1):
            fileName = file.split("L")[0] 
    
    return fileName


def matchingBruteForceORB(filesTrainImages, filesQueryImages):
    valuesDataMatching = []
    results = []
    
    filesTrainImages.sort()
    filesQueryImages.sort()
    
    # Initiate ORB detector
    orb = cv2.ORB_create()
    
    for fImgQuery in filesQueryImages:
        nMatch = 0
        index = 0
        firstImage = ""
        imgQuery = cv2.imread(PATH_DATABASES_QUERY_IMAGES + fImgQuery,0)
        
        nameImgQuery = getNameFile(fImgQuery)
    
        for fImgTrain in filesTrainImages:
            imgSeg = cv2.imread(PATH_DATABASES_TRAIN_IMAGES + fImgTrain,0)
            
            nameImgTrain  = getNameFile(fImgTrain)
            
            # find the keypoints and descriptors with SIFT
            kp1, des1 = orb.detectAndCompute(imgQuery,None)
            kp2, des2 = orb.detectAndCompute(imgSeg,None)
            
            # BFMatcher with default params
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1,des2, k=2)
           
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
        
            
    with open('results2-BruteForce-ORB.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Image Query', 'Image Train', "Value matching"])
        
        for rs in results:
            filewriter.writerow([rs['imageQuery'], rs['imageTrain'], rs['value']])
     
     
    
if __name__ == "__main__":
    filesTrainImages = os.listdir(PATH_DATABASES_TRAIN_IMAGES)
    filesQueryImages = os.listdir(PATH_DATABASES_QUERY_IMAGES)
    matchingBruteForceORB(filesTrainImages, filesQueryImages)