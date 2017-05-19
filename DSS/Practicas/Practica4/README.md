#Modelado de procesos de negocio con BPEL 2.0




##A realizar
1) Especificar utilizando BPEL 2.0 y la herramienta BPEL Designer para Eclipse el proceso de negocio (cuyo diagrama de actividad se muestra en la siguiente figura) y que se describe informalmente de la siguiente manera: *"El cliente invoca al proceso de negocio, especificando el nombre del empleado, el destino de su viaje, la fecha de salida y la fecha de regreso".*

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-1.png)


El proceso de negocio BPEL comprueba primera la categoría del empleado que va a viajar, que se corresponden con estos tipos de pasaje de avión: (a) clase turista, (b) clase business y (c) avión privado. Suponemos que disponemos de un SW contra el que se puede hacer la consulta, después de dicha consulta, el proceso BPEL comprobará el precion de billete con 2 líneas aéreas diferentes para encontrar mejor precio; suponemos otra vez que ambas compañías proporcionan un SW que permite realizar todas las gestiones anteriores. Por último, el proceso BPEL seleccionará el precio más bajo y devolverá un plan de viaje al cliente, para su aprobación.

2) Orquestar, de forma simplificada, el mercadeo entre un comprador y un vendedor de un producto solicitado, de acuerdo con el diagrama de interacción que se muestra en la siguiente figura.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-2.png)


(a) El comprador comienza pidiendo un precion al vendedor y el vendedor responde con un precio para el producto o una excepción sino conoce el artículo que le demandan o no estuviera disponible en el almacén. (a) El comprador continúa pidiendo precio al vendedor y entra en un comportamiento repetitivo con actualzaciones (del precio del artículo) hasta que decide comprar el artículo cuando considera que se le ofrece el mejor precio. (c) Se pide en este ejercicio desarrollar la descripción completa de la orquestación que se ha descrito anteriormente entre el comprador y el vendedor.


##SOA
Por medio de la arquitectura orientada a servicios (SOA) es posible realizar la integración de diferentes aplicaciones. El enfoque de esta arquitectura considera que las diferentes aplicaciones exponen sus funcionalidades a través de servicios web. De esta manera es posible acceder a diferentes funcionalidades de diferentes aplicaciones de una forma común a través de servicios web.


##BPEL
Cabe indicar que no es suficiente sólo con desarrollar servicios web y exponer sus funcionalidades, es también necesario tener alguna forma de componer dichas funcionalidades en un orden correcto. Para realizar dicha secuenciación se utiliza *la orquestación de servicios*, haciendo uso del lenguaje **BPEL** para realizar dicha composición.

Constituye un lenguaje estándar para la integración y automatización de procesos. Los procesos de negocio programados con BPEL serán capaces de ejecutarse en diferentes plataformas que cumplan dicho estándar, ofreciendo a los clientes una mayor libertad de elección. 

A través de este lenguaje se realiza una descripción relativamente simple de como pueden componerse los servicios web. Está basado en XML y soporta las tecnologías de servicios Web (incluyendo SOAP, WSDL, UDDI, WS-Reliable Messaging, WS-Addressing, WS-Coordination, y WS-Transaction).

###Estructura de un proceso BPEL
Un proceso BPEL especifica el orden exacto en el que deben invocarse los servicios Web participantes, tanto de forma secuencial como en paralelo.

En un escenario típico, el proceso de negocio BPEL recibe una petición de un cliente (que puede ser una aplicación cliente, u otro servicio Web, entre otros). Para servir dicha petición, el proceso invoca a diversos servicios Web y finalmente responde al cliente que ha realizado la llamada. Debido a que el proceso BPEL se comunica con otros servicios Web, tiene que tener en cuenta la descripción WSDL de los servicios Web a los que llama. 

	Un proceso BPEL es un servicio con estado de grano "grueso" (large-grained), que ejecuta unos pasos para completar una meta de negocio. Dicha meta puede ser la ejecución de una transacción de negocio, o la consecución del trabajo requerido por un servicio. Los pasos en el proceso BPEL ejecutan actividades (representadas por elementos del lenguaje BPEL) para lleva a cabo su cometido. Dichas actividades se centran en la invocación de servicios participantes para realizar las diferentes tareas y devolver los correspondientes resultados al proceso. El trabajo resultante de la colaboración de todos los servicios implicados es una orquestación de servicios. 
	
