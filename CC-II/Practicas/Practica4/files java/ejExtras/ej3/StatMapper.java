package oldapi;
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;
public class StatMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, DoubleWritable> {
       
        public void map(LongWritable key, Text value, OutputCollector<Text, DoubleWritable> output, Reporter reporter) throws IOException{
                String line = value.toString();
                String[] parts = line.split(",");
                for(int i = 0; i < parts.length - 1; i++){
			for(int j = i; j < parts.length - 1; j++){
				if(i != j){
					String nkey = String.valueOf(i+1) + "-" + String.valueOf(j+1);
                			output.collect(new Text(nkey), new DoubleWritable(Double.parseDouble(parts[i])));
					output.collect(new Text(nkey), new DoubleWritable(Double.parseDouble(parts[j])));
				}
			}
		}
        }
}
