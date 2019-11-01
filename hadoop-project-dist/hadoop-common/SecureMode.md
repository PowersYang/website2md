

# Hadoop in Secure Mode

## Introduction

This document describes how to configure authentication for Hadoop in secure mode. When Hadoop is configured to run in secure mode, each Hadoop service and each user must be authenticated by Kerberos.

Forward and reverse host lookup for all service hosts must be configured correctly to allow services to authenticate with each other. Host lookups may be configured using either DNS or /etc/hosts files. Working knowledge of Kerberos and DNS is recommended before attempting to configure Hadoop services in Secure Mode.

Security features of Hadoop consist of Authentication, [Service Level Authorization](./ServiceLevelAuth.html), [Authentication for Web Consoles](./HttpAuthentication.html) and Data Confidentiality.

## Authentication

### End User Accounts

When service level authentication is turned on, end users must authenticate themselves before interacting with Hadoop services. The simplest way is for a user to authenticate interactively using the [Kerberos kinit command](http://web.mit.edu/kerberos/krb5-1.12/doc/user/user_commands/kinit.html "MIT Kerberos Documentation of kinit"). Programmatic authentication using Kerberos keytab files may be used when interactive login with kinit is infeasible.

### User Accounts for Hadoop Daemons

Ensure that HDFS and YARN daemons run as different Unix users, e.g. hdfs and yarn. Also, ensure that the MapReduce JobHistory server runs as different user such as mapred.

It’s recommended to have them share a Unix group, e.g. hadoop. See also “Mapping from user to group” for group management.

User:Group  |  Daemons   
---|---  
hdfs:hadoop  |  NameNode, Secondary NameNode, JournalNode, DataNode   
yarn:hadoop  |  ResourceManager, NodeManager   
mapred:hadoop  |  MapReduce JobHistory Server   
  
### Kerberos principals for Hadoop Daemons

Each Hadoop Service instance must be configured with its Kerberos principal and keytab file location.

The general format of a Service principal is ServiceName/_HOST@REALM.TLD. e.g. dn/_HOST@EXAMPLE.COM.

Hadoop simplifies the deployment of configuration files by allowing the hostname component of the service principal to be specified as the _HOST wildcard. Each service instance will substitute _HOST with its own fully qualified hostname at runtime. This allows administrators to deploy the same set of configuration files on all nodes. However, the keytab files will be different.

#### HDFS

The NameNode keytab file, on each NameNode host, should look like the following:
    
    
    $ klist -e -k -t /etc/security/keytab/nn.service.keytab
    Keytab name: FILE:/etc/security/keytab/nn.service.keytab
    KVNO Timestamp         Principal
       4 07/18/11 21:08:09 nn/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 nn/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 nn/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
    

The Secondary NameNode keytab file, on that host, should look like the following:
    
    
    $ klist -e -k -t /etc/security/keytab/sn.service.keytab
    Keytab name: FILE:/etc/security/keytab/sn.service.keytab
    KVNO Timestamp         Principal
       4 07/18/11 21:08:09 sn/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 sn/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 sn/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
    

The DataNode keytab file, on each host, should look like the following:
    
    
    $ klist -e -k -t /etc/security/keytab/dn.service.keytab
    Keytab name: FILE:/etc/security/keytab/dn.service.keytab
    KVNO Timestamp         Principal
       4 07/18/11 21:08:09 dn/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 dn/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 dn/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
    

#### YARN

The ResourceManager keytab file, on the ResourceManager host, should look like the following:
    
    
    $ klist -e -k -t /etc/security/keytab/rm.service.keytab
    Keytab name: FILE:/etc/security/keytab/rm.service.keytab
    KVNO Timestamp         Principal
       4 07/18/11 21:08:09 rm/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 rm/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 rm/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
    

The NodeManager keytab file, on each host, should look like the following:
    
    
    $ klist -e -k -t /etc/security/keytab/nm.service.keytab
    Keytab name: FILE:/etc/security/keytab/nm.service.keytab
    KVNO Timestamp         Principal
       4 07/18/11 21:08:09 nm/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 nm/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 nm/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
    

#### MapReduce JobHistory Server

The MapReduce JobHistory Server keytab file, on that host, should look like the following:
    
    
    $ klist -e -k -t /etc/security/keytab/jhs.service.keytab
    Keytab name: FILE:/etc/security/keytab/jhs.service.keytab
    KVNO Timestamp         Principal
       4 07/18/11 21:08:09 jhs/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 jhs/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 jhs/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-256 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (AES-128 CTS mode with 96-bit SHA-1 HMAC)
       4 07/18/11 21:08:09 host/full.qualified.domain.name@REALM.TLD (ArcFour with HMAC/md5)
    

### Mapping from Kerberos principals to OS user accounts

Hadoop maps Kerberos principals to OS user (system) accounts using rules specified by hadoop.security.auth_to_local. How Hadoop evaluates these rules is determined by the setting of hadoop.security.auth_to_local.mechanism.

In the default hadoop mode a Kerberos principal must be matched against a rule that transforms the principal to a simple form, i.e. a user account name without ‘@’ or ‘/’, otherwise a principal will not be authorized and a error will be logged. In case of the MIT mode the rules work in the same way as the auth_to_local in [Kerberos configuration file (krb5.conf)](http://web.mit.edu/Kerberos/krb5-latest/doc/admin/conf_files/krb5_conf.html) and the restrictions of hadoop mode do not apply. If you use MIT mode it is suggested to use the same auth_to_local rules that are specified in your /etc/krb5.conf as part of your default realm and keep them in sync. In both hadoop and MIT mode the rules are being applied (with the exception of DEFAULT) to all principals regardless of their specified realm. Also, note you should not rely on the auth_to_local rules as an ACL and use proper (OS) mechanisms.

Possible values for auth_to_local are:

### Usage
    
    
    KDiag: Diagnose Kerberos Problems
      [-D key=value] : Define a configuration option.
      [--jaas] : Require a JAAS file to be defined in java.security.auth.login.config.
      [--keylen <keylen>] : Require a minimum size for encryption keys supported by the JVM. Default value : 256.
      [--keytab <keytab> --principal <principal>] : Login from a keytab as a specific principal.
      [--nofail] : Do not fail on the first problem.
      [--nologin] : Do not attempt to log in.
      [--out <file>] : Write output to a file.
      [--resource <resource>] : Load an XML configuration resource.
      [--secure] : Require the hadoop configuration to be secure.
      [--verifyshortname <principal>]: Verify the short name of the specific principal does not contain '@' or '/'
    

#### \--jaas: Require a JAAS file to be defined in java.security.auth.login.config.

If --jaas is set, the Java system property java.security.auth.login.config must be set to a JAAS file; this file must exist, be a simple file of non-zero bytes, and readable by the current user. More detailed validation is not performed.

JAAS files are not needed by Hadoop itself, but some services (such as Zookeeper) do require them for secure operation.

#### \--keylen <length>: Require a minimum size for encryption keys supported by the JVM".

If the JVM does not support this length, the command will fail.

The default value is to 256, as needed for the AES256 encryption scheme. A JVM without the Java Cryptography Extensions installed does not support such a key length. Kerberos will not work unless configured to use an encryption scheme with a shorter key length.

#### \--keytab <keytab> \--principal <principal>: Log in from a keytab.

Log in from a keytab as the specific principal.

  1. The file must contain the specific principal, including any named host. That is, there is no mapping from _HOST to the current hostname.
  2. KDiag will log out and attempt to log back in again. This catches JVM compatibility problems which have existed in the past. (Hadoop’s Kerberos support requires use of/introspection into JVM-specific classes).



#### \--nofail : Do not fail on the first problem

KDiag will make a best-effort attempt to diagnose all Kerberos problems, rather than stop at the first one.

This is somewhat limited; checks are made in the order which problems surface (e.g keylength is checked first), so an early failure can trigger many more problems. But it does produce a more detailed report.

#### \--nologin: Do not attempt to log in.

Skip trying to log in. This takes precedence over the --keytab option, and also disables trying to log in to kerberos as the current kinited user.

This is useful when the KDiag command is being invoked within an application, as it does not set up Hadoop’s static security state —merely check for some basic Kerberos preconditions.

#### \--out outfile: Write output to file.
    
    
    hadoop kdiag --out out.txt
    

Much of the diagnostics information comes from the JRE (to stderr) and from Log4j (to stdout). To get all the output, it is best to redirect both these output streams to the same file, and omit the --out option.
    
    
    hadoop kdiag --keytab zk.service.keytab --principal zookeeper/devix.example.org@REALM > out.txt 2>&1
    

Even there, the output of the two streams, emitted across multiple threads, can be a bit confusing. It will get easier with practise. Looking at the thread name in the Log4j output to distinguish background threads from the main thread helps at the hadoop level, but doesn’t assist in JVM-level logging.

#### \--resource <resource> : XML configuration resource to load.

To load XML configuration files, this option can be used. As by default, the core-default and core-site XML resources are only loaded. This will help, when additional configuration files has any Kerberos related configurations.
    
    
    hadoop kdiag --resource hbase-default.xml --resource hbase-site.xml
    

For extra logging during the operation, set the logging and HADOOP_JAAS_DEBUG environment variable to the values listed in “Troubleshooting”. The JVM options are automatically set in KDiag.

#### \--secure: Fail if the command is not executed on a secure cluster.

That is: if the authentication mechanism of the cluster is explicitly or implicitly set to “simple”:
    
    
    <property>
      <name>hadoop.security.authentication</name>
      <value>simple</value>
    </property>
    

Needless to say, an application so configured cannot talk to a secure Hadoop cluster.

#### \--verifyshortname <principal>: validate the short name of a principal

This verifies that the short name of a principal contains neither the "@" nor "/" characters.

### Example
    
    
    hadoop kdiag \
      --nofail \
      --resource hdfs-site.xml --resource yarn-site.xml \
      --keylen 1024 \
      --keytab zk.service.keytab --principal zookeeper/devix.example.org@REALM
    

This attempts to to perform all diagnostics without failing early, load in the HDFS and YARN XML resources, require a minimum key length of 1024 bytes, and log in as the principal zookeeper/devix.example.org@REALM, whose key must be in the keytab zk.service.keytab

## References

  1. O’Malley O et al. [Hadoop Security Design](https://issues.apache.org/jira/secure/attachment/12428537/security-design.pdf)
  2. O’Malley O, [Hadoop Security Architecture](http://www.slideshare.net/oom65/hadoop-security-architecture)
  3. [Troubleshooting Kerberos on Java 7](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
  4. [Troubleshooting Kerberos on Java 8](http://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
  5. [Java 7 Kerberos Requirements](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
  6. [Java 8 Kerberos Requirements](http://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/Troubleshooting.html)
  7. Loughran S., [Hadoop and Kerberos: The Madness beyond the Gate](https://steveloughran.gitbooks.io/kerberos_and_hadoop/content/)


