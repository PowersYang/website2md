

# The Hadoop FileSystem API Definition

This is a specification of the Hadoop FileSystem APIs, which models the contents of a filesystem as a set of paths that are either directories, symbolic links, or files.

There is surprisingly little prior art in this area. There are multiple specifications of Unix filesystems as a tree of inodes, but nothing public which defines the notion of “Unix filesystem as a conceptual model for data storage access”.

This specification attempts to do that; to define the Hadoop FileSystem model and APIs so that multiple filesystems can implement the APIs and present a consistent model of their data to applications. It does not attempt to formally specify any of the concurrency behaviors of the filesystems, other than to document the behaviours exhibited by HDFS as these are commonly expected by Hadoop client applications.

  1. [Introduction](introduction.html)
  2. [Notation](notation.html)
  3. [Model](model.html)
  4. [FileSystem class](filesystem.html)
  5. [FSDataInputStream class](fsdatainputstream.html)
  6. [FSDataOutputStreamBuilder class](fsdataoutputstreambuilder.html)
  7. [Testing with the Filesystem specification](testing.html)
  8. [Extending the specification and its tests](extending.html)
  9. [Uploading a file using Multiple Parts](multipartuploader.html)


