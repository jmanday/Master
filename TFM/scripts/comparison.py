#########################################################################
### Jesus Garcia Manday
### segmentation.py
### @Descripcion: script para realizar la segmentacion de las imagenes de
###             iris y obtener la textura del mismo a traves de dos
###             metodos posibles "caht" y "wahet"
#########################################################################


import os
import commands
import sys
import pandas as pd

PATH_EXECUTABLE = "/Users/jesusgarciamanday/Documents/Master/TFM/USITv1.0.3/"
PATH_DATABASES = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/CASIA V4/"
PATH_DATABASES_2 = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/CASIA\ V4/"
PATH_OUTPUTS = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/segmentation/"
PATH_OUTPUTS2 = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/feature extraction/"


def getImagesCASIAV4():
    vnames_images = []
    direc = os.chdir(PATH_DATABASES)
    cmd = ("ls " + PATH_DATABASES_2)

    res = commands.getstatusoutput(cmd)

    if res[0] == 0:
        vimages = res[1].split()
        for img in vimages:
            name_img = img.split('.')
            if name_img[1] == 'jpg':
                vnames_images.append(img)

    else:
        print ("Error:" + str(res[0]))
        print ("Descripcion: " + res[1])

    df = pd.DataFrame([[img, 0, 0, 0, 0, 0, 0, 0] for img in vnames_images], columns = ['image', 'lg', 'qsw', 'ko', 'cr', 'cb', 'dct', 'gfcf'])
    df.to_csv(PATH_OUTPUTS2 + 'results.csv', index=False)

    return vnames_images



if __name__ == "__main__":

    #mode_seg = sys.argv[1]
    images_CASIAV4 = getImagesCASIAV4()
        #direc = os.chdir(PATH_EXECUTABLE)

        #for img in images_CASIAV4:
        #    cmd = ("./" + mode_seg + " -i " + PATH_DATABASES_2 + img + " -o " + PATH_OUTPUTS + "/" + mode_seg + "/" + img.split('.')[0] + "-texture.png" + " -s 512 64 -e")

        #    res = commands.getstatusoutput(cmd)

        #    if(res[0] != 0):
        #        print ("Error:" + str(res[0]))
        #        print ("Descripcion: " + res[1])
