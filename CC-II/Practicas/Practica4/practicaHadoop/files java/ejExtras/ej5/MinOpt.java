package oldapi;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.util.Tool; 
import org.apache.hadoop.util.ToolRunner;

public class MinOpt extends Configured implements Tool{
	
	public static void main(String[] args) throws Exception {
		int res = ToolRunner.run(new Configuration(), new MinOpt(), args);
		System.exit(res);
	}

	public int run(String args[]) throws Exception{
	
		Configuration conf = new Configuration(true);
		Job job = new Job(conf, "MinOpt");
		job.setJarByClass(MinOpt.class);
                job.setMapperClass(MinOptMapper.class);
                job.setReducerClass(MinOptReducer.class);
                job.setOutputKeyClass(Text.class);
                job.setOutputValueClass(DoubleWritable.class);
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		return job.waitForCompletion(true)? 0 : 1;
	}
}
