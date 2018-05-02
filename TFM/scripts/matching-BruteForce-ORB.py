# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### matching-BruteForce.py
### @Descripcion: script para calcular el matching entre dos conjuntos de
###             de descriptores de dos imágenes usando el algoritmo 
###             fuerza bruta en el que por cada descriptor en el primer
###             conjunto busca el descriptor más cercano en el segundo
###             conjunto probando uno a uno
#########################################################################

import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 

img1 = cv2.imread('S1001L04.jpg',0) # queryImage
img2 = cv2.imread('S1001L05.jpg',0) # trainImage
imgOut = cv2.imread('S1001L05.jpg',0) 

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], imgOut, flags=2)
#plt.imshow(img3),plt.show()