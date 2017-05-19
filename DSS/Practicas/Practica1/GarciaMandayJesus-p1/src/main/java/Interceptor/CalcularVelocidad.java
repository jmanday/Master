package Interceptor;

public class CalcularVelocidad implements Filter {

	private static final double INTERVALO = 2.4;

	@Override
	public double execute(Object o) {
		double distancia= (double) o;
		double velocidad= distancia*3600.0/INTERVALO;
		return velocidad ;
	}

}
