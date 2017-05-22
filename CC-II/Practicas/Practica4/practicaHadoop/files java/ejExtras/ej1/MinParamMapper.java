package oldapi;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.conf.Configuration;

public class MinParamMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {
        private static int col=0;
	private static List<Double> list = new ArrayList<>();

        public void map(LongWritable key, Text value, Context context) throws IOException{
                Configuration conf = context.getConfiguration();
		String line = value.toString();
                String[] parts = line.split(",");
		col = Integer.parseInt(conf.get("col"));
                list.add(Double.parseDouble(parts[col]));
       }

	protected void cleanup(Context context) throws IOException, InterruptedException{
                Collections.sort(list);
                context.write(new Text("Min"), new DoubleWritable(list.get(0)));
        }
}
