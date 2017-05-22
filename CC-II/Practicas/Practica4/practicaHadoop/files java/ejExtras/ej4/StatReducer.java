package oldapi;
import java.io.IOException;
import java.util.Iterator;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;
public class StatReducer extends MapReduceBase implements Reducer<Text, DoubleWritable, Text, DoubleWritable> {
	

	public void reduce(Text key, Iterator<DoubleWritable> values, OutputCollector<Text, DoubleWritable> output, Reporter reporter) throws IOException {
		Double value = 0.0, sumc0 = 0.0, sumc1 = 0.0, mc0 = 0.0, mc1 = 0.0, prod_c0c1 = 0.0, sum_prod_c0c1 = 0.0;
		Double sum_pow_c0 = 0.0, sum_pow_c1 = 0.0, desv_c0 = 0.0, desv_c1 = 0.0, cov = 0.0, corr = 0.0;
		int i = 0, tam = 0;
		
		while (values.hasNext()) {
			value = values.next().get();
			if(i%2 == 0){
				if(i != 0)
					sum_prod_c0c1 += prod_c0c1;
				
				prod_c0c1 = value;
				sumc0 += value;
				sum_pow_c0 += Math.pow(value, 2);
			}
			else{
				prod_c0c1 = prod_c0c1 * value;
				sumc1 += value;
				sum_pow_c1 += Math.pow(value, 2);
			}

			i++;
		}
		
		tam = i / 2;
		//cálculo de las medias
		mc0 = (sumc0 / tam);
		mc1 = (sumc1 / tam);

		String med0 = key.toString().charAt(0)	+ "-Media";
                Text keyMed0 = new Text(med0);
                output.collect(keyMed0, new DoubleWritable(mc0));

                String med1 = key.toString().charAt(1) + "-Media";
                Text keyMed1 = new Text(med1);
                output.collect(keyMed1, new DoubleWritable(mc1));

		//cálculo de las desviaciones típicas
		desv_c0 = Math.sqrt((sum_pow_c0 / tam) - Math.pow(mc0,2));
		desv_c1 = Math.sqrt((sum_pow_c1 / tam) - Math.pow(mc1,2));

		String desv0 = key.toString().charAt(0) + "-Desv. Tipica";
		Text keyDesv0 = new Text(desv0);
		output.collect(keyDesv0, new DoubleWritable(desv_c0));

		String desv1 = key.toString().charAt(1)	+ "-Desv. Tipica";
		Text keyDesv1 = new Text(desv1);
                output.collect(keyDesv1, new DoubleWritable(desv_c1));

		//cálculo de la covarianza
		cov = (sum_prod_c0c1 / tam) - (mc0 * mc1);
		
		String txtCov = key.toString() + "-Covarianza";
		Text keyCov = new Text(txtCov);
		output.collect(keyCov, new DoubleWritable(cov));

		//cálculo de la correlación
		corr = (cov / (desv_c0 * desv_c1));

		String txt = key.toString() + "-Coe. Correl";
		Text keyCorr = new Text(txt);
		output.collect(keyCorr, new DoubleWritable(corr));
	}
}
