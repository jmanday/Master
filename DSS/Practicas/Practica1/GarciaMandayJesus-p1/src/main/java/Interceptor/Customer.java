package Interceptor;

public class Customer {
	private FilterManager filterManager;
	
	public void setFilterManager(FilterManager filterManager){
		this.filterManager = filterManager;
	}
	
	public void sendRequest(Double d){
		filterManager.filterRequest(d);
	}
}
