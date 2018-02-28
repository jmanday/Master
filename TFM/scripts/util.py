# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### util.py
### @Descripcion: script donde implementar métodos que sean de utilidad
###     para el resto de scripts
#########################################################################


import os
import commands
import sys
import shutil


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