Cuando definimos un proceso BPEL, esencialmente definimos un servicio Web que es una composición de otros servicios Web existentes. La interfaz del nuevo servicio Web BPEL utiliza un conjunto de port types a través de los cuales ofrece operaciones igual que cualquier otro servicio Web. Cada port type puede contener varias operaciones. Para invocar un proceso de negocio descrito con BPEL, tenemos que invocar al servicio Web resultante de la composición, tal y como mostramos en la siguiente figura. 

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-5.png)


Un proceso BPEL puede ser **síncrono** o **asíncrono**. Un proceso BPEL síncrono bloquea al cliente (aquél que usa el proceso BPEL) hasta que finaliza y devuelve el resultado a dicho cliente. Un proceso asíncrono no bloquea al al cliente. Para ello utiliza una llamada callback que devuelve un resultado (si es que lo hay). Normalmente utilizaremos procesos asíncronos para procesos que consumen mucho tiempo, y procesos síncronos para aquellos que devuelven un resultado en relativamente poco tiempo.

La estructura básica de un documento (fichero con extensión .bpel) que define un proceso BPEL es la siguiente:

 
	<process name="nameProcess" ... >

		<partnerLinks>
    		<!-- Declaración de partner links -->
    	</partnerLinks>
    	
    	<variables>
    		<!-- Declaración de variables -->
    	</variables>
    	
    	<sequence>
      	<!-- Cuerpo principal de la definición del proceso BPEL -->
      	</sequence>
	</process>


En la etiqueta **<process>** se añaden los espacios de nombres. Aquí tenemos que definir tanto el espacio de nombres objetivo ( targetNameSpace), como los namespaces para acceder a los WSDL de los servicios Web a los que invoca, y al WSDL del proceso BPEL. Tenemos que declarar también el namespace para todas las etiquetas y actividades BPEL (que puede ser el espacio de nombres por defecto, para así no tener que incluirlo en cada nombre de etiqueta BPEL). El namespace para actividades BPEL debe ser: *http://schemas.xmlsoap.org/ws/2003/03/business-process/*: 

	<process name="nameProcess" 
         targetNamespace= "http://..."
         xmlns="http://schemas.xmlsoap.org/ws/2003/03/business-process/"
         xmlns:sw1="http://..." <!-- namespace del servicio Web sw1 -->
         xmlns:sw2="http://..." <!-- namespace del servicio Web sw2 -->
         ... >  

	...

	</process>

Un proceso BPEL está formado por una serie de pasos. Cada uno de los pasos se denomina **actividad**. La etiqueta **<sequence>** contiene el conjunto de pasos o actividades que conforman el servicio que proporciona el proceso BPEL.

La etiqueta (o elemento) **<process>** está siempre presente en un proceso BPEL, es decir, es el mínimo requerimiento en un fichero BPEL.


###Partner Links
Mediante estos elementos se definen los enlaces con las diferentes "partes" que interactúan con el proceso BPEL. Cada partner link tiene asociado un partnerLinkType específico que se definirá en el WSDL correspondiente. 

Los procesos BPEL interactuan con servicios Web externos de dos formas distintas:

- El proceso BPEL invoca operaciones sobre otros servicios Web.
- El proceso BPEL recibe invocaciones de clientes. Uno de los clientes es el usuario del proceso BPEL, que realiza la invocación inicial. Otros clientes son, por ejemplo, servicios Web que han sido invocados por el proceso BPEL, pero realizan callbacks para devolver las respuestas solicitadas. En este último caso, el proceso cliente tiene dos roles: es invocado por el proceso BPEL e invoca al proceso BPEL.

Cada proceso BPEL tiene al menos un partner link cliente, debido a que tiene que haber un cliente que invoque al proceso BPEL. Por otro lado, un proceso BPEL tendrá (normalmente) al menos un partner link a quién invoque.

