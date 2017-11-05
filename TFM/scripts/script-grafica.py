# -*- coding: utf-8 -*-

#########################################################################
### Jesus Garcia Manday
### gauus.py
### @Descripcion: script to remove noise and apply blur the images
#########################################################################
from pylab import *

# modo selección ruleta
#list_algorithm_standar = [50661514,49454108,50072070,49191732]
#list_baldwiniana_1 = [50792366,49517434,50794922,50877986]
#list_baldwiniana_2 = [50901102,50392602,50802690,49648598]
#list_lamarckiana_1 = [50122474,49028596,50508862,49110542]
#list_lamarckiana_2 = [46408866,46006206,46553166,]

# modo selección SUS
#list_algorithm_standar = [50273578,49329032,50216268,49434430]
#list_baldwiniana_1 = [50683186,50781330,50919170,50440568]
#list_baldwiniana_2 = [50825588,50217826,51286552,49278444]
#list_lamarckiana_1 = [50765156,50234604,51216522,49255100]

# modo selección windowing
#list_algorithm_standar = [50380114,49552898,50498542,49107762]
#list_baldwiniana_1 = [50225420,50661008,50403078,50593082]
#list_baldwiniana_2 = [50718064,48546414,50572490,49024386]
#list_lamarckiana_1 = [51074406,48890590,50887400,49298502]

# modo selección ranking lineal
#list_algorithm_standar = [50793058,48643766,50156414,50156414]
#list_baldwiniana_1 = [50361474,50665166,50525924,50810558]
#list_baldwiniana_2 = [51136236,49235864,51079706,49273562]
#list_lamarckiana_1 = [50711134,48793998,50945016,49362510]

# modo selección ranking exponencial
#list_algorithm_standar = [50247668,49131524,50547556,49261630]
#list_baldwiniana_1 = [50470978,50824368,50431952,50588086]
#list_baldwiniana_2 = [51152236,49750956,50972250,49260286]
#list_lamarckiana_1 = [50796336,49217622,50750950,49419134]

# modo selección por torneo
list_algorithm_standar = [50805012,50199064,50611516,50125284]
list_baldwiniana_1 = [96,97,98,99,96,95,96,97,98,99,97,96,95,98,97,97,97,97,99,95,99,96,97,98,96,97,96,98,98,97]
list_baldwiniana_2 = [90,91,92,91,90,92,93,94,95,92,94,93,92,91,90,93,91,95,91,93,92,93,91,92,92,94,96,92,91,93]
list_lamarckiana_1 = [80,81,82,81,80,82,83,84,85,82,84,83,82,81,80,83,81,85,81,80,82,83,84,86,82,84,81,80,81,84]

#plt.plot(list_algorithm_standar)  # Dibuja el gráfico de la lista list_algorithm_standar
plt.xlabel("Rank")   # Inserta el título del eje X
plt.ylabel("Tasa de segmentación del iris")   # Inserta el título del eje Y
#plt.plot(list_algorithm_standar, marker='x', linestyle=':', color='b', label = "Algoritmo estándar")
plt.plot(list_baldwiniana_1, marker='*', linestyle='-', color='y', label = "Método propuesto")
plt.plot(list_baldwiniana_2, marker='o', linestyle='--', color='r', label = "Método Prewitt + transformada circular de Hough")
plt.plot(list_lamarckiana_1, marker='^', linestyle='-.', color='c', label = "Método áreas binarizadas")
#plt.plot(list_lamarckiana_2, marker='D', linestyle=':', color='g', label = "Lamarckiana.2-opt")
plt.legend(loc="best")
plt.show()
