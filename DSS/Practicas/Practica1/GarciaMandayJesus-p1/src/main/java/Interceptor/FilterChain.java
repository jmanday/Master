package Interceptor;

import java.util.ArrayList;
import java.util.List;

public class FilterChain {
	private List<Filter> filters = new ArrayList<Filter>();
	private Interfaz objetivo;
	
	public void addFilter(Filter filter){
		filters.add(filter);
	}
	
	public void setInterfaz(Interfaz objetivo){
		this.objetivo = objetivo;
	}
	
	public void execute(Double request){
		for(Filter filter : filters)
			System.out.println("Nueva velocidad (m/s) " + filter.execute(request));
		
		objetivo.execute(request);
	}
}
