#########################################################################
### Jesus Garcia Manday
### resultFilter.py
### @Descripcion:            
#########################################################################

import os
import sys
import numpy as np
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 
import csv

PATH_SCRIPTS = "/Users/jesusgarciamanday/Documents/Master/TFM/scripts/"

class DataMatching:
    def __init__(self, imageClassifier, imageMatching, value):
        self.imageClassifier = imageClassifier
        self.imageMatching = imageMatching
        self.value = value
        

def upperMatching(fileName):
    valuesDataMatching = [] 
    nameFirstFile = ""
    nMatch = 0
    nameFileMatching = ""
    
    with open(fileName, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')        

        for row in spamreader:
            print(row)
            res = row[0].split(",")
            if (len(res) > 1):
                if (nameFirstFile == ""):
                    nameFirstFile = res[0]

                if (nameFirstFile == res[0]):
                    if (int(res[2]) > nMatch):
                        nMatch = int(res[2])
                        nameFileMatching = res[1]
                else:
                    dm = DataMatching(nameFirstFile, nameFileMatching, nMatch)
                    valuesDataMatching.append(dm)
                    nMatch = 0
                    nameFirstFile = res[0]
                    if (int(res[2]) > nMatch):
                        nMatch = int(res[2])
                        nameFileMatching = res[1]
    
    
    with open('resultFilter-'+ fileName, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Image Classifier', 'Image Matching', "Value"])
        
        for dm in valuesDataMatching:
            filewriter.writerow([dm.imageClassifier, dm.imageMatching, dm.value])
            
            
if __name__ == "__main__":
    fileName = sys.argv[1]
    upperMatching (fileName)