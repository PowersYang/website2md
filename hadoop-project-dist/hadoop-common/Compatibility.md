  
  
# Apache Hadoop Compatibility

## Purpose

This document captures the compatibility goals of the Apache Hadoop project. The different types of compatibility between Hadoop releases that affect Hadoop developers, downstream projects, and end-users are enumerated. For each type of compatibility this document will:

#### Protocol Dependencies

The components of Apache Hadoop may have dependencies that include their own protocols, such as Zookeeper, S3, Kerberos, etc. These protocol dependencies SHALL be treated as internal protocols and governed by the same policy.

#### Transports

In addition to compatibility of the protocols themselves, maintaining cross-version communications requires that the transports supported also be stable. The most likely source of transport changes stems from secure transports, such as SSL. Upgrading a service from SSLv2 to SSLv3 may break existing SSLv2 clients. The minimum supported major version of any transports SHOULD NOT increase between minor releases within a major version, though updates because of security issues, license issues, or other reasons MAY occur. When a transport must be updated between minor releases within a major release, where possible the changes SHOULD only change the minor versions of the components without changing the major versions.

Service ports are considered as part of the transport mechanism. Default service port numbers must be kept consistent to prevent breaking clients.

#### Policy

Hadoop wire protocols are defined in .proto (ProtocolBuffers) files. Client-Server and Server-Server protocols SHALL be classified according to the audience and stability classifications noted in their .proto files. In cases where no classifications are present, the protocols SHOULD be assumed to be [Private](./InterfaceClassification.html#Private) and [Stable](./InterfaceClassification.html#Stable).

The following changes to a .proto file SHALL be considered compatible:

  * Add an optional field, with the expectation that the code deals with the field missing due to communication with an older version of the code
  * Add a new rpc/method to the service
  * Add a new optional request to a Message
  * Rename a field
  * Rename a .proto file
  * Change .proto annotations that effect code generation (e.g. name of java package)



The following changes to a .proto file SHALL be considered incompatible:

  * Change an rpc/method name
  * Change an rpc/method parameter type or return type
  * Remove an rpc/method
  * Change the service name
  * Change the name of a Message
  * Modify a field type in an incompatible way (as defined recursively)
  * Change an optional field to required
  * Add or delete a required field
  * Delete an optional field as long as the optional field has reasonable defaults to allow deletions



The following changes to a .proto file SHALL be considered incompatible:

  * Change a field id
  * Reuse an old field that was previously deleted.



Hadoop wire protocols that are not defined via .proto files SHOULD be considered to be [Private](./InterfaceClassification.html#Private) and [Stable](./InterfaceClassification.html#Stable).

In addition to the limitations imposed by being [Stable](./InterfaceClassification.html#Stable), Hadoop’s wire protocols MUST also be forward compatible across minor releases within a major version according to the following:

  * Client-Server compatibility MUST be maintained so as to allow users to continue using older clients even after upgrading the server (cluster) to a later version (or vice versa). For example, a Hadoop 2.1.0 client talking to a Hadoop 2.3.0 cluster.
  * Client-Server compatibility MUST be maintained so as to allow users to upgrade the client before upgrading the server (cluster). For example, a Hadoop 2.4.0 client talking to a Hadoop 2.3.0 cluster. This allows deployment of client-side bug fixes ahead of full cluster upgrades. Note that new cluster features invoked by new client APIs or shell commands will not be usable. YARN applications that attempt to use new APIs (including new fields in data structures) that have not yet been deployed to the cluster can expect link exceptions.
  * Client-Server compatibility MUST be maintained so as to allow upgrading individual components without upgrading others. For example, upgrade HDFS from version 2.1.0 to 2.2.0 without upgrading MapReduce.
  * Server-Server compatibility MUST be maintained so as to allow mixed versions within an active cluster so the cluster may be upgraded without downtime in a rolling fashion.



New transport mechanisms MUST only be introduced with minor or major version changes. Existing transport mechanisms MUST continue to be supported across minor versions within a major version. Default service port numbers SHALL be considered [Stable](./InterfaceClassification.html#Stable).

### REST APIs

REST API compatibility applies to the exposed REST endpoints (URLs) and response data format. Hadoop REST APIs are specifically meant for stable use by clients across releases, even major ones. For purposes of this document, an exposed PEST API is one that is documented in the public documentation. The following is a non-exhaustive list of the exposed REST APIs:

  * [WebHDFS](../hadoop-hdfs/WebHDFS.html)
  * [ResourceManager](../../hadoop-yarn/hadoop-yarn-site/ResourceManagerRest.html)
  * [NodeManager](../../hadoop-yarn/hadoop-yarn-site/NodeManagerRest.html)
  * [MR Application Master](../../hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredAppMasterRest.html)
  * [History Server](../../hadoop-mapreduce-client/hadoop-mapreduce-client-hs/HistoryServerRest.html)
  * [Timeline Server v1 REST API](../../hadoop-yarn/hadoop-yarn-site/TimelineServer.html)
  * [Timeline Service v2 REST API](../../hadoop-yarn/hadoop-yarn-site/TimelineServiceV2.html)



Each API has an API-specific version number. Any incompatible changes MUST increment the API version number.

#### Policy

The exposed Hadoop REST APIs SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving). With respect to API version numbers, the exposed Hadoop REST APIs SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable), i.e. no incompatible changes are allowed to within an API version number. A REST API version must be labeled as deprecated for a full major release before it can be removed.

### Log Output

The Hadoop daemons and CLIs produce log output via Log4j that is intended to aid administrators and developers in understanding and troubleshooting cluster behavior. Log messages are intended for human consumption, though automation use cases are also supported.

#### Policy

All log output SHALL be considered [Public](./InterfaceClassification.html#Public) and [Unstable](./InterfaceClassification.html#Unstable). For log output, an incompatible change is one that renders a parser unable to find or recognize a line of log output.

### Audit Log Output

Several components have audit logging systems that record system information in a machine readable format. Incompatible changes to that data format may break existing automation utilities. For the audit log, an incompatible change is any change that changes the format such that existing parsers no longer can parse the logs.

#### Policy

All audit log output SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). Any change to the data format SHALL be considered an incompatible change.

### Metrics/JMX

While the Metrics API compatibility is governed by Java API compatibility, the Metrics data format exposed by Hadoop MUST be maintained as compatible for consumers of the data, e.g. for automation tasks.

#### Policy

The data format exposed via Metrics SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable).

### File formats & Metadata

User and system level data (including metadata) is stored in files of various formats. Changes to the metadata or the file formats used to store data/metadata can lead to incompatibilities between versions. Each class of file format is addressed below.

#### User-level file formats

Changes to formats that end users use to store their data can prevent them from accessing the data in later releases, and hence are important to be compatible. Examples of these formats include har, war, SequenceFileFormat, etc.

##### Policy

User-level file formats SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). User-lever file format changes SHOULD be made forward compatible across major releases and MUST be made forward compatible within a major release. The developer community SHOULD prefer the creation of a new derivative file format to making incompatible changes to an existing file format. Such new file formats MUST be created as opt-in, meaning that users must be able to continue using the existing compatible format until and unless they explicitly opt in to using the new file format.

