# Tarea 0

En esta primera tarea de la asignatura vamos a proceder a instalar **Python 3.5**, el framework **Django** en la versión 1.96 y el servidor **Green Unicorn** en la versión 19.4.

Lo primero que se va a realizar es instalar Python en la versión que se pide como se muestra en la siguiente imagen:

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-1.png)



Una vez instalado Python, lo próximo será instalar el paquete **virtualenv** para la creación de los entornos virtuales a través gestor de paquetes para el desarrollo de Python **pip**. 

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-2.png)



El paquete para la creación de entornos virtuales es algo fundamental cuando se quiere utilizar Python como herramienta para el desarrollo web debido a que pip instala todos los paquetes de manera global por defecto, a diferencia de **Maven** o **npm** que los instala en el directorio del proyecto. El comportamiento de pip puede parecer irrelevante a simple vista, pero puede llegar a ser muy frustante cuando llegado el caso se tiene dos proyectos diferentes que necesitan usar diferentes versiones de la misma librería como sucede en la siguiente imagen:

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-3.png)



Ahí hemos podido ver que tanto project_1 como project_2 depende de la misma librería pero con versiones diferentes, un problema ya que solo se puede tener instalada una versión a la vez en el sistema.


La solución a este tipo de problemas es usar un **entorno virtual**, que en lo que consiste es en tener una copia separada de Python. Es decir,se crea un entorno virtual por cada proyecto aislando de esta manera las dependecias para los diferentes proyectos. Una vez que se tiene un entorno virtual para cada proyecto, es posible instalar las dependencias del proyecto dentro del entorno virtual en lugar de hacerlo en el entorno global de Python como se aprecia en la imagen:

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-4.png)



Lo recomentable es tener instalados el menor número de paquetes posible en el entorno global de Python y los necesarios para cada proyecto en su entorno virtual.

Una vez instalados los paqutes básicos del sistema que se necesitamos, pasamos a instalar las dependencias específicas de Python. Con **virtualenv** para el aislamiento de dependencias de paquetes y **pip** para el manejo de las mismas ya instalados, pasamos a usarlos para obtener **Django** y **Gunicorn**.

Lo primero será crear un directorio para almacenar los entornos virtuales que se vayan creando.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-5.png)



Creamos un entorno virtual dentro del directorio anterior y lo activamos.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-6.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-7.png)



Al activarlo hemos podido ver como la consola ha cambiado, ahora entre paréntesis nos indica el entorno virtual en el que estamos actualmente, en nuestro caso **(djpproject)**.

Una vez dentro del entorno virtual pasamos a instalar **Django** y **Green Unicorn** dentro de él a través del gestor de paquetes **pip**.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-8.png)



Para probar que todo se ha instalado correctamente dentro del entorno virtual, vamos a proceder a crear un nuevo proyecto Django llamado *djproject*. Una vez creado entramos al directorio.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-9.png)



Podríamos ejecutar Django con el servidor de desarrollo usando el comando **python manage.py runserver**, pero en vez de eso iniciaremos Django con Gunicorn como se muestra en la imagen.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-10.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea0/ssbw-t0-11.png)



Con todo esto ya esta todo listo para comenzar a desarrollar.
