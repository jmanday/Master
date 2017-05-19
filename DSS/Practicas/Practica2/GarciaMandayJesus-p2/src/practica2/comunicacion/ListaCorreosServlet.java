package practica2.comunicacion;

import practica2.modelo.*;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class ListaCorreosServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	private static final String EXPR_REG_EMAIL = "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
			+ "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$";

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doPost(request,response);
	}
	
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		try {
			String accion = request.getParameter("action"); 
			if (accion.equals("listarUsuarios")) {
				List<Usuario> lista = BDUsuario.listarUsuarios();
				ObjectOutputStream objOut = new ObjectOutputStream(response.getOutputStream());
				objOut.writeObject(lista);
				objOut.flush();
				objOut.close();
			}
			else if (accion.equals("aniadirUsuario")) {
				final Pattern pattern = Pattern.compile(EXPR_REG_EMAIL);
				
				ObjectOutputStream output = new ObjectOutputStream(response.getOutputStream());
				try {
					String nombre   = request.getParameter("nombre"),
					       apellido = request.getParameter("apellido"),
					       email    = request.getParameter("email");

					Matcher matcher = pattern.matcher(email);
					
					if (BDUsuario.existeEmail(email)) {
						output.writeInt(1);
						output.writeObject("Usuario ya existente");
					}
					else if (!matcher.matches()){
						output.writeInt(2);
						output.writeObject("Correo electronico no valido");
					}
					else {
						Usuario usuario = new Usuario();
						usuario.setNombre(nombre);
						usuario.setApellido(apellido);
						usuario.setEmail(email);
						
						BDUsuario.insertar(usuario);

						output.writeInt(0);
						output.writeObject("Usuario añadido correctamente");
					}
				} catch (Exception e) {
					output.writeInt(-1);
					output.writeObject("Error al añadir usuario");
				} finally {
					output.flush();
					output.close();
				}
			}
			else if (accion.equals("actualizarUsuario")) {
				ObjectOutputStream output = new ObjectOutputStream(response.getOutputStream());
				try {
					String nombre   = request.getParameter("nombre"),
					       apellido = request.getParameter("apellido"),
					       email    = request.getParameter("email");
					
					if (BDUsuario.existeEmail(email)) {
						Usuario usuario = new Usuario();
						usuario.setNombre(nombre);
						usuario.setApellido(apellido);
						usuario.setEmail(email);
						
						BDUsuario.actualizar(usuario);
						
						output.writeInt(0);
						output.writeObject("Usuario actualizado");
					}
					else {
						output.writeInt(1);
						output.writeObject("El usuario no existe");
					}
				} catch (Exception e) {
					output.writeInt(-1);
					output.writeObject("Error al actualizar usuario");
				} finally {
					output.flush();
					output.close();
				}
			}
			else if (accion.equals("eliminarUsuario")) {
				ObjectOutputStream output = new ObjectOutputStream(response.getOutputStream());
				try {
					String email = request.getParameter("email");
					
					if (BDUsuario.existeEmail(email)) {
						Usuario usuario = BDUsuario.seleccionarUsuario(email);
						BDUsuario.eliminar(usuario);
						
						output.writeInt(0);
						output.writeObject("Usuario eliminado");
					}
					else {
						output.writeInt(1);
						output.writeObject("El usuario no existe");
					}
				} catch (Exception e) {
					output.writeInt(-1);
					output.writeObject("Error al eliminar usuario");
				} finally {
					output.flush();
					output.close();
				}
			}
			else {
				ObjectOutputStream output = new ObjectOutputStream(response.getOutputStream());
				
				output.writeInt(-2);
				output.writeObject("Accion no permitida");
				output.flush();
				output.close();
			}
		}
		catch(Exception e) {
			response.setContentType("text/html");
			PrintWriter out = response.getWriter();
			out.println("<h1>" + "Lista de usuarios" + "</h1>");
			
			out.println("<table>");
			out.println("<tr><th>Nombre</th><th>Apellido</th><th>Email</th>");
			if (BDUsuario.listarUsuarios() != null){
				for(Usuario u : BDUsuario.listarUsuarios()) {	
					out.println("<tr><td>" + u.getNombre() + "</td>");
					out.println("<td>" + u.getApellido() + "</td>");
					out.println("<td>" + u.getEmail() + "</td></tr>");
				}
			}
			out.println("</table>");
		}
	}
}