BPEL trata a los clientes como partner links por dos razones. La más obvia es para proporcionar soporte para interacciones asíncronas. En interacciones asíncronas, los procesos necesitan invocar operaciones sobre sus clientes. Dichos procesos clientes devuelven el resultado mediante callbacks sobre el proceso que los invocó. 

La segunda razón está basada en el hecho de que el proceso BPEL puede ofrecer servicios. Estos servicios, ofertados a través de port types, pueden utilizarse por más de un cliente. El proceso puede querer distinguir entre diferentes clientes y ofrecerles únicamente la funcionalidad que éstos están autorizados a utilizar.

	Los partner links definen enlaces con los partners (partes que interaccionan con nuestro proceso de negocio) del proceso BPEL. Dichos partners pueden ser: (a) Servicios invocados por el proceso; (b) Servicios que invocan al proceso; (c) Servicios que tienen ambos roles: son invocados por el proceso e invocan al proceso. Ya que un cliente debe llamar al proceso BPEL, éste debe contener al menos una definición de partnerLink. 

La sintaxis para especificar los partnerLinks es:

 
	<partnerLinks>
		<partnerLink name="ncname" partnerLinkType="qname"
             myrole="ncname" partnerRole="ncname">
       </partnerLink>
	</partnerLinks>

Cada partner link es definido por un partner link type y un nombre de rol.

Cada partner link especifica uno o dos atributos, que tienen que ver con el rol que implementa cada uno de los servicios relacionados:

- myRole: indica el rol del propio proceso BPEL. Cuando solamente se especifica este atributo, cualquier cliente o partner puede interaccionar con el proceso BPEL sin ningún requerimiento adicional.
- partnerRole: indica el rol del partner. Si solamente definimos este atributo, estamos permitiendo la interacción con un partner o cliente que no imponga requerimientos sobre el proceso que haga la llamada.

Utilizaremos un único rol para una operación síncrona, ya que los resultados deben devolverse utilizando la misma operación. Utilizaremos dos roles en una operación asíncrona, ya que el rol del partner cambia cuando se realiza la llamada callback.

Los roles se definen en el documento WSDL de cada partner, cuando se especifican los partnerLinkTypes. 

Un **partnerLinkType** especifica la relación entre dos servicios, definiendo el rol que cada servicio implementa. Es decir, declara cómo interaccionan las partes y lo que cada parte ofrece. Los nombres de los roles son cadenas de caracteres arbitrarias. Cada rol especifica exactamente un tipo portType WSDL que debe ser implementado por el servicio correspondiente. 

Es fácil confundir los partner link y los partner link types, sin embargo: 

- Los **partner link types** y los roles son extensiones especiales de WSDL definidas por la especificación BPEL. Como tales, dichos elementos se definen en los ficheros WSDL, no en el fichero del proceso BPEL.
- **Partner link** es un elemento BPEL 2.0. Por lo que se define en el fichero del proceso BPEL.

El siguiente código corresponde a la descripción WSDL de un proceso BPEL, al que denominaremos Saludo, en el que declaramos el tipo MyPartnerLinkType, con el rol denominado ProveedorServicioSaludo. El servicio que implemente el rol ProveedorServicioSaludo, deberá implementar SaludoPortType. En este caso, MyPartnerLinkType describe la relación entre el cliente del proceso BPEL y el propio proceso BPEL. 

	<!-- Extracto de Saludo.wsdl -->
	<partnerLinkType name="MyPartnerLinkType">
		<role name="ProveedorServicioSaludo"
      		portType="SaludoPortType"/>
      	</role>
   </partnerLinkType>

A continuación se muestra un extracto del fichero que describe el proceso BPEL Saludo):

 
<!-- Extracto de Saludo.bpel -->
	<partnerLinks>
	   <partnerLink name="cliente"
	        partnerLinkType="MyPartnerLinkType"
	        myRole="ProveedorServicioSaludo"/>
	</partnerLinks>
	
Cuando utilizamos operaciones asíncronas, se definen dos roles.

	Cada partnerLink de un proceso BPEL se relaciona con un partnerLinkType que lo caracteriza. Cada partnerLinkType se define en el fichero WSDL: (a) del proceso BPEL, en el caso de que describa la interacción del cliente con el propio proceso BPEL, o (b) del servicio Web al que invoca dicho proceso BPEL. 


