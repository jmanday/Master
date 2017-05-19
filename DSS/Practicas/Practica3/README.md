#Implementación de un servicio CRUD en Java

Realizar un servicio web que llamaremos 'CRUD' (Create, Read, Update, Delete), que ha de ser RESTful y que nos permitirá mantener una lista de objetos de un determinado dominio de libre elección (reseñas bibliográficas, catálogo de coches, etc..), pero que ha de incorporar imágenes y sonidos, en nuestra aplicación Web a través de llamadas HTTP.


##REST con Java usando Jersey

###REST
Es un estilo de arquitectura basado en estándares web y y el protocolo HTTP. En una arquitectura REST cada cosa es un recurso. Un recurso es accedido a través de un interfaz común basado en los métodos estándar HTTP. En una arquitectura REST típicamente hay un servidor REST que proporciona acceso a los recursos y un cliente REST que accede y modifica esos recursos.

Cada recurso debe soportar las operaciones comunes de HTTP. Los recursos son identificados por IDs globales que son típicamente **URIs**. REST permite que los recursos tengan diferentes representaciones, como por ejemplo texto, XML, JSON, etc. El cliente REST puede preguntar por una específica representación a través del protocolo HTTP.

Los métodos *PUT*, *GET*, *POST* y *DELETE* son usados típicamente en las arquitecturas basadas en REST. 

- **GET**: define un acceso de lectura del recurso.
- **PUT**: crea un nuevo recurso.
- **DELETE**: elimina los recursos.
- **POST**: actualiza un recurso existente o crea un nuevo.

Los servicios webs **RESTful** están basados en métodos HTTP y el concepto de REST. Típicamente define el URI base para los servicios, el soporte de tipos MIME (XML, texto, JSON,...) y el conjunto de operaciones (POST, GET, PUT, DELETE).



###JAX-RS con Jersey
Java define el soporte a REST a través  de *Java Specification Request (JSR)*. **JAX-RS** es la API de Java para definir servicios web RESTful a través de anotaciones para establecer la relación REST de las clases Java.

**Jersey** es un librería que implementa la **API JAX-RS**,  proporcionando una solución para implementar servicios webs RESTful en un contenedor servlet de Java.

En el lado del servidor Jersey proporciona una implementación de Servlet que escanea clases predefinidas para identificar recursos RESTful. En el archivo de configuración **web.xml** se registra el servlet para la aplicación web.

Jersey también proporciona una librería cliente para comunicar con un servicio web RESTful.

Una URL base de ejemplo de un servlet puede ser como esta:

	http://your_domain:port/display-name/url-pattern/path_from_rest_class
	
Este servlet lo que hace es analizar las peticiones de entrada y seleccionar las correctas clases y métodos para responder a la petición.

Una aplicación web RESTful consiste por lo tanto, en clases de datos y servicios. Estos dos tipos son típicamente administrados en diferentes paquetes.

JAX-RS soporta la creación de XML  y JSON a través de JAXB. Proporciona una serie de anotaciones como se muestran a continuación:

- **@POST**: el método responderá a una petición HTTP POST.
- **@GET**: el método responderá a una petición HTTP GET.
- **@PUT**: el método responderá a una petición HTTP PUT.
- **@DELETE**: el método responderá a una petición HTTP DELETE.


###Instalación de Jersey

