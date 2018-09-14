#########################################################################
### Jesus Garcia Manday
### calculateSuccess.py
### @Descripcion: script que pinta los puntos de interés obtenidos en la
###                 imagen correspondiente
#########################################################################

import os
import sys
import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import csv

PATH_KEYPOINTS = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/lip-vireo-kp-test/"
PATH_IMAGES_KEYPOINTS = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/query-images-test/"


class Detector:
    def __init__(self, numkp):
        self.numkp = numkp
        
        
def getKeypointsFromFile(nameFile):
    nLine = 0
    features = []
    keypoints = []
    
    with open(nameFile, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')        
        for row in spamreader:
            if (nLine != 0):
                res = row[0].split(" ")
                keypoints.append({"px": res[0], "py": res[1]})
            
            nLine += 1
        
        return keypoints
    
    
def drawKeypoint():
    direcImgs = os.listdir(PATH_IMAGES_KEYPOINTS)
    direcImgs.sort()
    
    direcKeypoints = os.listdir(PATH_KEYPOINTS)
    direcKeypoints.sort()
    
    for img in direcImgs:
        nameFileImage = img.split(".")[len(img.split(".")) - 2]
        extension = img.split(".")[len(img.split(".")) - 1]
        nPath = PATH_IMAGES_KEYPOINTS + img
        img = cv2.imread(nPath,0)
        
        for detector in direcKeypoints:
            direcDetector = os.listdir(PATH_KEYPOINTS + detector)
            direcDetector.sort()
            
            for fKeypoint in direcDetector:
                nameFileKeypoint = fKeypoint.split(".")[len(fKeypoint.split(".")) - 2]
                if (nameFileImage == nameFileKeypoint):
                    pathFile = PATH_KEYPOINTS + detector + "/" + fKeypoint
                    keypoints = getKeypointsFromFile(pathFile)
                    
                    for kp in keypoints:
                        cv2.circle(img, (int(kp['px']), int(kp['py'])), 2, (94,206,165,255), -1)
                        cv2.imwrite(nameFileImage + "-" + detector + "-keypoints." + extension , img)
                    
        
    
if __name__ == "__main__":
    drawKeypoint()