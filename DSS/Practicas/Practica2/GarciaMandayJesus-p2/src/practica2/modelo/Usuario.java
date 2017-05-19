package practica2.modelo;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Usuario {
	@Id
	@GeneratedValue(strategy = GenerationType.TABLE)
	private long id;
	private String nombre;
	private String apellido;
	private String email;
	
	public Usuario(){}
	
	public Usuario(Usuario us){
		this.id = us.getId();
		this.nombre = us.getNombre();
		this.apellido = us.getApellido();
		this.email = us.getEmail();
	}
	
	public long getId(){
		return id;
	}
	
	public void setId(long id){
		this.id = id;
	}
	
	public String getNombre(){
		return nombre;
	}
	
	public void setNombre(String nombre){
		this.nombre = nombre;
	}
	
	public String getApellido(){
		return apellido;
	}
	
	public void setApellido(String apellido){
		this.apellido = apellido;
	}
	
	public String getEmail(){
		return email;
	}
	
	public void setEmail(String email){
		this.email = email;
	}
	
	@Override
	public String toString(){
		return nombre + " " + apellido + " " + email;
	}
}