#### System-internal data schemas

Hadoop internal data may also be stored in files or other data stores. Changing the schemas of these data stores can lead to incompatibilities.

##### MapReduce

MapReduce uses formats like I-File to store MapReduce-specific data.

###### Policy

All MapReduce-internal file formats, such as I-File format or the job history server’s jhist file format, SHALL be considered [Private](./InterfaceClassification.html#Private) and [Stable](./InterfaceClassification.html#Stable).

##### HDFS Metadata

HDFS persists metadata (the image and edit logs) in a private file format. Incompatible changes to either the format or the metadata prevent subsequent releases from reading older metadata. Incompatible changes must include a process by which existing metadata may be upgraded.

Depending on the degree of incompatibility in the changes, the following potential scenarios can arise:

  * Automatic: The image upgrades automatically, no need for an explicit “upgrade”.
  * Direct: The image is upgradeable, but might require one explicit release “upgrade”.
  * Indirect: The image is upgradeable, but might require upgrading to intermediate release(s) first.
  * Not upgradeable: The image is not upgradeable.



HDFS data nodes store data in a private directory structure. Incompatible changes to the directory structure may prevent older releases from accessing stored data. Incompatible changes must include a process by which existing data directories may be upgraded.

###### Policy

The HDFS metadata format SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Incompatible changes MUST include a process by which existing metadata may be upgraded. The upgrade process SHALL be allowed to require more than one upgrade. The upgrade process MUST allow the cluster metadata to be rolled back to the older version and its older disk format. The rollback MUST restore the original data but is not REQUIRED to restore the updated data. Any incompatible change to the format MUST result in the major version number of the schema being incremented.

The data node directory format SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Incompatible changes MUST include a process by which existing data directories may be upgraded. The upgrade process SHALL be allowed to require more than one upgrade. The upgrade process MUST allow the data directories to be rolled back to the older layout.

##### AWS S3A Guard Metadata

For each operation in the Hadoop S3 client (s3a) that reads or modifies file metadata, a shadow copy of that file metadata is stored in a separate metadata store, which offers HDFS-like consistency for the metadata, and may also provide faster lookups for things like file status or directory listings. S3A guard tables are created with a version marker which indicates compatibility.

###### Policy

The S3A guard metadata schema SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable). Any incompatible change to the schema MUST result in the version number of the schema being incremented.

