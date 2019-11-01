

# Rumen

* * *

  * Overview
    * Motivation
    * Components
  * How to use Rumen?
    * Trace Builder
    * Folder
  * Appendix
    * Resources
    * Dependencies



* * *

## Overview

Rumen is a data extraction and analysis tool built for Apache Hadoop. Rumen mines JobHistory logs to extract meaningful data and stores it in an easily-parsed, condensed format or digest. The raw trace data from MapReduce logs are often insufficient for simulation, emulation, and benchmarking, as these tools often attempt to measure conditions that did not occur in the source data. For example, if a task ran locally in the raw trace data but a simulation of the scheduler elects to run that task on a remote rack, the simulator requires a runtime its input cannot provide. To fill in these gaps, Rumen performs a statistical analysis of the digest to estimate the variables the trace doesn’t supply. Rumen traces drive both Gridmix (a benchmark of Hadoop MapReduce clusters) and SLS (a simulator for the resource manager scheduler).

### Motivation

  * Extracting meaningful data from JobHistory logs is a common task for any tool built to work on MapReduce. It is tedious to write a custom tool which is so tightly coupled with the MapReduce framework. Hence there is a need for a built-in tool for performing framework level task of log parsing and analysis. Such a tool would insulate external systems depending on job history against the changes made to the job history format.

  * Performing statistical analysis of various attributes of a MapReduce Job such as task runtimes, task failures etc is another common task that the benchmarking and simulation tools might need. Rumen generates


[ *Cumulative Distribution Functions (CDF)* ](http://en.wikipedia.org/wiki/Cumulative_distribution_function) for the Map/Reduce task runtimes. Runtime CDF can be used for extrapolating the task runtime of incomplete, missing and synthetic tasks. Similarly CDF is also computed for the total number of successful tasks for every attempt. 

### Components

Rumen consists of 2 components

  * Trace Builder : Converts JobHistory logs into an easily-parsed format. Currently TraceBuilder outputs the trace in [JSON](http://www.json.org/) format.

  * *Folder *: A utility to scale the input trace. A trace obtained from TraceBuilder simply summarizes the jobs in the input folders and files. The time-span within which all the jobs in a given trace finish can be considered as the trace runtime. Folder can be used to scale the runtime of a trace. Decreasing the trace runtime might involve dropping some jobs from the input trace and scaling down the runtime of remaining jobs. Increasing the trace runtime might involve adding some dummy jobs to the resulting trace and scaling up the runtime of individual jobs.




## How to use Rumen?

Converting JobHistory logs into a desired job-trace consists of 2 steps

  1. Extracting information into an intermediate format

  2. Adjusting the job-trace obtained from the intermediate trace to have the desired properties.




> Extracting information from JobHistory logs is a one time operation. This so called Gold Trace can be reused to generate traces with desired values of properties such as output-duration, concentration etc.

Rumen provides 2 basic commands

  * TraceBuilder
  * Folder



Firstly, we need to generate the Gold Trace. Hence the first step is to run TraceBuilder on a job-history folder. The output of the TraceBuilder is a job-trace file (and an optional cluster-topology file). In case we want to scale the output, we can use the Folder utility to fold the current trace to the desired length. The remaining part of this section explains these utilities in detail.

### Trace Builder

#### Command
    
    
    hadoop rumentrace [options] <jobtrace-output> <topology-output> <inputs>
    

This command invokes the TraceBuilder utility of Rumen.

TraceBuilder converts the JobHistory files into a series of JSON objects and writes them into the <jobtrace-output> file. It also extracts the cluster layout (topology) and writes it in the<topology-output> file. <inputs> represents a space-separated list of JobHistory files and folders.

> 1) Input and output to TraceBuilder is expected to be a fully qualified FileSystem path. So use file:// to specify files on the local FileSystem and <hdfs://> to specify files on HDFS. Since input files or folder are FileSystem paths, it means that they can be globbed. This can be useful while specifying multiple file paths using regular expressions.
> 
> 2) By default, TraceBuilder does not recursively scan the input folder for job history files. Only the files that are directly placed under the input folder will be considered for generating the trace. To add all the files under the input directory by recursively scanning the input directory, use ‘-recursive’ option.

Cluster topology is used as follows :

  * To reconstruct the splits and make sure that the distances/latencies seen in the actual run are modeled correctly.

  * To extrapolate splits information for tasks with missing splits details or synthetically generated tasks.




#### Options

Parameter |  Description |  Notes   
---|---|---  
-demuxer | Used to read the jobhistory files. The default is DefaultInputDemuxer. | Demuxer decides how the input file maps to jobhistory file(s). Job history logs and job configuration files are typically small files, and can be more effectively stored when embedded in some container file format like SequenceFile or TFile. To support such usage cases, one can specify a customized Demuxer class that can extract individual job history logs and job configuration files from the source files.   
-recursive | Recursively traverse input paths for job history logs. | This option should be used to inform the TraceBuilder to recursively scan the input paths and process all the files under it. Note that, by default, only the history logs that are directly under the input folder are considered for generating the trace.   
  
#### Example
    
    
    hadoop rumentrace \
      file:///tmp/job-trace.json \
      file:///tmp/job-topology.json \
      hdfs:///tmp/hadoop-yarn/staging/history/done_intermediate/testuser
    

