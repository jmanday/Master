#############################################################
# Este script toma de entrada un csv que lo recorre por fila
#   y se queda con el mayor valor de cada una y la columna a la
#   que pertenece. Para el problema de MNIST cada fila tiene 10
#   columnas y un valor de pertenencia cada una al número representado
#   por su columna, es decir, en cada fila obtenemos un valor de pertenencia
#   a los números de 0 al 9
#############################################################

import pandas as pd
import numpy as np

df = pd.read_csv('./submission4.csv')
labels = []

for index, row in df.iterrows():
   nummax = row.max()
   for n in range(0, len(row)-1):
       if (nummax == row[n]):
           labels.append(n)

for i in labels:
    print(i,  end='')
