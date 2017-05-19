package com.jersey.singleton;

import java.util.HashMap;
import java.util.Map;

import com.jersey.model.Car;

public enum CarDao {
	instance;
	
	private Map<String, Car> contentProvider = new HashMap<>();
	
	private CarDao(){
		Car mycar = new Car("4532DEV", "Renault", "Negro", "780");
		contentProvider.put("4532DEV", mycar);
		
		mycar = new Car("8564GBS", "Mercedes", "Blanco", "1123");
		contentProvider.put("8564GBS", mycar);
		
		mycar = new Car("9654DFS", "Ford", "Gris", "120");
		contentProvider.put("9654DFS", mycar);
	}
	
	public Map<String, Car> getModel(){
		return contentProvider;
	}
}
