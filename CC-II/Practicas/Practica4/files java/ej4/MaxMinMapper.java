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
public class MaxMinMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, DoubleWritable> {
        public static int col=5;

        public void map(LongWritable key, Text value, OutputCollector<Text, DoubleWritable> output, Reporter reporter) throws IOException{
                String line = value.toString();
                String[] parts = line.split(",");
		for(int i = 1; i < parts.length; i++)
                	output.collect(new Text(String.valueOf(i)), new DoubleWritable(Double.parseDouble(parts[i-1])));
        }
}