This will analyze all the jobs in /tmp/hadoop-yarn/staging/history/done_intermediate/testuser stored on the HDFS FileSystem and output the jobtraces in /tmp/job-trace.json along with topology information in /tmp/job-topology.json stored on the local FileSystem.

### Folder

#### Command
    
    
    hadoop rumenfolder [options] [input] [output]
    

This command invokes the Folder utility of Rumen. Folding essentially means that the output duration of the resulting trace is fixed and job timelines are adjusted to respect the final output duration.

> Input and output to Folder is expected to be a fully qualified FileSystem path. So use file:// to specify files on the local FileSystem and hdfs:// to specify files on HDFS.

#### Options

Parameter |  Description |  Notes   
---|---|---  
-input-cycle | Defines the basic unit of time for the folding operation. There is no default value for input-cycle. Input cycle must be provided.  | '-input-cycle 10m' implies that the whole trace run will be now sliced at a 10min interval. Basic operations will be done on the 10m chunks. Note that *Rumen* understands various time units like m(min), h(hour), d(days) etc.   
-output-duration | This parameter defines the final runtime of the trace. Default value if 1 hour.  | '-output-duration 30m' implies that the resulting trace will have a max runtime of 30mins. All the jobs in the input trace file will be folded and scaled to fit this window.   
-concentration | Set the concentration of the resulting trace. Default value is 1.  | If the total runtime of the resulting trace is less than the total runtime of the input trace, then the resulting trace would contain lesser number of jobs as compared to the input trace. This essentially means that the output is diluted. To increase the density of jobs, set the concentration to a higher value.  
-debug | Run the Folder in debug mode. By default it is set to false. | In debug mode, the Folder will print additional statements for debugging. Also the intermediate files generated in the scratch directory will not be cleaned up.   
-seed | Initial seed to the Random Number Generator. By default, a Random Number Generator is used to generate a seed and the seed value is reported back to the user for future use.  | If an initial seed is passed, then the Random Number Generator will generate the random numbers in the same sequence i.e the sequence of random numbers remains same if the same seed is used. Folder uses Random Number Generator to decide whether or not to emit the job.   
-temp-directory | Temporary directory for the Folder. By default the output folder's parent directory is used as the scratch space.  | This is the scratch space used by Folder. All the temporary files are cleaned up in the end unless the Folder is run in debug mode.  
-skew-buffer-length | Enables Folder to tolerate skewed jobs. The default buffer length is 0. | '-skew-buffer-length 100' indicates that if the jobs appear out of order within a window size of 100, then they will be emitted in-order by the folder. If a job appears out-of-order outside this window, then the Folder will bail out provided -allow-missorting is not set. Folder reports the maximum skew size seen in the input trace for future use.   
-allow-missorting | Enables Folder to tolerate out-of-order jobs. By default mis-sorting is not allowed.  | If mis-sorting is allowed, then the Folder will ignore out-of-order jobs that cannot be deskewed using a skew buffer of size specified using -skew-buffer-length. If mis-sorting is not allowed, then the Folder will bail out if the skew buffer is incapable of tolerating the skew.   
  
#### Examples

##### Folding an input trace with 10 hours of total runtime to generate an output trace with 1 hour of total runtime
    
    
    hadoop rumenfolder \
      -output-duration 1h \
      -input-cycle 20m \
      file:///tmp/job-trace.json \
      file:///tmp/job-trace-1hr.json
    

If the folded jobs are out of order then the command will bail out.

##### Folding an input trace with 10 hours of total runtime to generate an output trace with 1 hour of total runtime and tolerate some skewness
    
    
    hadoop rumenfolder \
      -output-duration 1h \
      -input-cycle 20m \
      -allow-missorting \
      -skew-buffer-length 100 \
      file:///tmp/job-trace.json \
      file:///tmp/job-trace-1hr.json
    

If the folded jobs are out of order, then atmost 100 jobs will be de-skewed. If the 101st job is out-of-order, then the command will bail out.

##### Folding an input trace with 10 hours of total runtime to generate an output trace with 1 hour of total runtime in debug mode
    
    
    hadoop rumenfolder \
      -output-duration 1h \
      -input-cycle 20m \
      -debug -temp-directory file:///tmp/debug \
      file:///tmp/job-trace.json \
      file:///tmp/job-trace-1hr.json
    

This will fold the 10hr job-trace file file:///tmp/job-trace.json to finish within 1hr and use file:///tmp/debug as the temporary directory. The intermediate files in the temporary directory will not be cleaned up.

##### Folding an input trace with 10 hours of total runtime to generate an output trace with 1 hour of total runtime with custom concentration.
    
    
    hadoop rumenfolder \
      -output-duration 1h \
      -input-cycle 20m \
      -concentration 2 \
      file:///tmp/job-trace.json \
      file:///tmp/job-trace-1hr.json
    

This will fold the 10hr job-trace file file:///tmp/job-trace.json to finish within 1hr with concentration of 2. If the 10h job-trace is folded to 1h, it retains 10% of the jobs by default. With concentration as 2, 20% of the total input jobs will be retained.

## Appendix

### Resources

[MAPREDUCE-751](https://issues.apache.org/jira/browse/MAPREDUCE-751) is the main JIRA that introduced Rumen to MapReduce. Look at the MapReduce [rumen-component](https://issues.apache.org/jira/browse/MAPREDUCE/component/12313617) for further details.
