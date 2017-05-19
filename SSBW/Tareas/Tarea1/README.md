# Tarea 1

Esta tarea trata de servir distintos tipos de contenidos al navegador, es decir, al cliente de las peticiones *HTTP*, tales como texto plano, html e imágenes.

Para ello usaremos el microframework de python **Flask**, por lo que comenzaremos por crear un nuevo entorno virtual, activarlo e instalar en él dicha herramienta.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea1/ssbw-t1-1.png)


Para comenzar crearemos una mínima aplicación como la que se muestra a continuación:

	from flask import Flask
	app = Flask(__name__)
	
	@app.route('/')
	def hello_world():
		return 'Hello, World!'
		
En ese extracto de código del fichero al que llamaremos **hello.py** lo primero que hacemoses importar la clase **Flask**, ya que una instancia de esta clase será nuestra aplicación WSGI. Lo siguiente que realizamos es crear una instancia de esa clase. El primer argumento es el nombre del paquete o módulo de la aplicación y se suele emplear cuando la aplicación es importada como un módulo. Es importante este aspecto porque Flask necesita saber donde mirar para las plantillas, los ficheros estáticos y demás.

Lo siguiente en aparecer es la palabra **route**, a través de la cual le decimos a Flask con que URL será activada nuestra función, en este caso la que hemos definido como *hello_world()*

Para poder ejecutar la aplicación vamos a utilizar el comando **flask**, pero antes de poder hacer esto es necesario indicarle al terminal de la aplicación la variable de entorno  que va a necesitar:

	export FLASK_APP=hello.py
	flask run

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea1/ssbw-t1-2.png)


