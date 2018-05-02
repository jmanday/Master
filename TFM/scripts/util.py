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

# método para copiar ficheros a un directorio destino
def copyFilesToPath(originPath, destinyPath, formatFile):
    originDirec = os.chdir(originPath)
    files = os.listdir(originDirec)
    
    
    #proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
    #output = proc.stdout.read() 
    #output = output.decode("utf-8")
    #files = output.split()
    
    for f in files:
        if f.split(".")[len(f.split(".")) - 1] == formatFile:
            shutil.copy(f, destinyPath + f)
    

    
    #proc2 = subprocess.Popen(['cat', aux[1]], stdout=subprocess.PIPE)
    #output2 = proc2.stdout.read()
    #print(output2)
    #aux2 = output2.split()
    #print(aux2[1])
    
    # the function call Popen start a process in Python. You can start any program with any parameter
    #process = Popen(['cat', aux[1]], stdout=PIPE, stderr=PIPE) 
    
    # Reads input and output from the process. 'stdout' is the process out and 'stderr' will be write
    #   only if an error occurs. If you want to wait for the program to finish you can call Popen.wait()
    #stdout, stderr = process.communicate()
    #print(stdout)
    
    

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


if __name__ == "__main__":
    copyFilesToPath(sys.argv[1], sys.argv[2], sys.argv[3])