##Orquestación frente a coreografía
Los servicios web exponen las operaciones de ciertas aplicaciones o sistemas de información. Que varios servicios web se combinen implica la integración de las aplicaciones subyacentes.

Existen dos formas en la que los servicios web pueden combinarse:

- Orquestación
- Coreografía	

En una **orquestación**, un proceso central (que puede ser otro servicio web) lleva el control de los servicios web implicados en la realización de la tarea y coordina la ejecución de las diferentes operaciones sobre dichos servicios web. Los servicios web implicados no son conscientes de que forman parte de un proceso de composición (un proceso de negocio de nivel mas alto). Únicamente el coordinador es consciente de dicha orquestación, por lo que esta se centraliza mediante definiciones explícitas de las operaciones y del orden en el que se deben invocar a los servicios web. Es normalmente usada en procesos de negocio privados.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-3.png)


Cuando se hace **coreografía** no exite coodinador central. En su lugar, cada servicio web implicado en dicha coreografía sabe exactamente cuando tiene que ejecutar sus operaciones y con quien debe interacturar. Se basa en el intercambio de mensajes en procesos de negocio públicos. Todos los servicios web implicados en la coreografía deben estar informados de las operaciones a ejecutar, los mensajes a intercambiar y el tiempo a invertir en dicho intercambio de mensajes.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-4.png)


##Instalación del plugin BPEL
Para instalar el plugin de BPEL en Eclipse basta con ir a *Help --> Install new software --> Add* y buscar BPEL en la url **http://download.eclipse.org/bpel/site/1.0.5** como se muestra en la imagen.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-6.png)



##Instalación del servidor ODE
Lo siguiente será instalar el servidor ODE, para ello creamos un nuevo servidor como se ha estado haciendo hasta ahora, es decir, *new Server*, una vez ahí se selecciona el *Ode v1.x server* dentro del paquete Apache como aparece en la imagen.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-7.png)


Lo siguiente será descargarse el desplegable [ode.war](http://www.apache.org/dyn/closer.cgi/ode/apache-ode-war-1.3.6.zip) del sitio web oficial de Apache. Una vez descargado hay que copiarlo dentro de la carpeta *webapps* de la distribución de Tomcat instalada. A continuación habrá que configurar algunos parámetros necesarios como el path del desplegable *ode* o el path de Tomcat para el servidor ODE como se puede ver en la siguiente imagen.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-8.png)


Para que se cree la carpeta *ode* dentro del servidor Tomcat es necesario lanzarlo mediante la orden del script:

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-9.png)


Una vez que Tomcat esta arrancado y se ha creado dicho directorio, ya solo queda añadir al claspath de Tomcat un par de JARs externos como se ve en la imagen, **tomcat-july.jar** y **bootstrap.jar**.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-10.png)


A continuación se detendrá Tomcat desde la terminal y se lanzará el servidor ODE desde el Eclipse.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-11.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-12.png)


##Despliegue de un proceso BPEL
Comenzamos creando un nuevo proyecto BPEL en Eclipse: *File --> New --> Other --> BPEL2.0 --> BPEL Project* llamándolo *ODE_Prueba* y seleccionando como runtime objetivo a **Apache ODE 1.x** y su configuración por defecto.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-13.png)


Ahora lo siguiente es crear el proceso BPEL, para lo cual sobre la carpeta *ODE_Prueba\beplContent* se seleccionará del menú *File --> New --> Other --> BPEL2.0 --> New BPEL process file* y se configura con los siguientes parámetros.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-14.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-15.png)


###Proceso BPEL
Una vez realizado todo lo anterior se puede visualizar el proceso BPEL a través del archivo *HolaMundo.bpel*. 

Comenzaremos arrastrando la acción *Assign* desde la paleta; en el apartado *Actions*, uniéndola sobre la acción *receiveInput* y eliminándo luego el cuadrado *FIX_ME-Add_Business_Logic_Here* del gráfico, quedando el proceso BPEL de la siguiente manera.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-16.png)


