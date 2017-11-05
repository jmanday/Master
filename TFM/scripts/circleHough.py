from PIL import Image, ImageDraw
import random
import filtros
import time
from math import sqrt, fabs
import sys

def dibuja_deteccion(imagen, radio, centros):
    """toma como parametros la imagen original, el radio
    y los centros que se detectaron y regresa una imagen con
    los circulos que se encontraron dibujados
    """
    draw = ImageDraw.Draw(imagen)
    x_imagen, y_imagen = imagen.size
    for i in range(len(centros)):
        amarillo = (255, random.randint(120,255), random.randint(0, 40))
        x = centros[i][0]
        y = centros[i][1]
        draw.ellipse((x-radio,y-radio, x+radio,y+radio),
                     fill=None, outline=amarillo)
        draw.ellipse((x-radio,y-radio, x+radio,y+radio),
                     fill=None, outline=amarillo)
        radio = radio + 1
        draw.ellipse((x-radio,y-radio, x+radio,y+radio),
                     fill=None, outline=amarillo)
        radio = radio - 1
        draw.ellipse((x-radio,y-radio, x+radio,y+radio),
                     fill=None, outline=amarillo)
        draw.ellipse((x-1,y-1, x+1,y+1),
                     fill=None, outline="green")
        draw.text((x+2,y+2), str(i), fill="white")
        print ("ID  %s " %i)
    return imagen

def dibuja_circulo(num, radio, imagen):
    """num es el numero de circulos aleatorios que se van a
    dibujar, y la imagen es el canvas en el que se dibuja,
    regresa la imagen con los circulos dibujados
    """
    draw = ImageDraw.Draw(imagen)
    x_imagen, y_imagen = imagen.size
    for i in range(num):
        x = random.randint(radio, x_imagen-radio)
        y = random.randint(radio, y_imagen-radio)
        draw.ellipse((x-radio,y-radio, x+radio,y+radio),
                     fill="black")
        print("Circulo dibujado con centro en (%s, %s) y radio de %s" %(x,y, radio))
    ruido = 1
    for i in range(ruido):
        radio = random.randint(10, 50)
        x = random.randint(radio, x_imagen-radio)
        y = random.randint(radio, y_imagen-radio)
        draw.ellipse((x-radio,y-radio, x+radio,y+radio),
                     fill="black")
        print("Ruido dibujado con centro en (%s, %s) y radio de %s" %(x,y, radio))
    draw.rectangle((10, 10, 90, 90), fill="black", outline="red")
    draw.rectangle((120, 100, 200, 200), fill="black", outline="red")
    return imagen

def crea_imagen():
    """crea una imagen con cierta dim, en blanco
    """
    im = Image.new('RGB', (500,500), (255,255,255))
    return im

def obtiene_votos(pix_x, pix_y, dim, radio):
    """se analiza la imagen, asi cada pixel detectado como
    borde da lugar al circulo con el radio, las celdas que
    pertenecen a ese circulo reciben un voto
    """
    votos = []
    for pos in xrange(dim):
        votos.append([0] * dim)
    for ym in xrange(dim):
        y = dim / 2- ym
        for xm in xrange(dim):
            x = xm - dim / 2
            gx = pix_x[ym, xm][0]
            gy = pix_y[ym, xm][0]
            g = sqrt(gx ** 2 + gy ** 2)
            if fabs(g) > 0:
                cosTheta = gx / g
                sinTheta = gy / g
                xc = int(round(x - radio * cosTheta))
                yc = int(round(y - radio * sinTheta))
                xcm = xc + dim / 2
                ycm = dim / 2 - yc
                if xcm >= 0 and xcm < dim and ycm >= 0 and ycm < dim:
                    votos[ycm][xcm] += 1
    for rango in xrange (1, int(round(dim * 0.1))):
        agregado = True
        while agregado:
            agregado = False
            for y in xrange(dim):
                for x in xrange(dim):
                    v = votos[y][x]
                    if v > 0:
                        for dx in xrange(-rango, rango):
                            for dy in xrange(-rango, rango):
                                if not (dx == 0 and dy == 0):
                                    if y + dy >= 0 and y + dy < dim and x + dx >= 0 and x + dx < dim:
                                        w = votos[y + dy][x + dx]
                                        if w > 0:
                                            if v - rango >= w:
                                                votos[y][x] = v + w
                                                votos[y + dy][x + dx] = 0
                                                agregado = True
    return votos


def detecta_centros(votos, dim):
    """se encarga de detectar los centros
    """
    maximo = 0
    suma = 0.0
    for x in xrange(dim):
        for y in xrange(dim):
            v = votos[y][x]
            suma += v
            if v > maximo:
                maximo = v
    promedio = suma / (dim * dim)
    umbral = (maximo + promedio) / 2.0
    centros = []
    for x in xrange(dim):
        for y in xrange(dim):
            v = votos[y][x]
            if v > umbral:
                print('Posible centro detectado en (%d, %d). ' % (y,x))
                centros.append((y,x))
    return centros

def main():
    """funcion principal
    """
    try:
        radio = int(sys.argv[1])
        num = int(sys.argv[2])
    except:
        print("recuerda escribe el radio y el numero de circulos")
        return
    dim = 500
    im = crea_imagen()
    im = dibuja_circulo(num, radio, im)
    im.save("original.png")
    path = "circulos.png"
    im.save(path)
    im = filtros.abrir_imagen(path)
    im = filtros.hacer_gris(im)
    sobelx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobely = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    Gx = filtros.convolucion(im, sobelx)
    Gy = filtros.convolucion(im, sobely)
    Gx.save("imagenx.png")
    Gy.save("imageny.png")
    votos = list()
    pix_x = Gx.load()
    pix_y = Gy.load()
    votos = obtiene_votos(pix_x, pix_y, dim, radio)
    centros = detecta_centros(votos, dim)
    im = dibuja_deteccion(im, radio, centros)
    im.save("final.png")

main()
