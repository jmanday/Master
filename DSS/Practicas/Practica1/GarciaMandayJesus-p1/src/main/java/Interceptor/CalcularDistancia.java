package Interceptor;

public class CalcularDistancia implements Filter {

	private static final int RADIO = 2;

	@Override
	public double execute(Object o) {
		double revolAnt = 1.34;
		double revoluciones = (double) o;
		double distancia = (revoluciones - revolAnt) * 2* RADIO * 3.1416;
		return distancia;
	}

}