Lo siguiente es añadirle un operador de asignación a la acción previamente añadida, para ello se selecciona la actividad *Assign* y con el click derecho se elige *Show in properties*, una vez dentro, en la pestaña *Properties* se selecciona *Details* y con el *New* se terminará de defirnir. Ya solo queda asignar el *from* y *to* desde las ventanas como se muestra en la imagen. A la pregunta sobre inicialización de la variable le respondemos “yes”.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-17.png)



###Archivo WSDL
Ahora hay que proporcionar un *puerto* y una *ligadura* (**binding**) para comunicar con los servicios. Para ello hay que editar el fichero *HolaMundoArtifacts.wsdl*.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-18.png)


Sobre *HolaMundoService* al clickear debe aparecer en el menú la opción de *Show Porperties*. Clicando en *HolaMundoPort* aparecerá un menú desplegable que se abre. Hay que asegurarse que la dirección del puerto está asignada a: **http://localhost:8080/ode/processes/HolaMundo**. La sustitución en la pantalla que se nos presenta puede ser:

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-19.png)


###Despliegue del servicio
Una vez creado el servicio, para este ejemplo ha sido uno muy básico que lo único que hace es aceptar una cadena del cliente y devolvérsela mostrándola. Como todo SW, hay que desplegarlo para que puedan acceder a el los clientes. Para ello, se debe clickear en la carpeta *bpelContent* y seleccionar las acciones *File --> New --> Others --> BPEL2.0 --> BPEL Deployment Descriptor*. Una vez echo esto se seleccionará el fichero *deploy.xml* para abirlo en su editor *ODE Deployment Descriptor Editor* como se muestra en la imagen.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-20.png)


En la tabla denominada *Inbound Interfaces* de la imagen anterior, se muestran las interfaces que proporciona el proceso, especificando el servicio, puerto y ligadura que se quiere utilizar para cada *PartnerLink* que aparece en las filas de la tabla. En este ejemplo el *PartnerLink* se llamará *client*.

Por tanto, ya se tiene el modelado del servicio *HolaMundo* que se compone de los siguientes elementos:

- Un proyecto BPEL: *ODE_Prueba*
- Un proceso BPEL: *HolaMundo.bpel*
- El archivo con el servicio web: *HolaMundoArtifact.wsdl*
- Descriptor de despliegue del servicio: *deploy.xml*

Ahora lo que resta es añadir el proyecto BPEL al servidor ODE que se encuentra arrancado.


###Ejecución del servicio
Sobre el servidor ODE, con el botón derecho seleccionaremos Add and Remove, nos aparecerá un menú partido con ODE_Prueba en la columna izquierda *(Available)*, que añadiremos a la columna derecha *(Configured)*. Si apareciese una ventana de notificación o si el menú partido tuviera su columna izquierda vacía, hay que cerrar el runtime de Eclipse y volver a configurar el servidor Ode v1.x, a través del enlace launch and configuration de su menú de configuración. Por último, seleccionamos Add y Finish.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-21.png)


Comprobamos que todo ha ido correctamente con los mensajes que nos lanza el servidor ODE.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-22.png)


###Consola de administración ODE
En la dirección *http://localhost:8080/ode* accedemos a la página principal de la consola de ODE. A través de la dirección *http://localhost:8080/ode/deployment/services/* se listan los servicios instalados en el puerto 8080 de la máquina local, también es accesible desde la página inicial a través de *Deployment browser --> Process services*.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-23.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-24.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-25.png)


##Ejecución del proceso BPEL con el navegador de servicos web de Eclipse
Para ejecutar el proceso BPEL en el navegador de servicios web de Eclipse hay que seleccionar con el botón derecho el fichero *HolaMundoArtifacts.wsdl* y acceder desde el menú *Web Services --> Test with Web Services Explorer*.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-26.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-27.png)


En el árbol de la izquierda hay que buscar el elemento *process*. Ahora hay que clicar en el enlace *process* de la tabla Operations para que nos aparezca un cuadro de texto de sustitución para los parámetros de la operación cuyo comportamiento queramos probar y poder llamarla o especificar puntos finales (*endpoints*) adicionales. A continuación se escribe el mensaje correspondiente en la caja de texto y se pulsa el botón **Go**, de esta manera aparecerá el resultado de la ejecución en la ventana inferior.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-28.png)

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p4-29.png)




