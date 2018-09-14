# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### matching-FlannBased.py
### @Descripcion: script para calcular el matching entre dos conjuntos de
###             de descriptores de dos imágenes usando el algoritmo 
###             Flann en el que se entrena una colección de descriptores
###             de entrenamiento y llama a sus métodos de búsqueda más 
###             cercano para encontar los mejores resultados    
#########################################################################

import os
import sys
import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import csv

PATH_DATABASES_TRAIN_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/train-images3/" #fuente de datos de imágenes segmentadas para comparar
PATH_DATABASES_QUERY_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/query-images3/" #fuente de datos de imágenes a clasificar

class DataMatching:

    def __init__(self, imageSegmented, imageClassifier, value):
        self.imageSegmented = imageSegmented
        self.imageClassifier = imageClassifier
        self.value = value
        
        
def getNameFile(file):
    fileName = ""
    
    if (len(file.split("R")) > 1):
            fileName = file.split("R")[0]
    else:  
        if (len(file.split("L")) > 1):
            fileName = file.split("L")[0] 
    
    return fileName


def matchingFlannBased(filesTrainImages, filesQueryImages):
    valuesDataMatching = []
    results = []
    
    filesTrainImages.sort()
    filesQueryImages.sort()
    
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()
    
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
            kp1, des1 = sift.detectAndCompute(imgQuery,None)
            kp2, des2 = sift.detectAndCompute(imgSeg,None)
            
    
            # FLANN parameters
            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            search_params = dict(checks=100)   # or pass empty dictionary

            flann = cv2.FlannBasedMatcher(index_params,search_params)
            matches = flann.knnMatch(des1,des2,k=2)

            #print(len(matches[0]))
            #max_dist = 0
            #min_dist = 100

            #for m, n in matches:
            #    dist = m.distance
            #    if dist < min_dist:
            #        min_dist = dist
            #    if dist > max_dist:
            #        max_dist = dist 
                    
            good = []
            i = 0
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])

                    #for i,(m,n) in enumerate(matches):
            #    if m.distance < max(2*min_dist, 0.02):
            #        good.append([m])
            
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
        
    with open('results2-FlannBased-SIFT.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Image Query', 'Image Train', "Value matching"])
        
        for rs in results:
            filewriter.writerow([rs['imageQuery'], rs['imageTrain'], rs['value']])
        

if __name__ == "__main__":
    filesTrainImages = os.listdir(PATH_DATABASES_TRAIN_IMAGES)
    filesQueryImages = os.listdir(PATH_DATABASES_QUERY_IMAGES)
    matchingFlannBased(filesTrainImages, filesQueryImages)
    #extra()