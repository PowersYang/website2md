

# Hadoop-AWS module: Integration with Amazon Web Services

##  Overview

Apache Hadoop’s hadoop-aws module provides support for AWS integration. applications to easily use this support.

To include the S3A client in Apache Hadoop’s default classpath:

  1. Make sure thatHADOOP_OPTIONAL_TOOLS in hadoop-env.sh includes hadoop-aws in its list of optional modules to add in the classpath.

  2. For client side interaction, you can declare that relevant JARs must be loaded in your ~/.hadooprc file:
    
        hadoop_add_to_classpath_tools hadoop-aws
    




The settings in this file does not propagate to deployed applications, but it will work for local clients such as the hadoop fs command.

##  Introducing the Hadoop S3A client.

Hadoop’s “S3A” client offers high-performance IO against Amazon S3 object store and compatible implementations.

### Other S3 Connectors

There other Hadoop connectors to S3. Only S3A is actively maintained by the Hadoop project itself.

  1. Apache’s Hadoop’s original s3:// client. This is no longer included in Hadoop.
  2. Amazon EMR’s s3:// client. This is from the Amazon EMR team, who actively maintain it.
  3. Apache’s Hadoop’s [s3n: filesystem client](./s3n.html). This connector is no longer available: users must migrate to the newer s3a: client.



##  Getting Started

S3A depends upon two JARs, alongside hadoop-common and its dependencies.

### Buffering upload data on disk fs.s3a.fast.upload.buffer=disk

When fs.s3a.fast.upload.buffer is set to disk, all data is buffered to local hard disks prior to upload. This minimizes the amount of memory consumed, and so eliminates heap size as the limiting factor in queued uploads —exactly as the original “direct to disk” buffering.
    
    
    <property>
      <name>fs.s3a.fast.upload.buffer</name>
      <value>disk</value>
    </property>
    
    <property>
      <name>fs.s3a.buffer.dir</name>
      <value>${hadoop.tmp.dir}/s3a</value>
      <description>Comma separated list of directories that will be used to buffer file
        uploads to.</description>
    </property>
    

This is the default buffer mechanism. The amount of data which can be buffered is limited by the amount of available disk space.

### Buffering upload data in ByteBuffers: fs.s3a.fast.upload.buffer=bytebuffer

When fs.s3a.fast.upload.buffer is set to bytebuffer, all data is buffered in “Direct” ByteBuffers prior to upload. This may be faster than buffering to disk, and, if disk space is small (for example, tiny EC2 VMs), there may not be much disk space to buffer with.

The ByteBuffers are created in the memory of the JVM, but not in the Java Heap itself. The amount of data which can be buffered is limited by the Java runtime, the operating system, and, for YARN applications, the amount of memory requested for each container.

The slower the upload bandwidth to S3, the greater the risk of running out of memory —and so the more care is needed in tuning the upload settings.
    
    
    <property>
      <name>fs.s3a.fast.upload.buffer</name>
      <value>bytebuffer</value>
    </property>
    

### Buffering upload data in byte arrays: fs.s3a.fast.upload.buffer=array

When fs.s3a.fast.upload.buffer is set to array, all data is buffered in byte arrays in the JVM’s heap prior to upload. This may be faster than buffering to disk.

The amount of data which can be buffered is limited by the available size of the JVM heap heap. The slower the write bandwidth to S3, the greater the risk of heap overflows. This risk can be mitigated by tuning the upload settings.
    
    
    <property>
      <name>fs.s3a.fast.upload.buffer</name>
      <value>array</value>
    </property>
    

### Upload Thread Tuning

Both the Array and Byte buffer buffer mechanisms can consume very large amounts of memory, on-heap or off-heap respectively. The disk buffer mechanism does not use much memory up, but will consume hard disk capacity.

If there are many output streams being written to in a single process, the amount of memory or disk used is the multiple of all stream’s active memory/disk use.

Careful tuning may be needed to reduce the risk of running out memory, especially if the data is buffered in memory.

There are a number parameters which can be tuned:

  1. The total number of threads available in the filesystem for data uploads or any other queued filesystem operation. This is set in fs.s3a.threads.max

  2. The number of operations which can be queued for execution:, awaiting a thread: fs.s3a.max.total.tasks

  3. The number of blocks which a single output stream can have active, that is: being uploaded by a thread, or queued in the filesystem thread queue: fs.s3a.fast.upload.active.blocks

  4. How long an idle thread can stay in the thread pool before it is retired: fs.s3a.threads.keepalivetime




