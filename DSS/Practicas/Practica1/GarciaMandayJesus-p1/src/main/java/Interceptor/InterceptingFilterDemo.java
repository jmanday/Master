package Interceptor;

public class InterceptingFilterDemo {
	public static void main(String[] args){
		
		FilterManager filterManager = new FilterManager(new Interfaz());
		filterManager.setFilter(new CalcularVelocidad());
		
		Customer client = new Customer();
		client.setFilterManager(filterManager);
		client.sendRequest(500.0);
	}
}
