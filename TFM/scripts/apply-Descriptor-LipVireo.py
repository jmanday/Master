# -*- coding: utf-8 -*-

#################################################################################
### Jesus Garcia Manday
### apply-Descriptor-LipVireo.py
### @Descripcion: script para obtener los ficheros descriptores de los puntos
###             de interés de cada imagen
###
### @Params: 
###     - detector: el tipo de detector de puntos de interés a aplicar
###     - descriptor: el tipo de descriptor de puntos de interés a aplicar
###     - pathSource: path origen donde se almacenan las imágenes
###     - pathDestiny: path destino donde se van a almacenar los ficheros ".pkeys"
###
### @Execute: ./lip-vireo -dir ../databases/images-grouped/reflexion-especular/ -d hesslap -p SURF 
###         -dsdir ../outputs/lip-vireo-kp-images/reflexion-especular/SURF/hesslap/ -c lip-vireo.conf
###################################################################################


import os
import subprocess
from subprocess import Popen, PIPE
import sys


def applyDescriptor(detector, descriptor, pathSource, pathDestiny):
    cmd = "./lip-vireo -dir " + pathSource " -d " + detector " -p " + descriptor + " -dsdir " + pathDestiny + " -c lip-vireo.conf"
    os.system(cmd)

if __name__ == "__main__":
    detector = sys.argv[1]
    descriptor = sys.argv[2]
    pathSource = sys.argv[3]
    pathDestiny = sys.argv[4]
    
    applyDescriptor(detector, descriptor, pathSource, pathDestiny)
    
    
    