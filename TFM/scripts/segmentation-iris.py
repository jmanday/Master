# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### segmentation-iris.py
### @Descripcion: script para realizar la segmentación de las imágenes de
###             iris a través de los datos conocidos de su centro y radio 
###             de las circunferencias que lo delimitan
#########################################################################


import os
import sys
import numpy as np
import cv2
import subprocess
from subprocess import Popen, PIPE
from PIL import Image

PATH_DATABASES_IMAGES = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/images/"
PATH_DATABASES_DATAS = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/datas/"
PATH_DATABASES_IMAGES_SEGMENTED = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/images-segmented/"

class DatasIris:
    
    def __init__(self, positions):
        pos = positions.split()
        self.centerX = pos[0] 
        self.centerY = pos[1]
        self.r = pos[5]
        
        self.startX = int(self.centerX) - int(self.r)
        self.startY = int(self.centerY) - int(self.r)
        self.endX = int(self.centerX) + int(self.r)
        self.endY = int(self.centerY) + int(self.r)
        

def crop(image_path, coords, saved_location):
    image_obj = Image.open(PATH_DATABASES_IMAGES + image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(PATH_DATABASES_IMAGES_SEGMENTED + saved_location)

    
def segmentationIris(filesImages, filesDatas):
    
    filesImages.sort()
    filesDatas.sort()
    
    datasIris = []
    
    for fd in filesDatas:
        process = Popen(['cat', PATH_DATABASES_DATAS + fd], stdout=PIPE, stderr=PIPE) 
        stdout, stderr = process.communicate()
        stdout = stdout.decode("utf-8")

        di = DatasIris(stdout)
        datasIris.append(di)
        
    for (fi,di) in zip(filesImages, datasIris):
        #cropped = img1[di.startX:di.startY, di.endX:di.endY]
        #cv2.imwrite(PATH_DATABASES_IMAGES_SEGMENTED + fi, cropped)   
        crop(fi, (di.startX, di.startY, di.endX, di.endY), fi)
        

if __name__ == "__main__":
    filesImages = os.listdir(PATH_DATABASES_IMAGES)
    filesDatas = os.listdir(PATH_DATABASES_DATAS)
    
    segmentationIris(filesImages, filesDatas)
