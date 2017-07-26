import os
import commands

PATH_EXECUTABLE = "/Users/jesusgarciamanday/Documents/Master/TFM/USITv1.0.3/"
PATH_DATABASES = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/CASIA V4/"
PATH_DATABASES_2 = "/Users/jesusgarciamanday/Documents/Master/TFM/databases/CASIA\ V4/"
PATH_OUTPUTS = "/Users/jesusgarciamanday/Documents/Master/TFM/outputs/segmentation/caht/"

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

    return vnames_images

if __name__ == "__main__":

    images_CASIAV4 = getImagesCASIAV4()
    direc = os.chdir(PATH_EXECUTABLE)

    for img in images_CASIAV4:
        cmd = ("./caht -i " + PATH_DATABASES_2 + img + " -o " + PATH_OUTPUTS + img.split('.')[0] + "-texture.png" + " -s 512 64 -e")

        res = commands.getstatusoutput(cmd)

        if(res[0] != 0):
            print ("Error:" + str(res[0]))
            print ("Descripcion: " + res[1])