##### YARN Resource Manager State Store

The YARN resource manager stores information about the cluster state in an external state store for use in fail over and recovery. If the schema used for the state store data does not remain compatible, the resource manager will not be able to recover its state and will fail to start. The state store data schema includes a version number that indicates compatibility.

###### Policy

The YARN resource manager state store data schema SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Any incompatible change to the schema MUST result in the major version number of the schema being incremented. Any compatible change to the schema MUST result in the minor version number being incremented.

##### YARN Node Manager State Store

The YARN node manager stores information about the node state in an external state store for use in recovery. If the schema used for the state store data does not remain compatible, the node manager will not be able to recover its state and will fail to start. The state store data schema includes a version number that indicates compatibility.

###### Policy

The YARN node manager state store data schema SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Any incompatible change to the schema MUST result in the major version number of the schema being incremented. Any compatible change to the schema MUST result in the minor version number being incremented.

##### YARN Federation State Store

The YARN resource manager federation service stores information about the federated clusters, running applications, and routing policies in an external state store for use in replication and recovery. If the schema used for the state store data does not remain compatible, the federation service will fail to initialize. The state store data schema includes a version number that indicates compatibility.

###### Policy

The YARN federation service state store data schema SHALL be considered [Private](./InterfaceClassification.html#Private) and [Evolving](./InterfaceClassification.html#Evolving). Any incompatible change to the schema MUST result in the major version number of the schema being incremented. Any compatible change to the schema MUST result in the minor version number being incremented.

### Command Line Interface (CLI)

The Hadoop command line programs may be used either directly via the system shell or via shell scripts. The CLIs include both the user-facing commands, such as the hdfs command or the yarn command, and the admin-facing commands, such as the scripts used to start and stop daemons. Changing the path of a command, removing or renaming command line options, the order of arguments, or the command return codes and output break compatibility and adversely affect users.

#### Policy

All Hadoop CLI paths, usage, and output SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable) unless documented as experimental and subject to change.

Note that the CLI output SHALL be considered distinct from the log output generated by the Hadoop CLIs. The latter SHALL be governed by the policy on log output. Note also that for CLI output, all changes SHALL be considered incompatible changes.

### Web UI

Web UI, particularly the content and layout of web pages, changes could potentially interfere with attempts to screen scrape the web pages for information. The Hadoop Web UI pages, however, are not meant to be scraped, e.g. for automation purposes. Users are expected to use REST APIs to programmatically access cluster information.

#### Policy