When the maximum allowed number of active blocks of a single stream is reached, no more blocks can be uploaded from that stream until one or more of those active blocks’ uploads completes. That is: a write() call which would trigger an upload of a now full datablock, will instead block until there is capacity in the queue.

How does that come together?

  * As the pool of threads set in fs.s3a.threads.max is shared (and intended to be used across all threads), a larger number here can allow for more parallel operations. However, as uploads require network bandwidth, adding more threads does not guarantee speedup.

  * The extra queue of tasks for the thread pool (fs.s3a.max.total.tasks) covers all ongoing background S3A operations (future plans include: parallelized rename operations, asynchronous directory operations).

  * When using memory buffering, a small value of fs.s3a.fast.upload.active.blocks limits the amount of memory which can be consumed per stream.

  * When using disk buffering a larger value of fs.s3a.fast.upload.active.blocks does not consume much memory. But it may result in a large number of blocks to compete with other filesystem operations.




We recommend a low value of fs.s3a.fast.upload.active.blocks; enough to start background upload without overloading other parts of the system, then experiment to see if higher values deliver more throughput —especially from VMs running on EC2.
    
    
    <property>
      <name>fs.s3a.fast.upload.active.blocks</name>
      <value>4</value>
      <description>
        Maximum Number of blocks a single output stream can have
        active (uploading, or queued to the central FileSystem
        instance's pool of queued operations.
    
        This stops a single stream overloading the shared thread pool.
      </description>
    </property>
    
    <property>
      <name>fs.s3a.threads.max</name>
      <value>10</value>
      <description>The total number of threads available in the filesystem for data
        uploads *or any other queued filesystem operation*.</description>
    </property>
    
    <property>
      <name>fs.s3a.max.total.tasks</name>
      <value>5</value>
      <description>The number of operations which can be queued for execution</description>
    </property>
    
    <property>
      <name>fs.s3a.threads.keepalivetime</name>
      <value>60</value>
      <description>Number of seconds a thread can be idle before being
        terminated.</description>
    </property>
    

### Cleaning up after partial Upload Failures

There are two mechanisms for cleaning up after leftover multipart uploads: - Hadoop s3guard CLI commands for listing and deleting uploads by their age. Documented in the [S3Guard](./s3guard.html) section. - The configuration parameter fs.s3a.multipart.purge, covered below.

If a large stream write operation is interrupted, there may be intermediate partitions uploaded to S3 —data which will be billed for.

These charges can be reduced by enabling fs.s3a.multipart.purge, and setting a purge time in seconds, such as 86400 seconds —24 hours. When an S3A FileSystem instance is instantiated with the purge time greater than zero, it will, on startup, delete all outstanding partition requests older than this time.
    
    
    <property>
      <name>fs.s3a.multipart.purge</name>
      <value>true</value>
      <description>True if you want to purge existing multipart uploads that may not have been
         completed/aborted correctly</description>
    </property>
    
    <property>
      <name>fs.s3a.multipart.purge.age</name>
      <value>86400</value>
      <description>Minimum age in seconds of multipart uploads to purge</description>
    </property>
    

If an S3A client is instantiated with fs.s3a.multipart.purge=true, it will delete all out of date uploads in the entire bucket. That is: it will affect all multipart uploads to that bucket, from all applications.

Leaving fs.s3a.multipart.purge to its default, false, means that the client will not make any attempt to reset or change the partition rate.

The best practise for using this option is to disable multipart purges in normal use of S3A, enabling only in manual/scheduled housekeeping operations.

### S3A “fadvise” input policy support

The S3A Filesystem client supports the notion of input policies, similar to that of the Posix fadvise() API call. This tunes the behavior of the S3A client to optimise HTTP GET requests for the different use cases.

See [Improving data input performance through fadvise](./performance.html#fadvise) for the details.

## Metrics

S3A metrics can be monitored through Hadoop’s metrics2 framework. S3A creates its own metrics system called s3a-file-system, and each instance of the client will create its own metrics source, named with a JVM-unique numerical ID.

As a simple example, the following can be added to hadoop-metrics2.properties to write all S3A metrics to a log file every 10 seconds:
    
    
    s3a-file-system.sink.my-metrics-config.class=org.apache.hadoop.metrics2.sink.FileSink
    s3a-file-system.sink.my-metrics-config.filename=/var/log/hadoop-yarn/s3a-metrics.out
    *.period=10
    

Lines in that file will be structured like the following:
    
    
    1511208770680 s3aFileSystem.s3aFileSystem: Context=s3aFileSystem, s3aFileSystemId=892b02bb-7b30-4ffe-80ca-3a9935e1d96e, bucket=bucket,
    Hostname=hostname-1.hadoop.apache.com, files_created=1, files_copied=2, files_copied_bytes=10000, files_deleted=5, fake_directories_deleted=3,
    directories_created=3, directories_deleted=0, ignored_errors=0, op_copy_from_local_file=0, op_exists=0, op_get_file_status=15, op_glob_status=0,
    op_is_directory=0, op_is_file=0, op_list_files=0, op_list_located_status=0, op_list_status=3, op_mkdirs=1, op_rename=2, object_copy_requests=0,
    object_delete_requests=6, object_list_requests=23, object_continue_list_requests=0, object_metadata_requests=46, object_multipart_aborted=0,
    object_put_bytes=0, object_put_requests=4, object_put_requests_completed=4, stream_write_failures=0, stream_write_block_uploads=0,
    stream_write_block_uploads_committed=0, stream_write_block_uploads_aborted=0, stream_write_total_time=0, stream_write_total_data=0,
    s3guard_metadatastore_put_path_request=10, s3guard_metadatastore_initialization=0, object_put_requests_active=0, object_put_bytes_pending=0,
    stream_write_block_uploads_active=0, stream_write_block_uploads_pending=0, stream_write_block_uploads_data_pending=0,
    S3guard_metadatastore_put_path_latencyNumOps=0, S3guard_metadatastore_put_path_latency50thPercentileLatency=0,
    S3guard_metadatastore_put_path_latency75thPercentileLatency=0, S3guard_metadatastore_put_path_latency90thPercentileLatency=0,
    S3guard_metadatastore_put_path_latency95thPercentileLatency=0, S3guard_metadatastore_put_path_latency99thPercentileLatency=0
    

Depending on other configuration, metrics from other systems, contexts, etc. may also get recorded, for example the following:
    
    
    1511208770680 metricssystem.MetricsSystem: Context=metricssystem, Hostname=s3a-metrics-4.gce.cloudera.com, NumActiveSources=1, NumAllSources=1,
    NumActiveSinks=1, NumAllSinks=0, Sink_fileNumOps=2, Sink_fileAvgTime=1.0, Sink_fileDropped=0, Sink_fileQsize=0, SnapshotNumOps=5,
    SnapshotAvgTime=0.0, PublishNumOps=2, PublishAvgTime=0.0, DroppedPubAll=0
    

Note that low-level metrics from the AWS SDK itself are not currently included in these metrics.

##  Other Topics

###  Copying Data with distcp

Hadoop’s distcp tool is often used to copy data between a Hadoop cluster and Amazon S3. See [Copying Data Between a Cluster and Amazon S3](https://hortonworks.github.io/hdp-aws/s3-copy-data/index.html) for details on S3 copying specifically.

The distcp update command tries to do incremental updates of data. It is straightforward to verify when files do not match when they are of different length, but not when they are the same size.

Distcp addresses this by comparing file checksums on the source and destination filesystems, which it tries to do even if the filesystems have incompatible checksum algorithms.

The S3A connector can provide the HTTP etag header to the caller as the checksum of the uploaded file. Doing so will break distcp operations between hdfs and s3a.

For this reason, the etag-as-checksum feature is disabled by default.
    
    
    <property>
      <name>fs.s3a.etag.checksum.enabled</name>
      <value>false</value>
      <description>
        Should calls to getFileChecksum() return the etag value of the remote
        object.
        WARNING: if enabled, distcp operations between HDFS and S3 will fail unless
        -skipcrccheck is set.
      </description>
    </property>
    

If enabled, distcp between two S3 buckets can use the checksum to compare objects. Their checksums should be identical if they were either each uploaded as a single file PUT, or, if in a multipart PUT, in blocks of the same size, as configured by the value fs.s3a.multipart.size.

To disable checksum verification in distcp, use the -skipcrccheck option:
    
    
    hadoop distcp -update -skipcrccheck -numListstatusThreads 40 /user/alice/datasets s3a://alice-backup/datasets
    
