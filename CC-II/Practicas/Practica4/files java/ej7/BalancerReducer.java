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
public class BalancerReducer extends MapReduceBase implements Reducer<Text, DoubleWritable, Text, DoubleWritable> {
	

	public void reduce(Text key, Iterator<DoubleWritable> values, OutputCollector<Text, DoubleWritable> output, Reporter reporter) throws IOException {
		Double c0 = 0.0, c1 = 0.0;
		Double bal = 0.0;

		while (values.hasNext()) {
			if(values.next().get() == 0.0)
				c0++;
			else
				c1++;
		}

		bal = (c0 > c1)? c0/c1 : c1/c0;
		output.collect(key, new DoubleWritable(bal));
	}
}
