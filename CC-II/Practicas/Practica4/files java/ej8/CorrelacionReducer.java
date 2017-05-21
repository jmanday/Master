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
public class CorrelacionReducer extends MapReduceBase implements Reducer<Text, DoubleWritable, Text, DoubleWritable> {
	

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
		mc0 = (sumc0 / tam);
		mc1 = (sumc1 / tam);

		//cálculo de las desviaciones típicas
		desv_c0 = Math.sqrt((sum_pow_c0 / tam) - Math.pow(mc0,2));
		desv_c1 = Math.sqrt((sum_pow_c1 / tam) - Math.pow(mc1,2));

		//cálculo de la covarianza
		cov = (sum_prod_c0c1 / tam) - (mc0 * mc1);

		//cálculo de la correlación
		corr = (cov / (desv_c0 * desv_c1));

		output.collect(key, new DoubleWritable(corr));
	}
}