![alt text](https://raw.githubusercontent.com/jmanday/Images/master/SSBW/Tarea1/ssbw-t1-3.png)


Se puede comprobar que todo se ha realizado correctamente y que el servidor esta atendiendo dicha petición.

Como inciso, por defecto en Flask el servidor es accesible solamente desde la propia máquina en la que se ejecuta, por lo que ninguna otra de la misma red podría hacerlo. Esto es debido a que en modo de depuración un usuario de la aplicación puede ejecutar arbitrariamente código Python en dicha máquina. Para hacer el servidor disponible publicamente simplemente basta con añadir lo siguiente:

	flask run --host=0.0.0.0
	
Esto le dirá al sistema operativo que escuche en todos los puertos públicos.



## WorkFlow

A modo de resumen general se va a mostrar los pasos que se sigue en el modelo cliente-servidor dentro de una aplicación web:

1. Un usuario realiza una petición para ir a una página de inicio a través de su URL (/).
2. El fichero **routes.py** mapea la URL (/) a una función de Python.
3. La función de Python busca una plantilla web dentro de la carpeta **templates**.
4. Una plantilla web mira en la carpeta **static** por si necesita alguna imagen, o fichero CSS o JavaScript para renderizar a HTML.
5. El renderizado HTML es enviado de vuelta al fichero **routes.py**.
6. **routes.py** envía el HTML al navegador que realizó la petición.


## Debug Mode

Mediante el modo de depuración evitamos la tediosa tarea de tener que reiniciar el servidor cada vez que se produzca un cambio en el código, algo que tendríamos que hacer si esa opción no estuviese habilitada. Para habilitar el modo depuración basta con indicarlo en la variable de entorno de flask:

	export FLASK_DEBUG=1
	flask run
	
Esto hace que se active el modo depuración, que se active la recarga automática y se habilite el modo depuración.



## Routing

El enrutamiento es empleado en las aplicaciones web modernas para evitar que el usuario deba pasar por toda la jerarquía de navegabilidad para acceder a una página concreta, lo que en dispositivos móbiles con una baja conexión de red es muy útil.


Para ello se utiliza la funcionalidad de Flask llamada **route**, a través de la cual el servidor expone las direcciones URL a las que va a saber responder y por lo tanto servir.

	@app.route('/')
	def index():
		return 'Index Page'
		
	@app.route('/hello')
	def hello():
		return 'Hello, World!'


## Variables Rules

Es posible añadir variables a una URL para su posterior tratamiento en el servidor, donde son pasadas como un parámetro a la función asociada a la ruta. De manera opcional, las variables añadidas a la URL pueden ser convertidas usando un regla específica. Existen diferentes tipos de conversiones como a **string, int, float, path, any** o **uuid**.

	@app.route('/user/<username>')
	def show_user_profile(username):
		return 'User %s' % username


	@app.route('/post/<int:post_id>')
	def show_post(post_id):
		return 'Post %d' % post_id

	
	
## Unique URLs

El comportamiento de redireccionamiento que tiene Flask para las URLs se basa en el módulo de enrutamiento de Werkzeug, y es que en las siguientes dos reglas:

	@app.route('/projects/')
	def projects():
   		return 'The project page'

	@app.route('/about')
	def about():
    	return 'The about page'
    	
    	
podrían parecer que tienen el mismo comportamiento, pero no es así debido a la barra **/**. En el primer caso, la URL para el endpoint *project* tiene dicha barra, por lo que si se accede a la URL sin la barra el comportamiento es el mismo que en un sistema de ficheros, es decir, la función se lamzaría porque se estaría tratando de la misma URL. 

Pero en el caso contrario, es decir, para el endpoint **about** si le añadiesemos al final la barra el servidor no sabría que ruta es la que se está solicitanto, por lo que daría un error 404 de 'no encontrado'.



## URL Building

Mediante la función **url_for()** es posible construir URLs dinámicas para una función específica. Esto es muy útil ya que en una aplicación web todo está basado en rutas, por lo que se tiene que tener especial cuidado cuando se usan. Una buena técnica para evitar problemas con las rutas, por ejemplo si es cambiada, es el de utilizar la referencia al método y no la ruta directamente. Este método hace exactamente eso, recibe como parámetro el nombre del método y devuelve la ruta asociada a dicho método:

	@app.route('/saludo/dia')
	def dia():
		 return "Buenos Dias!!!"
		 
	
	@app.route('/saludo/tarde')
	def tarde():
		return "Buenas Tardes!!!"
		
	@app.route('/saludo/noche')
	def noche():
		return "Buenas Noches!!! Que descanses!!!"
		
		
	<ul>
  		<li>{{ url_for("dia") }}</li>
  		<li>{{ url_for("tarde") }}</li>
  		<li>{{ url_for("noche") }}</li>
	</ul>	
	
	
esta es la manera mas correcta de manejar rutas con Flask, ya que si la ruta cambia no afecta para nada al código que hay en el html, ya que este está llamando al método asociado a la ruta.



## HTTP Methods

El protocolo HTTP conoce diferentes métodos para acceder a una url. Aunque por defecto una ruta solo realiza peticiones **GET**, como argumento a una ruta se puede indicar los tipos de métodos que soporta, como se muestra en el ejemplo:

	from flask import request
	
	@app.route('/login', methods=['GET', 'POST'])
	def login():
	    if request.method == 'POST':
	        do_the_login()
	    else:
	        show_the_login_form()	
	        

Toda petición **GET** incluye de manera automática las cabeceras **HEAD** de la petición. Los métodos HTTP, también conocidos como verbos, lo que hacen es decirle al servidor que quiere hacer el cliente con la página solicitada.

- **GET**: el navegador le dice al servidor que solo quiere obtener la información que hay almacenada en la página.


- **HEAD**: el navegador le dice al servidor que quiere obtener la información pero en este caso no del contenido de la página, sino de la cabecera.

- **POST**: el navegador le dice al servidor que quiere enviar alguna nueva información a esa URL y que debe asegurarse de que el dato es almacenado.

- **DELETE**: el navegador le dice al servidor que elimine la información de la localización dada.

- **OPTIONS**: le proporciona al cliente una manera de conocer los métodos que son soportados por una URL particular.

Cabe destacar que de HTML1 a HTML4 los únicos métodos soportados por el servidor son los métodos **GET** y **POST**, aunque con JavaScript y las nuevas versiones de HTML es posible utilizar el resto de los métodos.



## Static Files

Los ficheros estáticos en una aplicación se suelen emplear para temas relacionados con el diseño como son los CSS o para ficheros de código JavaScript.

Existe una forma de generar URLs para ficheros estáticos usando para ello el endpoint especial **static**.

	url_for('static', filename='style.css')     
	


## Rendering Templates

Es bastante engorroso y poco divertido tener que generar HTML desde dentro de Python. Para evitar esto Flask configura el motor de plantillas **Jinja2**.

Para renderizar una plantilla se puede usar el método **render_template()**. Lo único que hay que hacer es proporcionar el nombre de la plantilla y las variables que se quiere pasar como argumento a dicho motor de plantillas como se muestra en el ejemplo.


	from flask import render_template
	
	@app.route('/hello/')
	@app.route('/hello/<name>')
	def hello(name=None):
	    return render_template('hello.html', name=name)   
	    

Flask lo que hace es mirar en la carpeta **templates**, que se encontrará en el nivel del módulo de la aplicación. 

	<!doctype html>
	<title>Hello from Flask</title>
	{% if name %}
	  <h1>Hello {{ name }}!</h1>
	{% else %}
	  <h1>Hello, World!</h1>
	{% endif %}	
	

Dentro de las plantillas se puede tener acceso a la **petición** (request), la **sesión** (session) y objetos **g**.

Las plantillas son realmente útiles si se utiliza la herencia de plantillas. El escape automático está habilitado. A través de la clase **Markup** es posible trabajar con lenguajes de marcas.	    

Es importante tener separado el contenido del diseño para hacer la aplicación fácil de mantener. Es por eso que para evitar duplicar código de diseño de una plantilla a otra se utiliza la **herencia**. Las plantillas principales definen todos los elementos comunes de la aplicación que va a existir en todas las páginas, definiendo también bloques de contenido (**block content**) que serán rellenado por el contenido de las plantillas hijo.

	from flask import Flask, render_template
 
	app = Flask(__name__)      
	 
	@app.route('/')
	def home():
	  return render_template('home.html')
	 
	if __name__ == '__main__':
	  app.run(debug=True)
	  
El flujo de trabajo es el siguiente:

- Primero se importa la clase **Flask** y la función **render_template**.
- Seguidamente se crea un instancia de la clase Flask.
- A continuación se mapea la URL (/) a la función *home()*, que se ejecutará cada vez que alguien visite esa URL.
- La función *home()* usa la función de Flask *render_template()* para renderizar los ficheros **html** y enviárselos al navegador.


## CSS

Las hojas de estilo son añadidas a la plantilla principal del diseño, es decir, a la plantilla padre, ya que así será heredada por todos sus hijos.

La referencia a la hoja de estilos CSS se suele realizar en la cabecera (**HEAD**) de este fichero como se muestra en el ejemplo.

	<!DOCTYPE html>
	<html>
	  <head>
	    <title>Flask</title>    
	    <strong><link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}"></strong>
	  </head>
	  <body>
	    <header>
	      <div class="container">
	        <h1 class="logo">Flask App</h1>
	      </div>
	      </header>
	     
	    <div class="container">
	      {% block content %}
	      {% endblock %}
	    </div>
	  </body>
	</html>

Es en este caso cuando usamos la función **url_for** para generar un path de la URL para el fichero de la hoja de estilo CSS desde la carpeta *static*. 



### Custom Error Pages

Flask proporciona la función **abort()** para manejar cuando una petición HTTP aborta, proporcionando para ello una página de error blanca y negra con un pobre y breve descripción.

Los siguientes códigos de errores son comúnmente mostrados al usuario por parte del servidor:

- *404 Not Found*: este error aparece cuando se solicita una URL que no existe.
- *403 Forbiden*: este error es enviado cuando se quiere acceder a un recurso no permitido.
- *410 Gone*: este error es enviado cuando se solicita un recurso que ha sido recientemente eliminado. Esta relacionado con el *404*. 
- *500 Internal Server Error*: este error sucede cuando ocurre un error de programación en el servidor.

Los errores son manejados con **errorhandler()**, a la que hay que proporcionarle el código de error y el código de estado para la respuesta del servidor. Es importante recordar que Flask no disparará el manejador del error *500 Internal Server Error*si es está ejecutando en *Modo Debug*.


## Realización tarea

### Sirviendo contenidos

Esta primera parte de la tarea consiste en servir al navegador diferentes contenidos, entre los que estan el texto plano, html e imágenes. Para esto es necesario cambiar el tipo de contenido en la cabecera de la respuesta que el servidor expone como se muestra en el siguiente código:

	from flask import Flask, render_template, send_file, make_response
	
	app = Flask(__name__)
	
	# ruta para servir html
	@app.route('/home')
	def home():
		return render_template('home.html', mimetype='html')
	
	# ruta para servir texto
	@app.route('/text')
	def text():
	    bar = 'This is text'
	    response = make_response(bar)
	    response.headers['Content-Type'] = 'text; charset=utf-8'
	    return response
	
	# ruta para servir una imagen
	@app.route('/image')
	def image():
	    filename = './static/img/circulo_rojo.png'
	    return send_file(filename, mimetype='image/png')
	    
	    
### Sitio web estático con plantillas

Para esta segunda parte de la primera tarea se utiliza el motor de plantillas **Jinja2** a través del cual establecemos como plantilla estática para que el servidor la renderize y se la sirva al cliente.

	<!DOCTYPE html>
	<html>
	    <head>
	        <title>Flask App</title>
	        <strong><link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}"></strong>
	    </head>
	    <body>
	        <header>
	            <div class="container">
	                <h1 class="logo">Flask App</h1>
	            </div>
	        </header>
	
	        <div class="container">
	              {% block content %}
	              {% endblock %}
	        </div>
	    </body>
	</html>	    

En las plantillas también se hace referencia a las hojas de estilo, generalmente en la cabecera como se ve en el ejemplo anterior. Esta plantilla se utilizaría como generalizada, heredándo el resto de plantillas de esta para que se mantega siempre las partes comunes en todas las demás.

	{% extends "layout.html" %}
	{% block content %}
	  <div class="jumbo">
	    <h2>Welcome to the Flask app<h2>
	    <h3>This is the home page for the Flask app<h3>
	  </div>
	{% endblock %}
	  