The Hadoop Web UI SHALL be considered [Public](./InterfaceClassification.html#Public) and [Unstable](./InterfaceClassification.html#Unstable).

### Functional Compatibility

Users depend on the behavior of a Hadoop cluster remaining consistent across releases. Changes which cause unexpectedly different behaviors from the cluster can lead to frustration and long adoption cycles. No new configuration should be added which changes the behavior of an existing cluster, assuming the cluster’s configuration files remain unchanged. For any new settings that are defined, care should be taken to ensure that the new setting does not change the behavior of existing clusters.

#### Policy

Changes to existing functionality MUST NOT change the default behavior or the meaning of existing configuration settings between maintenance releases within the same minor version, regardless of whether the changes arise from changes to the system or logic or to internal or external default configuration values.

Changes to existing functionality SHOULD NOT change the default behavior or the meaning of existing configuration settings between minor releases within the same major version, though changes, such as to fix correctness or security issues, may require incompatible behavioral changes. Where possible such behavioral changes SHOULD be off by default.

### Hadoop Configuration Files

Users use Hadoop-defined properties to configure and provide hints to Hadoop and custom properties to pass information to jobs. Users are encouraged to avoid using custom configuration property names that conflict with the namespace of Hadoop-defined properties and should avoid using any prefixes used by Hadoop, e.g. hadoop, io, ipc, fs, net, file, ftp, kfs, ha, file, dfs, mapred, mapreduce, and yarn.

In addition to properties files, Hadoop uses other configuration files to set system behavior, such as the fair scheduler configuration file or the resource profiles configuration file.

#### Policy

Hadoop-defined properties (names and meanings) SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). The units implied by a Hadoop-defined property MUST NOT change, even across major versions. Default values of Hadoop-defined properties SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving).

Hadoop configuration files that are not governed by the above rules about Hadoop-defined properties SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). The definition of an incompatible change depends on the particular configuration file format, but the general rule is that a compatible change will allow a configuration file that was valid before the change to remain valid after the change.

### Log4j Configuration Files

The log output produced by Hadoop daemons and CLIs is governed by a set of configuration files. These files control the minimum level of log message that will be output by the various components of Hadoop, as well as where and how those messages are stored.

#### Policy

All Log4j configurations SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving).

### Directory Structure

Source code, artifacts (source and tests), user logs, configuration files, output, and job history are all stored on disk on either the local file system or HDFS. Changing the directory structure of these user-accessible files can break compatibility, even in cases where the original path is preserved via symbolic links (such as when the path is accessed by a servlet that is configured to not follow symbolic links).

#### Policy

The layout of source code and build artifacts SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable). Within a major version, the developer community SHOULD preserve the overall directory structure, though individual files MAY be added, moved, or deleted with no warning.

The directory structure of configuration files, user logs, and job history SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving).

### Java Classpath

Hadoop provides several client artifacts that applications use to interact with the system. These artifacts typically have their own dependencies on common libraries. In the cases where these dependencies are exposed to end user applications or downstream consumers (i.e. not [shaded](https://stackoverflow.com/questions/13620281/what-is-the-maven-shade-plugin-used-for-and-why-would-you-want-to-relocate-java)) changes to these dependencies can be disruptive. Developers are strongly encouraged to avoid exposing dependencies to clients by using techniques such as [shading](https://stackoverflow.com/questions/13620281/what-is-the-maven-shade-plugin-used-for-and-why-would-you-want-to-relocate-java).

With regard to dependencies, adding a dependency is an incompatible change, whereas removing a dependency is a compatible change.

Some user applications built against Hadoop may add all Hadoop JAR files (including Hadoop’s library dependencies) to the application’s classpath. Adding new dependencies or updating the versions of existing dependencies may interfere with those in applications’ classpaths and hence their correct operation. Users are therefore discouraged from adopting this practice.

#### Policy

The set of dependencies exposed by the Hadoop client artifacts SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). Any dependencies that are not exposed to clients (either because they are shaded or only exist in non-client artifacts) SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable)

### Environment variables

