# Tarea 3

Existen diferentes frameworks css para el desarrollo web como **Material Framework**, **Leaf**, **Materialize**, **Essence**, ett. En esta tercera tarea se va a utilizar el framework responsive **Boostrap** que se emplea para facilitar el uso de las páginas ayudando a que se ajusten al tamaño que tenga el navegador si se visualiza en diferentes dispositivos como móviles, tablets, etc.

Para utilizar **Boostrap** lo primero es añadir el enlace a la hoja de estilos que vamos a utilizar en la cabecera del fichero *html* antes de cualquie otro enlace a otra hoja de estilo.

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">


Lo siguiente es añadir los plugins para **JavaScript**, **jQuery** y **Tether** cerca del final de la página (justo antes de cerrar la etiqueta *body*). 

	<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>