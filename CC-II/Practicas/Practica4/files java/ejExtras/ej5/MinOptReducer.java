package oldapi;
import java.io.IOException;
import java.util.Iterator;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MinOptReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {
	
	public void reduce(Text key, Iterator<DoubleWritable> values, Context context) throws IOException, InterruptedException {
		Double min = values.next().get();
		context.write(key, new DoubleWritable(min));
	}
}
