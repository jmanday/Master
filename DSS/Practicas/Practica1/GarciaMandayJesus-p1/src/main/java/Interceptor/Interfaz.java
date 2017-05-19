package Interceptor;

import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public class Interfaz {
	
	private static String URL = "http://localhost:8080/practica1/home.jsf";
	
	public Object execute(Object o){

        if (Desktop.isDesktopSupported()) {
            try {
				Desktop.getDesktop().browse(new URI(URL));
			} catch (IOException | URISyntaxException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

        }
		return o;
	}
}
