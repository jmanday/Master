package com.jersey.model;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement

public class Car {
	private String registration_number;
	private String mark;
	private String colour;
	private String kilometers;
	
	public Car(){
		
	}
	
	public Car(String  registration_number, String mark, String colour, String kilometers){
		this.registration_number = registration_number;
		this.mark = mark;
		this.colour = colour;
		this.kilometers = kilometers;
	}
	
	
	public void setRegistrarionNumber(String registration_number){
		this.registration_number = registration_number;
	}
	
	
	public String getRegistrationNumber(){
		return registration_number;
	}
	
	
	public void setMark(String mark){
		this.mark = mark;
	}
	
	
	public String getMark(){
		return mark;
	}
	
	
	public void setColour(String colour){
		this.colour = colour;
	}
	
	
	public String getColour(){
		return colour;
	}
	
	
	public void setKilometers(String kilometers){
		this.kilometers = kilometers;
	}
	
	
	public String getKilometers(){
		return kilometers;
	}
}
