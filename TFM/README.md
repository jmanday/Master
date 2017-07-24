# Trabajo Final de Master
## Reconocimiento de personas a través del iris en condiciones no ideales

### Objetivo
El propósito de este Trabajo Final de Master es analizar e investigar las posibles soluciones y alternativas presentes en el campo del reconocmiento de personas a través del iris.

Debido a que el problema para reconocer personas a través del iris en condicioles ideales está resuelto y existen numerosas teorías y propuestas que ayudan a ello, existe del mismo modo un campo muy amplio sin solución óptima que permite ser explorado para aportar nuevas propuestas que ayuden a mejorar las ya existentes en el reconocimiento de personas a través del iris en condiciones no ideales.


### USIT
Es un paquete software para el reconocimiento de iris que incluye algoritmos para:
 - preprocesamiento del iris
 - extracción de características
 - comparación de características

**USIT** se basa en una herramienta de línea de comandos fácil de usar. Es un proyecto de código abierto que está implementado en c++ y desarrollado por el grupo de investigación *The Multimedia Signal Processing and Security Lab* (wavelab) del departamento de Ciencias de la Computación de la Universidad de Salzburgo.

En la siguiente figura se muestra la cadena de procesos típica en el procesamiento del iris (remarcando los módulos que son proporcionados por dicho paquete software).

![Procesamiento del iris](https://raw.githubusercontent.com/jmanday/Images/master/TFM/tfm-img1.png)


### Librerías
Para el funcionamiento de **USIT** son necesarias las librerías de **OpenCV** y **Boost**.

Instalaremos la librería **OpenCV** desde el gestor de paquetes *hombrew* para mac, por lo que debemos tenerlo instalado. Con dicho software instalado ejecutamos las siguientes órdenes.

	brew tap homebrew/science
	brew install opencv
	
Esto nos instalará las librerías y dependencias de opencv necesarias para **USIT** tales como *libopencv_core*, *libopencv_photo*, etc, en el directorio **/usr/local/lib**.

Para indicar la localización del conjunto de librerías necesarias de **OpenCV** al compilador, vamos a instalar la herramienta **pkg-config** para eviar de esta forma el tener que incluir manualmente cada una de las librerías para compilar ya que esto lo hará automáticamente dicho paquete. Para ello lo instalamos con el gestor **brew**.

	brew install pkg-config
	
Una vez instalado hay que indicar en la variable de entorno la localización del fichero **opencv.pc** que será el que contenga todas las librerías que queramos utilizar de **OpenCV**, por lo que exportamos dicha variable con el siguiente comando.

	$ export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
	
Con el mismo gestor de paquetes instalamos **Boost**, la otra librería necesaria para **USIT**.

	brew install boost --c++11
	
Le debemos de indicar que instale las librerías del paquete **Boost** que fueron compiladas con **libc++** ya que los programas con los algoritmos que proporciona el paquete **USIT** se van a compilar con ese mismo. Es también necesario indicarle que haga el linkado con la siguiente orden.

	brew link boost
	
Previamente el sistema operativo debe tener instalado dicho compilador **libc++** para que todo funcione correctamente.

	


