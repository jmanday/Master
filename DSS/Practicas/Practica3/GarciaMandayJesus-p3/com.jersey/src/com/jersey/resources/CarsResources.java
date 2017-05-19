package com.jersey.resources;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.Consumes;
import javax.ws.rs.FormParam;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.DELETE;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Request;
import javax.ws.rs.core.UriInfo;

import com.jersey.model.Car;
import com.jersey.singleton.CarDao;

// Will map the resource to the URL cars
@Path("/cars")
public class CarsResources {
	
	// Allows to insert contextual objects into the class,
    // e.g. ServletContext, Request, Response, UriInfo
    @Context
    UriInfo uriInfo;
    @Context
    Request request;

    // Return the list of cars to the user in the browser
    @GET
    @Produces(MediaType.TEXT_XML)
    public List<Car> getCarsBrowser() {
    	List<Car> cars = new ArrayList<Car>();
        cars.addAll(CarDao.instance.getModel().values());
        return cars;
    }

    // Return the list of cars for applications
    @GET
    @Produces({ MediaType.APPLICATION_XML, MediaType.APPLICATION_JSON })
    public List<Car> getCars() {
    	List<Car> cars = new ArrayList<Car>();
    	cars.addAll(CarDao.instance.getModel().values());
        return cars;
    }

    // retuns the number of cars
    // Use http://localhost:8080/com.vogella.jersey.todo/rest/todos/count
    // to get the total number of records
    @GET
    @Path("count")
    @Produces(MediaType.TEXT_PLAIN)
    public String getCount() {
    	int count = CarDao.instance.getModel().size();
        return String.valueOf(count);
    }

    @POST
    @Produces(MediaType.TEXT_HTML)
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    public void newCar(@FormParam("registration_number") String registrarion_number,
                    @FormParam("mask") String mask,
                    @FormParam("colour") String colour,
                    @FormParam("kilometers") String kilometers,
                    @Context HttpServletResponse servletResponse) throws IOException {
    	Car car = new Car(registrarion_number, mask, colour, kilometers);
         
    	CarDao.instance.getModel().put(registrarion_number, car);

    	servletResponse.sendRedirect("../create_car.html");
    }
    

    // Defines that the next path parameter after todos is
    // treated as a parameter and passed to the TodoResources
    // Allows to type http://localhost:8080/com.vogella.jersey.todo/rest/todos/1
    // 1 will be treaded as parameter todo and passed to TodoResource
    @Path("{car}")
    public CarResource getCarResource(@PathParam("car") String id) {
    	return new CarResource(uriInfo, request, id);
    }
}
