#########################################################################
### Jesus Garcia Manday
### calculateSuccess.py
### @Descripcion: script que calcula el porcentaje de acierto en la 
###                 comparación de las imágenes. Recoge como entrada un
###                 fichero csv con los campos "Image Classifier", "Image
###                 Matching" y "Value", donde dice a cada imagen a 
###                 clasificar que imagen de matching es la que mayor valor
###                 ha obtenido de compararlas con todas
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
    count = 0
    success = 0
    
    res = fileName.split("/")
    name = res[len(res)-1]
    
    detector = name.split("-")[len(name.split("-")) - 1]
    detector = detector.split(".")[0]
    descriptor = name.split("-")[len(name.split("-")) - 2]
    
    print("\nDetector: ", detector, "    ", "Descriptor: ", descriptor)    
    
    with open(fileName, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')        
        for row in spamreader:
            if (count != 0):
                if (row[0] == row[1]):
                    success += 1
                
            count += 1

    result = (success/count) * 100
    print("Precisión: ", result, "%\n")        
    
    
if __name__ == "__main__":
    fileName = sys.argv[1]
    upperMatching (fileName)