Lo primero es descargarse la librería [Jersey](https://jersey.java.net/download.html) de su página.

El fichero zip contiene los ficheros JAR con la implementación de Jersey. Todos los ficheros dentro de los directorio *api*, *ext* y *lib* se deben copiar dentro de la carpeta *WEB-INF/lib*.

###Eclipe Web Tool Platform
El proyecto **Eclipse WTP** proporciona herramientas para desarrollar aplicaciones web estándar de Java y aplicaciones Java EE. Los artefactos web en un entorno Java son las páginas HTML, ficheros XML, servicios web, servlets y JSPs. Eclipse WTP simplifica la creación de esos artefactos y proporciona entornos de ejecución donde pueden ser desplegados, lanzados y depurados.

Eclipse WTP soporta la mayoría de contenedores web como pueden ser **Jetty** y **Apache Tomcat**. 


###Contenedor web
Para este tutorial se va a utilizar Tomcat como contenedor web. Para usar Tomcat como contenedor de servlet es necesario seguir la guía de instalación de [Eclipse WTP](http://www.vogella.com/tutorials/EclipseWTP/article.html#eclipse-web-tool-platform) para tener instalada la herramienta de desarrollo web.

En la guía lo que hace es en primer lugar instalar las siguientes características que son necesarias:

- Eclipse Java EE Developer Tools
- Eclipse Java Web Developer Tools
- Eclipse Web Developer Tools
- JST Server Adapters
- JST Server Adapters Extensions

Una vez instaladas toca configurar un entorno de ejecución a través de Eclipse WTP desde *Preferences->Server->Runtime->Evironments*. Una vez ahí se crea un nuevo entorno de ejecución del servidor y se selecciona el tipo de servidor Tomcat.

Para que aparezca la pestaña de **Servers** es necesarios activarla desde *Window->Show View->Other->Servers*, de esta forma tendremos visible todos los servidores Tomcat que hay disponibles.

De forma alternativa se puede utilizar [Google App Engine](http://www.vogella.com/tutorials/GoogleAppEngineJava/article.html) para ejecutar la parte del servidor.


###Crear un servicio web RESTful

Para ello lo primero es crear un nuevo *Dynamic Web Project* como se muestra en la imagen.

![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p3-1.png)

Lo siguiente es crear una clase que se registrará como un recurso get a través de la notación **@GET** al importarlo desde **javax.ws.rs.GET**.

	package com.jmanday.jersey2;

	import javax.ws.rs.GET;
	import javax.ws.rs.Path;
	import javax.ws.rs.Produces;
	import javax.ws.rs.core.MediaType;

	@Path("/hello")
	public class Hello {
	
	// This method is called if TEXT_PLAIN is request
	  @GET
	  @Produces(MediaType.TEXT_PLAIN)
	  public String sayPlainTextHello() {
	    return "Hello Jersey";
	  }

	  // This method is called if XML is request
	  @GET
	  @Produces(MediaType.TEXT_XML)
	  public String sayXMLHello() {
	    return "<?xml version=\"1.0\"?>" + "<hello> Hello Jersey" + "</hello>";
	  }

	  // This method is called if HTML is request
	  @GET
	  @Produces(MediaType.TEXT_HTML)
	  public String sayHtmlHello() {
	    return "<html> " + "<title>" + "Hello Jersey" + "</title>"
	        + "<body><h1>" + "Hello Jersey" + "</body></h1>" + "</html> ";
	  }

	}

La anotacion **@Produces** define que el recurso compartido es texto y el tipo **MIME HTML**. La anotación **@Path** define bajo que url estará disponible el servicio.

Es necesario registrar a **Jersey** como el despachador de servlets para las peticiones *REST*. Para hacer esto hay que modificar el archivo **web.xml**.

	<?xml version="1.0" encoding="UTF-8"?>
	<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd" id="WebApp_ID" version="3.1">
  		<display-name>com.jmanday.jersey2</display-name>
  		<servlet>
    		<servlet-name>Jersey REST Service</servlet-name>
    		<servlet-class>org.glassfish.jersey.servlet.ServletContainer</servlet-class>
     	<!-- Register resources and providers under com.vogella.jersey.first package. -->
    	<init-param>
        	<param-name>jersey.config.server.provider.packages</param-name>
        	<param-value>com.jmanday.jersey2</param-value>
    	</init-param>
    	<load-on-startup>1</load-on-startup>
  	</servlet>
  	<servlet-mapping>
    	<servlet-name>Jersey REST Service</servlet-name>
    	<url-pattern>/rest/*</url-pattern>
  	</servlet-mapping>
  	<welcome-file-list>
    	<welcome-file>index.html</welcome-file>
    	<welcome-file>index.htm</welcome-file>
    	<welcome-file>index.jsp</welcome-file>
    	<welcome-file>default.html</welcome-file>
    	<welcome-file>default.htm</welcome-file>
    	<welcome-file>default.jsp</welcome-file>
  	</welcome-file-list>
	</web-app>

El parámetro **jersey.config.server.provider.packages** define en que paquete **Jersey** buscará las clases del servicio web, es decir, que clases son los recursos que el servicio web proporciona, por lo que esta propiedad debe apuntar al paquete que contiene la clase que se quiere exponer como recurso web a través de los parámetros **param-value**. La propiedad **url-pattern** define la parte base de la URL que la aplicación web servirá.

Una realizado todo lo anterior ya podemos lanzar la aplicación web, para ello es necesario ejecutar el proyecto como servidor. Esto se realiza haciendo click derecho con el ratón y elegir la opción de **Run as server**, con esta opción el contenedor web **Tomcat** echará a andar y ya se podrá acceder al recurso a través de la siguiente URL:

	http://localhost:8080/com.jmanday.jersey/rest/hello
	
El nombre que se visualizará del servicio web viene derivado del parámetro **display-name** dentro del fichero **web.xml**, que será tomado del nombre del proyecto y por tanto el mismo, argumento con el que el servlet mapea el **url-patern** y la anotación **@Path** del fichero de la clase. Es decir, la URL a la que se le harán las peticiones será tomada de ese parámetro, por lo que si el proyecto se llama la propiedad tiene el valor *com.jmanday.jersey*, las peticiones se harán a la URL:
	
	http://localhost:8080/com.jmanday.jersey

En este ejemplo el cliente realiza una petición de la representación HTML del recurso.


###Crear un cliente REST
**Jersey** contiene una librería REST cliente que puede ser usada para testear o construir un cliente real en Java.

Para hacer esto se tiene que crear un nuevo proyecto en Java al que llamaremos **com.jmanday.jersey2.cliente** y se le añadirá los ficheros JARs de la libreria **Jersey** a un directorio llamado *lib*, una vez copiados los ficheros y dentro del directorio se seleccionan todos y se añaden al **Build path** a través del click derecho del ratón. 

Una vez realizado lo anterior nos creamos la siguiente clase:

	package com.jmanday.jersey2.client;

	import java.net.URI;

	import javax.ws.rs.client.Client;
	import javax.ws.rs.client.ClientBuilder;
	import javax.ws.rs.client.WebTarget;
	import javax.ws.rs.core.MediaType;
	import javax.ws.rs.core.Response;
	import javax.ws.rs.core.UriBuilder;

	import org.glassfish.jersey.client.ClientConfig;

	public class Test {

		public static void main(String[] args) {
			ClientConfig config = new ClientConfig();

        	Client client = ClientBuilder.newClient(config);

        	WebTarget target = client.target(getBaseURI());

        	String response = target.path("rest").
                                 path("hello").
                                 request().
                                 accept(MediaType.TEXT_PLAIN).
                                 get(Response.class)
                                 .toString();


        	String plainAnswer = target.path("rest").path("hello").request().accept(MediaType.TEXT_PLAIN).get(String.class);
        	String xmlAnswer = target.path("rest").path("hello").request().accept(MediaType.TEXT_XML).get(String.class);
        	String htmlAnswer= target.path("rest").path("hello").request().accept(MediaType.TEXT_HTML).get(String.class);

        	System.out.println(response);
        	System.out.println(plainAnswer);
        	System.out.println(xmlAnswer);
        	System.out.println(htmlAnswer);
    	}

		private static URI getBaseURI() {
			return UriBuilder.fromUri("http://localhost:8080/com.vogella.jersey.first").build();
    	}
	}


###Servicio web RESTful y JAXB
La API de Java **JAX-RS** soporta la creación y mapeo automático de XML y JSON a través de **JAXB**.

Volvemos a crear un nuevo *proyecto web dinámico** llamado en este caso **p1-jaxb**. Hay que asegurarse que se crea el fichero **web.xml**.

Lo siguiente será crear la clase del modelo de dominio:

	package model;

	import javax.xml.bind.annotation.XmlRootElement;

	@XmlRootElement

	public class Todo {
		private String summary;
		private String description;
	
		public String getSummary(){
			return summary;
		}
	
		public void setSummaty(String summary){
			this.summary = summary;
		}
	
		public String getDescription(){
			return description;
		}
	
		public void setDescription(String description){
			this.description = description;
		}
	
	}
	
	
Ahora creamos la clase recurso del servico web que simplemente lo que hace es devolver una instancia de la clase creada anteriormente **Todo**:

	package model;

	import javax.ws.rs.GET;
	import javax.ws.rs.Path;
	import javax.ws.rs.Produces;
	import javax.ws.rs.core.MediaType;

	@Path("/todo")
	public class TodoResource {

		// Este método es llamado si la peticion es XML
    	@GET
    	@Produces( { MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
    	public Todo getXML() {
    	 	Todo todo = new Todo();
        	todo.setSummary("This is my first todo");
        	todo.setDescription("This is my first todo");
        	return todo;
    	}

    	// Este método puede ser usado para testear la integración con el navegador
    	@GET
    	@Produces( { MediaType.TEXT_XML })
    	public Todo getHTML() {
    	 	Todo todo = new Todo();
        	todo.setSummary("This is my first todo");
        	todo.setDescription("This is my first todo");
        	return todo;
    	}
	}

Lo siguiente será modificar el fichero **web.xml** para configurar los parámetros **display-name**, **param-value** y **url-pattern**. Una vez configuradas todas esas propiedades ejecutamos el servlet en el servidor.

Para probar el servicio web nos creamos un cliente desde un nuevo proyecto java con la siguiente clase de testeo:

	package com.jmanday.jersey2.jaxb.client;

	import java.net.URI;

	import javax.ws.rs.client.Client;
	import javax.ws.rs.client.ClientBuilder;
	import javax.ws.rs.client.WebTarget;
	import javax.ws.rs.core.MediaType;
	import javax.ws.rs.core.UriBuilder;

	import org.glassfish.jersey.client.ClientConfig;

	public class TodoTest {
		public static void main(String[] args) {
        	ClientConfig config = new ClientConfig();
        	Client client = ClientBuilder.newClient(config);

        	WebTarget target = client.target(getBaseURI());
        
        	// Get XML
        	String xmlResponse = target.path("rest").path("todo").request()
                        .accept(MediaType.TEXT_XML).get(String.class);
        	// Get XML for application
        	String xmlAppResponse =target.path("rest").path("todo").request()
                        .accept(MediaType.APPLICATION_XML).get(String.class);

        	// For JSON response also add the Jackson libraries to your webapplication
                        // In this case you would also change the client registration to
                        // ClientConfig config = new ClientConfig().register(JacksonFeature.class);
                        // Get JSON for application
                        // System.out.println(target.path("rest").path("todo").request()
                        // .accept(MediaType.APPLICATION_JSON).get(String.class));

        	System.out.println(xmlResponse);
        	System.out.println(xmlAppResponse);
		}

		private static URI getBaseURI() {
        	return UriBuilder.fromUri("http://localhost:8080/com.jmanday.jersey2.jaxb/rest/todo").build();
		}
	}


###Servicio web RESTful CRUD
Ahora vamos a crear un servicio web RESTful CRUD (Create, Read, Update, Delete). Esto permitirá mantener una lista de objetos de la clase **Todo** en la aplicación web a través de llamadas HTTP.

Para ello comenzamos creando un nuevo proyecto dinámico web como hasta ahora, se le añaden y configuran las librerías *jar* y se modifica el fichero **web.xml**.

Lo siguiente será crear el modelo de datos y un *Singleton* que ejerce como el proveedor de datos para el modelo. La clase **Todo** es anotada con la notación de **JAXB**.

	package com.jmanday.jersey2.crud.model;

	import javax.xml.bind.annotation.XmlRootElement;

	@XmlRootElement
	public class Todo {
		private String id;
    	private String summary;
    	private String description;

	    public Todo(){
	
	    }
	    
	    
	    public Todo (String id, String summary){
	    	this.id = id;
	    	this.summary = summary;    
	    }
	    
	    
	    public String getId() {
	    	return id;
	    }
      
    
	    public void setId(String id) {
	        this.id = id;
	    }
     
    
    	public String getSummary() {
	        return summary;
	    }
      
    
    	public void setSummary(String summary) {
        	this.summary = summary;
    	}
        
    
    	public String getDescription() {
        	return description;
    	}
        
    
    	public void setDescription(String description) {
        	this.description = description;
    	}
	}
	
La clase que implementará el patrón Singleton y que se encargará de proveer las instanscias de la clase *Todo*:

	package singleton;

	import java.util.HashMap;
	import java.util.Map;
	
	import com.jmanday.jersey2.crud.model.Todo;
	
	public enum TodoDao {
		instance;
		
		private Map<String, Todo> contentProvider = new HashMap<>();
		
		private TodoDao(){
			Todo todo = new Todo("1", "Learn Rest");
			todo.setDescription("Read tutorials");
			contentProvider.put("1", todo);
			
			todo = new Todo("2", "Do something");
			todo.setDescription("Read tutorials complete");
			contentProvider.put("2", todo);
		}
		
		public Map<String, Todo> getModel(){
			return contentProvider;
		}
	}
	
El servicio REST puede ser usado a través de formularios HTML, para comprobar el funcionamiento vamos a crear la siguiente página llamada *"create_todo.html"* en la carpeta **WebContent** que va a permitir enviar un nuevo dato al servicio:

	<!DOCTYPE html>
	<html>
	<head>
	<meta charset="UTF-8">
	<title>Formulario para crear un nuevo recurso</title>
	</head>
	<body>
		<form action="../com.jmanday.jersey2.crud/rest/todos" method="POST">
	    	<label for="id">ID</label>
	        <input name="id" />
	        <br/>
	        <label for="summary">Summary</label>
	        <input name="summary" />
	        <br/>
	        Description:
	        <TEXTAREA NAME="description" COLS=40 ROWS=6></TEXTAREA>
	        <br/>
	        <input type="submit" value="Submit" />
	        </form>
	</body>
	</html>
	
Ahora creamos la clase que será usada como un recurso REST:

	package com.jmanday.jersey2.crud.resources;
	
	import javax.ws.rs.Consumes;
	import javax.ws.rs.DELETE;
	import javax.ws.rs.GET;
	import javax.ws.rs.PUT;
	import javax.ws.rs.Produces;
	import javax.ws.rs.core.Context;
	import javax.ws.rs.core.MediaType;
	import javax.ws.rs.core.Request;
	import javax.ws.rs.core.Response;
	import javax.ws.rs.core.UriInfo;
	import javax.xml.bind.JAXBElement;
	
	import com.jmanday.jersey2.crud.model.Todo;
	import com.jmanday.jersey2.crud.singleton.TodoDao;
	
	public class TodoResource {
		@Context
	    UriInfo uriInfo;
	    @Context
	    Request request;
	    String id;
	    
	    public TodoResource(UriInfo uriInfo, Request request, String id) {
	    	this.uriInfo = uriInfo;
	        this.request = request;
	        this.id = id;
	    }
	
	    //Application integration
	    @GET
	    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
	    public Todo getTodo() {
	    	Todo todo = TodoDao.instance.getModel().get(id);
	    	if(todo==null)
	    		throw new RuntimeException("Get: Todo with " + id +  " not found");
	        return todo;
	    }
	
	    // for the browser
	    @GET
	    @Produces(MediaType.TEXT_XML)
	    public Todo getTodoHTML() {
	    	Todo todo = TodoDao.instance.getModel().get(id);
	        if(todo==null)
	        	throw new RuntimeException("Get: Todo with " + id +  " not found");
	        return todo;
	    }
	
	    @PUT
	    @Consumes(MediaType.APPLICATION_XML)
	    public Response putTodo(JAXBElement<Todo> todo) {
	    	Todo c = todo.getValue();
	    	return putAndGetResponse(c);
	    }
	
	    @DELETE
	    public void deleteTodo() {
	    	Todo c = TodoDao.instance.getModel().remove(id);
	        if(c==null)
	        	throw new RuntimeException("Delete: Todo with " + id +  " not found");
	    }
	
	    private Response putAndGetResponse(Todo todo) {
	    	Response res;
	        if(TodoDao.instance.getModel().containsKey(todo.getId())) {
	        	res = Response.noContent().build();
	        } else {
	        	res = Response.created(uriInfo.getAbsolutePath()).build();
	        }
	        TodoDao.instance.getModel().put(todo.getId(), todo);
	        return res;
	    }
	
	}
	
Esta última clase tiene la anotación **@PathParam** para definir que el *id* es insertado como parámetro:

	package com.jmanday.jersey2.crud.resources;
	
	import java.io.IOException;
	import java.util.ArrayList;
	import java.util.List;
	
	import javax.servlet.http.HttpServletResponse;
	import javax.ws.rs.Consumes;
	import javax.ws.rs.FormParam;
	import javax.ws.rs.GET;
	import javax.ws.rs.POST;
	import javax.ws.rs.Path;
	import javax.ws.rs.PathParam;
	import javax.ws.rs.Produces;
	import javax.ws.rs.core.Context;
	import javax.ws.rs.core.MediaType;
	import javax.ws.rs.core.Request;
	import javax.ws.rs.core.UriInfo;
	
	import com.jmanday.jersey2.crud.model.Todo;
	import com.jmanday.jersey2.crud.singleton.TodoDao;
	
	// Will map the resource to the URL todos
	@Path("/todos")
	public class TodosResource {
	
		// Allows to insert contextual objects into the class,
	    // e.g. ServletContext, Request, Response, UriInfo
	    @Context
	    UriInfo uriInfo;
	    @Context
	    Request request;
	
	    // Return the list of todos to the user in the browser
	    @GET
	    @Produces(MediaType.TEXT_XML)
	    public List<Todo> getTodosBrowser() {
	            List<Todo> todos = new ArrayList<Todo>();
	            todos.addAll(TodoDao.instance.getModel().values());
	            return todos;
	    }
	
	    // Return the list of todos for applications
	    @GET
	    @Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
	    public List<Todo> getTodos() {
	            List<Todo> todos = new ArrayList<Todo>();
	            todos.addAll(TodoDao.instance.getModel().values());
	            return todos;
	    }
	
	    // retuns the number of todos
	    // Use http://localhost:8080/com.vogella.jersey.todo/rest/todos/count
	    // to get the total number of records
	    @GET
	    @Path("count")
	    @Produces(MediaType.TEXT_PLAIN)
	    public String getCount() {
	            int count = TodoDao.instance.getModel().size();
	            return String.valueOf(count);
	    }
	
	    @POST
	    @Produces(MediaType.TEXT_HTML)
	    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
	    public void newTodo(@FormParam("id") String id,
	                    @FormParam("summary") String summary,
	                    @FormParam("description") String description,
	                    @Context HttpServletResponse servletResponse) throws IOException {
	            Todo todo = new Todo(id, summary);
	            if (description != null) {
	                    todo.setDescription(description);
	            }
	            TodoDao.instance.getModel().put(id, todo);
	
	            servletResponse.sendRedirect("../create_todo.html");
	    }
	
	    // Defines that the next path parameter after todos is
	    // treated as a parameter and passed to the TodoResources
	    // Allows to type http://localhost:8080/com.vogella.jersey.todo/rest/todos/1
	    // 1 will be treaded as parameter todo and passed to TodoResource
	    @Path("{todo}")
	    public TodoResource getTodo(@PathParam("todo") String id) {
	            return new TodoResource(uriInfo, request, id);
	    }
	}
	
Una vez configurado todo probamos la aplicación web ejecutándola en el servidor de Tomcat:

- probandola desde el propio Eclipse para hacerle una petición GET de texto plano
![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p3-2.png)

- y desde el navegador web para hacerle una petición GET de aplicación XML
![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p3-3.png)


También es posible hacer peticiones para obtener el número de instancias *Todo* creadas de la siguiente manera:

	http://localhost:8080/com.jmanday.jersey2.crud/rest/todos/count
	
![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p3-4.png)	

O incluso para conocer los datos de una instancia *Todo* con un identificador propio:

	 http://localhost:8080/com.jmanday.jersey2.crud/rest/todos/1
	
![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p3-5.png)	
	

Para testear el servicio web vamos a crear un cliente en el propio proyecto a diferencia de como en los ejemplos anteriores donde se ha creado en un proyecto a parte.

	package com.jmanday.jersey2.crud.client;
	
	import java.net.URI;
	
	import javax.ws.rs.client.Client;
	import javax.ws.rs.client.ClientBuilder;
	import javax.ws.rs.client.Entity;
	import javax.ws.rs.client.WebTarget;
	import javax.ws.rs.core.Form;
	import javax.ws.rs.core.MediaType;
	import javax.ws.rs.core.Response;
	import javax.ws.rs.core.UriBuilder;
	
	import org.glassfish.jersey.client.ClientConfig;
	
	import com.jmanday.jersey2.crud.model.Todo;
	
	public class Tester {
		
		public static void main(String[] args) {
			ClientConfig config = new ClientConfig();
	        Client client = ClientBuilder.newClient(config);
	        WebTarget service = client.target(getBaseURI());
	
	        // create one todo
	        Todo todo = new Todo("3", "Blabla");
	        Response response = service.path("rest").path("todos").path(todo.getId()).request(MediaType.APPLICATION_XML).put(Entity.entity(todo,MediaType.APPLICATION_XML),Response.class);
	
	        // Return code should be 201 == created resource
	        System.out.println(response.getStatus());
	
	        // Get the Todos
	        System.out.println(service.path("rest").path("todos").request().accept(MediaType.TEXT_XML).get(String.class));
	
	//        // Get JSON for application
	//        System.out.println(service.path("rest").path("todos").request().accept(MediaType.APPLICATION_JSON).get(String.class));
	
	        // Get XML for application
	        System.out.println(service.path("rest").path("todos").request().accept(MediaType.APPLICATION_XML).get(String.class));
	
	        //Get Todo with id 1
	        Response checkDelete = service.path("rest").path("todos/1").request().accept(MediaType.APPLICATION_XML).get();
	
	        //Delete Todo with id 1
	        service.path("rest").path("todos/1").request().delete();
	
	        //Get get all Todos id 1 should be deleted
	        System.out.println(service.path("rest").path("todos").request().accept(MediaType.APPLICATION_XML).get(String.class));
	
	        //Create a Todo
	        Form form =new Form();
	        form.param("id", "4");
	        form.param("summary","Demonstration of the client lib for forms");
	        response = service.path("rest").path("todos").request().post(Entity.entity(form,MediaType.APPLICATION_FORM_URLENCODED),Response.class);
	        System.out.println("Form response " + response.getStatus());
	
	        //Get all the todos, id 4 should have been created
	        System.out.println(service.path("rest").path("todos").request().accept(MediaType.APPLICATION_XML).get(String.class));
	
		}
	
		
		private static URI getBaseURI() {
			return UriBuilder.fromUri("http://localhost:8080/com.jmanday.jersey2.crud").build();
		}
	} 
	
El ejemplo anterior contiene un formulario para llamar a un método POST del servicio web.

###Esquema 
En la siguiente imagen se muestra un esquema de los componentes que forman el servicio web **RESTful**:


![alt text](https://raw.githubusercontent.com/jmanday/Images/master/DSS/dss-p3-6.png)	