Users and related projects often utilize the environment variables exported by Hadoop (e.g. HADOOP_CONF_DIR). Removing or renaming environment variables can therefore impact end user applications.

#### Policy

The environment variables consumed by Hadoop and the environment variables made accessible to applications through YARN SHALL be considered [Public](./InterfaceClassification.html#Public) and [Evolving](./InterfaceClassification.html#Evolving). The developer community SHOULD limit changes to major releases.

### Build artifacts

Hadoop uses Maven for project management. Changes to the contents of generated artifacts can impact existing user applications.

#### Policy

The contents of Hadoop test artifacts SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable). Test artifacts include all JAR files generated from test source code and all JAR files that include “tests” in the file name.

The Hadoop client artifacts SHALL be considered [Public](./InterfaceClassification.html#Public) and [Stable](./InterfaceClassification.html#Stable). Client artifacts are the following:

  * hadoop-client
  * hadoop-client-api
  * hadoop-client-minicluster
  * hadoop-client-runtime
  * hadoop-hdfs-client
  * hadoop-hdfs-native-client
  * hadoop-mapreduce-client-app
  * hadoop-mapreduce-client-common
  * hadoop-mapreduce-client-core
  * hadoop-mapreduce-client-hs
  * hadoop-mapreduce-client-hs-plugins
  * hadoop-mapreduce-client-jobclient
  * hadoop-mapreduce-client-nativetask
  * hadoop-mapreduce-client-shuffle
  * hadoop-yarn-client



All other build artifacts SHALL be considered [Private](./InterfaceClassification.html#Private) and [Unstable](./InterfaceClassification.html#Unstable).

### Hardware/Software Requirements

To keep up with the latest advances in hardware, operating systems, JVMs, and other software, new Hadoop releases may include features that require newer hardware, operating systems releases, or JVM versions than previous Hadoop releases. For a specific environment, upgrading Hadoop might require upgrading other dependent software components.

#### Policies

  * Hardware 
    * Architecture: Intel and AMD are the processor architectures currently supported by the community. The community has no plans to restrict Hadoop to specific architectures, but MAY have family-specific optimizations. Support for any processor architecture SHOULD NOT be dropped without first being documented as deprecated for a full major release and MUST NOT be dropped without first being deprecated for at least a full minor release.
    * Minimum resources: While there are no guarantees on the minimum resources required by Hadoop daemons, the developer community SHOULD avoid increasing requirements within a minor release.
  * Operating Systems: The community SHOULD maintain the same minimum OS requirements (OS kernel versions) within a minor release. Currently GNU/Linux and Microsoft Windows are the OSes officially supported by the community, while Apache Hadoop is known to work reasonably well on other OSes such as Apple MacOSX, Solaris, etc. Support for any OS SHOULD NOT be dropped without first being documented as deprecated for a full major release and MUST NOT be dropped without first being deprecated for at least a full minor release.
  * The JVM requirements SHALL NOT change across minor releases within the same major release unless the JVM version in question becomes unsupported. The JVM version requirement MAY be different for different operating systems or even operating system releases.
  * File systems supported by Hadoop, e.g. through the FileSystem API, SHOULD not become unsupported between minor releases within a major version unless a migration path to an alternate client implementation is available.



## References

Here are some relevant JIRAs and pages related to the topic:

  * The evolution of this document - [HADOOP-9517](https://issues.apache.org/jira/browse/HADOOP-9517)
  * Binary compatibility for MapReduce end-user applications between hadoop-1.x and hadoop-2.x - [MapReduce Compatibility between hadoop-1.x and hadoop-2.x](../../hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduce_Compatibility_Hadoop1_Hadoop2.html)
  * Annotations for interfaces as per interface classification schedule - [HADOOP-7391](https://issues.apache.org/jira/browse/HADOOP-7391) [Hadoop Interface Classification](./InterfaceClassification.html)
  * Compatibility for Hadoop 1.x releases - [HADOOP-5071](https://issues.apache.org/jira/browse/HADOOP-5071)
  * The [Hadoop Roadmap](http://wiki.apache.org/hadoop/Roadmap) page that captures other release policies


