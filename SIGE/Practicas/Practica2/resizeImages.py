import sys, os, re, traceback
from PIL import Image
from skimage.io import imread, imsave
from resizeimage import resizeimage

cwd = os.getcwd()
rootDir = cwd + '/imagenes'


for file_name in os.listdir(rootDir):
    folderDir = rootDir + '/' + file_name
    if (os.path.isdir(folderDir)):
        fileImages = os.listdir(folderDir)
        for fImage in fileImages: # para cada imagen
            if os.path.splitext(fImage)[1] == '.jpg':
                nameFileDir = folderDir + '/' + fImage
            # redimensiono la imagen a 256x256
                print(nameFileDir)
                with open(nameFileDir, 'r+b') as f:
                    with Image.open(f) as image:
                        cover = resizeimage.resize_cover(image, [256, 256])
                        cover.save(nameFileDir, image.format)
    else:
        with open(folderDir, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [256, 256])
                cover.save(folderDir, image.format)
