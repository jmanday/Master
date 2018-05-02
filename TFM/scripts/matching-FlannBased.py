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

import numpy as np
import cv2
import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt 

img1 = cv2.imread('thumbnail.png',0) # queryImage
img2 = cv2.imread('thumbnail.png',0) # trainImage
imgOut = cv2.imread('S1001L05.jpg',0) 

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k=2)

max_dist = 0
min_dist = 100

for m, n in matches:
    dist = m.distance
    if dist < min_dist:
        min_dist = dist
    if dist > max_dist:
        max_dist = dist       

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]

good = []
for i,(m,n) in enumerate(matches):
    if m.distance < max(2*min_dist, 0.02):
        good.append([m])
        
print(len(good))        
# ratio test as per Lowe's paper
#for i,(m,n) in enumerate(matches):
#    if m.distance < 0.7*n.distance:
#        matchesMask[i]=[1,0]
        
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

print(len(matchesMask))
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
plt.imshow(img3,),plt.show()