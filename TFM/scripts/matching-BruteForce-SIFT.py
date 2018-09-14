# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### matching-BruteForce-SIFT.py
### @Descripcion: script para calcular el matching entre dos conjuntos de
###             de descriptores de dos imágenes usando el algoritmo 
###             fuerza bruta en el que por cada descriptor en el primer
###             conjunto busca el descriptor más cercano en el segundo
###             conjunto probando uno a uno. Usando el detector SIFT. 
#########################################################################

import os
import sys
import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import csv
from random import seed
from random import randint
import shutil
import random

PATH_DATABASES_TRAIN_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/lip-vireo-des-images/" #fuente de datos de imágenes segmentadas para comparar
PATH_DATABASES_TEST_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/lip-vireo-des-images/" #fuente de datos de imágenes a clasificar
PATH_DESTINY = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/lip-vireo-des-images/reflexion-especular/SIFT/log" 


class DataMatching:
    def __init__(self, imageQuery, imageTrain, value):
        self.imageQuery = imageQuery
        self.imageTrain = imageTrain
        self.value = value
        

def getNameFile(file):
    fileName = ""
    
    if (len(file.split("R")) > 1):
            fileName = file.split("R")[0]
    else:  
        if (len(file.split("L")) > 1):
            fileName = file.split("L")[0] 
    
    return fileName


def selectionImageTest(path):
    originDirec = os.chdir(path)
    dataSet = os.listdir(originDirec)
    
    count = 0
    i = 0
    index = 0
    test = []
    train = []
    sizeDataset = len(dataSet)
    numTest = int(len(dataSet) * 0.2)
    numTrain = len(dataSet) - numTest

    imgTest = random.sample(range(sizeDataset), sizeDataset)
    
    while count < sizeDataset:
        if ((sizeDataset - i) >= numTest):
            count += numTest
            while i < count:
                #print (imgTest[i])
                test.append(imgTest[i])
                i += 1

            if index == 0:
                j = i
                while j < sizeDataset:
                    #print (imgTest[j])
                    train.append(imgTest[j])
                    j += 1
            else:
                z = 0
                j = i
                while z < (index * numTest):
                    #print (imgTest[z])
                    train.append(imgTest[z])
                    z += 1

                while j < sizeDataset:
                    #print (imgTest[j])
                    train.append(imgTest[j])
                    j += 1

            index += 1        

            print ("=================COPIANDO=================")
            
            for fileTest in test:
                shutil.copy(dataSet[fileTest], PATH_DESTINY + str(index) + "/test/" + dataSet[fileTest])
                
            for fileTrain in train:
                shutil.copy(dataSet[fileTrain], PATH_DESTINY + str(index) + "/train/" + dataSet[fileTrain])
                
            test.clear()
            train.clear()
        else:
            count = sizeDataset
    
    
    
def matchingBruteForceSIFT(pathFilesTest, pathFilesTrain):
    dataSetTest = os.listdir(PATH_DATABASES_TEST_IMAGES + pathFilesTest)
    dataSetTrain = os.listdir(PATH_DATABASES_TRAIN_IMAGES + pathFilesTrain)
    
    valuesDataMatching = []
    results = []
    
    dataSetTest.sort()
    dataSetTrain.sort()
    
    # Initiate SIFT detector
    #sift = cv2.SIFT()
    sift = cv2.xfeatures2d.SIFT_create()
    
    for fImgQuery in dataSetTest:
        nMatch = 1000000
        imageMatching = ""
        index = 0
        firstImage = ""
        imgTest = cv2.imread(PATH_DATABASES_TEST_IMAGES + pathFilesTest + fImgQuery,0)
        
        nameImgQuery = getNameFile(fImgQuery)
    
        for fImgTrain in dataSetTrain:
            imgTrain = cv2.imread(PATH_DATABASES_TRAIN_IMAGES + pathFilesTrain + fImgTrain,0)
            
            nameImgTrain  = getNameFile(fImgTrain)
    
            # find the keypoints and descriptors with SIFT
            kp1, des1 = sift.detectAndCompute(imgTest,None)
            kp2, des2 = sift.detectAndCompute(imgTrain,None)
            
            # BFMatcher with default params
            bf = cv2.BFMatcher()
            
            matches = bf.knnMatch(des1,des2, k=2)

            # Apply ratio test
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])
                    
            if (len(good) < nMatch):
                nMatch = len(good)
                imageMatching = nameImgTrain
         
        
        valuesDataMatching.append({"imageQuery": nameImgQuery, "imageMatching": imageMatching, "value": nMatch})    
        firstImage = ""
        nMatch = 0
        
        results.append(valuesDataMatching)
        valuesDataMatching = []
        
    print (len(results))
        
      
    with open('results2-BruteForce-SIFT.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Image Query', 'Image Train', "Value matching"])
        
        for rs in results:
            filewriter.writerow([rs['imageQuery'], rs['imageTrain'], rs['value']])

        
if __name__ == "__main__":
    #filesTrainImages = os.listdir(PATH_DATABASES_TRAIN_IMAGES)
    #filesQueryImages = os.listdir(PATH_DATABASES_QUERY_IMAGES)
    #selectionImageTest(sys.argv[1])
    matchingBruteForceSIFT(sys.argv[1], sys.argv[2])