package com.jersey.resources;

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

import com.jersey.model.Car;
import com.jersey.singleton.CarDao;

public class CarResource {
	@Context
    UriInfo uriInfo;
    @Context
    Request request;
    String id;
    
    public CarResource(UriInfo uriInfo, Request request, String id) {
    	this.uriInfo = uriInfo;
        this.request = request;
        this.id = id;
    }

    //Application integration
    @GET
    @Produces({MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON})
    public Car getCar() {
    	Car car = CarDao.instance.getModel().get(id);
    	if(car==null)
    		throw new RuntimeException("Get: Car with " + id +  " not found - Type APP_XML/APP_JSON");
        return car;
    }

    // for the browser
    @GET
    @Produces(MediaType.TEXT_XML)
    public Car getCarHTML() {
    	Car car = CarDao.instance.getModel().get(id);
        if(car==null)
        	throw new RuntimeException("Get: Car with " + id +  " not found - Type TEXT_XML");
        return car;
    }

    @PUT
    @Consumes(MediaType.APPLICATION_XML)
    public Response putCar(JAXBElement<Car> car) {
    	Car c = car.getValue();
    	return putAndGetResponse(c);
    }

    @DELETE
    public void deleteCar() {
    	Car c = CarDao.instance.getModel().remove(id);
        if(c==null)
        	throw new RuntimeException("Delete: Car with " + id +  " not found");
    }

    private Response putAndGetResponse(Car car) {
    	Response res;
        if(CarDao.instance.getModel().containsKey(car.getRegistrationNumber())) {
        	res = Response.noContent().build();
        } else {
        	res = Response.created(uriInfo.getAbsolutePath()).build();
        }
        
        CarDao.instance.getModel().put(car.getRegistrationNumber(), car);
        return res;
    }
}
