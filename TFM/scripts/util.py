# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### util.py
### @Descripcion: script donde implementar métodos que sean de utilidad
###     para el resto de scripts
#########################################################################


import os
import subprocess
from subprocess import Popen, PIPE
import sys
import shutil
from random import seed
from random import randint

PATH_SOURCE = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/" #path donde se almacena la base de datos de las imágenes

# método para mover algunos ficheros a un directorio destino
def copySeveralFilesToPath(originPath, destinyPath):
    n = 0
    
    #print(originPath)
    #print(destinyPath)
    
    #originDirec = os.chdir(originPath)
    files = os.listdir(originPath)
    files.sort()
    
    files2 = os.listdir(destinyPath)
    files2.sort()
    
    for f in files:
        name = f.split(".")[0]
    
        for f2 in files2:
            name2 = f2.split(".")[0]
            
            if (name == name2):
                #shutil.move(f, destinyPath + f)
                shutil.move(destinyPath + f2, destinyPath + "query-images/"+ f2)
    

# método para copiar ficheros de una forma aleatoria de un directorio a otro
def copyRandomFiles(originPath):            
    listDirecDestiny = ["images-grouped/oclusion/", "images-grouped/iluminacion-variable/", "images-grouped/reflexion-especular/"]
    originDirec = os.chdir(originPath)
    files = os.listdir(originDirec)
    
    maxRandom = 70
    value = 0
    count = 0
    lastCounted = 0
    numFiles = len(files)
    indexDirecDestiny = 0
    
    # seed random number generator
    seed(1)
    
    # generate some integers
    while (numFiles > 0):
        value = randint(0, maxRandom)
        indexDirecDestiny = randint(0, 2)
        lastCounted = count + value
        
        while (count < (lastCounted)):
            shutil.copy(files[count], PATH_SOURCE + listDirecDestiny[indexDirecDestiny] + files[count])
            count += 1
            
        numFiles -= value
        
        if(numFiles < maxRandom):
            maxRandom = numFiles
                
    
    
    #for f in files:
        #print(PATH_SOURCE + "images-grouped/" + listDirecDestiny[0])
        #print(PATH_SOURCE + "images-grouped/" + listDirecDestiny[1])
        #print(PATH_SOURCE + "images-grouped/" + listDirecDestiny[2])
    
    
# método para copiar ficheros de un determinado formato a un directorio destino
def copyFilesToPathByFormat(originPath, destinyPath, formatFile):
    originDirec = os.chdir(originPath)
    files = os.listdir(originDirec)
    
    
    for f in files:
        if f.split(".")[len(f.split(".")) - 1] == formatFile:
            shutil.copy(f, destinyPath + f)
    


    
    
# método que obtiene una selección de un 20% de imágenes para test y un 80% para entrenamiento
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
    
         

# método modifica el nombre a ficheros
def changeNameFiles(path):
    nameFiles = []

    direc = os.chdir(path)
    cmd = ("ls")
    res = commands.getstatusoutput(cmd)

    if res[0] == 0:
        names = res[1].split()

    for folder in names:
        path = PATH_OUTPUTS_FEATURE_EXTRACTION + folder + "/"
        cmd = ("ls " + path)
        res = commands.getstatusoutput(cmd)

        if res[0] == 0:
            nameFiles = res[1].split()

        for name in nameFiles:
            aux = (name.split("-"))[1].split(".")
            new_name = aux[0] + "." + aux[2]
            shutil.move(path + name, path + new_name)
            

# método que calcula la traspuesta de una matriz que
#   se le pasa por parámetro
def transpose(matrix):
    maux = []
    vrow = []
    i = 0
    j = 0

    while i < len(matrix):
        for row in matrix:
            vrow.append(row[i])
        maux.append(vrow)
        vrow = []
        i += 1

    matrix = maux
    return matrix


def getNameSplit(nameFile):
    fileName = ""

    if (len(nameFile.split("R")) > 1):
            fileName = nameFile.split("R")[0]
    else:  
        if (len(nameFile.split("L")) > 1):
            fileName = nameFile.split("L")[0] 
                
                
    return fileName


# método que devuelve el nombre de un fichero eliminando
#   los caracteres numéricos que exista
def getNameFiles(path):
    count = 0
    num = 0
    nFiles = 0
    saveFiles = []
    auxFileName = ""
    listNameFiles = [] 
    files = os.listdir(path)
    files.sort()

    for file in files:
        fileName = ""

        if (len(file.split("R")) > 1):
                fileName = file.split("R")[0]
        else:  
            if (len(file.split("L")) > 1):
                fileName = file.split("L")[0] 
    
        if (auxFileName == ""):
            count += 1
        else:  
            if (fileName != auxFileName):
                listNameFiles.append({"file": auxFileName, "count": count})
                count = 0
            
            count += 1
        
        auxFileName = fileName
            
    if (count != 0):
        listNameFiles.append({"file": fileName, "count": count})

    # sólo nos quedamos con las imágenes que tengan como mínimo 10 instancias     
    for f in listNameFiles:
        if (f["count"] >= 10):
            saveFiles.append(f["file"])

    return saveFiles


# método que crea una nueva carpeta donde se van a almacenar las imágenes que se
#   utilizarán de entrenamiento. Recibe el nombre de las imágenes que tienen más 
#   10 instancias y de cada una de ellas copia 5 instancias del ojo derecho y otras
#   5 instancias del ojo izquierdo en una nueva carpeta "train-images3"
def createTrainImages(path, destinyPath, nameFiles):
    numFilesR = 0
    numFilesL = 0
    firstName = ""
    listNameFiles = [] 
    files = os.listdir(path)
    files.sort()
        
    for file in files:
        name = getNameSplit(file)
        
        if (firstName != "") and (name != firstName):
            numFilesR = 0
            numFilesL = 0
            
        if (name in nameFiles):
            firstName = name
            if (len(file.split("L")) > 1) and (numFilesL < 5):
                listNameFiles.append(file)
                numFilesL += 1

            if (len(file.split("R")) > 1) and (numFilesR < 5):
                listNameFiles.append(file)
                numFilesR += 1
      
    for f in listNameFiles:
        shutil.copy(path + "/" + f, destinyPath + "/" + f)
        #print(path + "/" + f + "-----" + destinyPath + "/" + f)

        
# método que crea una nueva carpeta donde se van a almacenar las imágenes que se
#   utilizarán para clasificarlas. Recibe el nombre de las imágenes que tienen más 
#   10 instancias y de la carpeta donde están todas las imágenes a clasificar sólo
#   selecciona las que estan en ese conjunto, copiándolas a nuevo directorio llamado
#   "query-images3"
def createQueryImages(path, destinyPath, nameFiles):
    files = os.listdir(path)
    files.sort()
    
    for file in files:
        name = getNameSplit(file)
        if (name in nameFiles):
            #print(path + "/" + file, destinyPath + "/" + file)
            shutil.copy(path + "/" + file, destinyPath + "/" + file)
    
    
           
    
if __name__ == "__main__":
    copyRandomFiles(sys.argv[1])