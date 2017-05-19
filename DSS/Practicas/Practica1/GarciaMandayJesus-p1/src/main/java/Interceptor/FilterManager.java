package Interceptor;

public class FilterManager {
	private FilterChain filterChain;
	
	public FilterManager(Interfaz objetivo){
		filterChain = new FilterChain();
		filterChain.setInterfaz(objetivo);
	}
	
	public void setFilter(Filter filter){
		filterChain.addFilter(filter);
	}
	
	public void filterRequest(Double request){
		filterChain.execute(request);
	}
}
