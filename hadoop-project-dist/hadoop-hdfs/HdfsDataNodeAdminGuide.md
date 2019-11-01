

# HDFS DataNode Admin Guide

## Overview

The Hadoop Distributed File System (HDFS) namenode maintains states of all datanodes. There are two types of states. The fist type describes the liveness of a datanode indicating if the node is live, dead or stale. The second type describes the admin state indicating if the node is in service, decommissioned or under maintenance.

When an administrator decommission a datanode, the datanode will first be transitioned into DECOMMISSION_INPROGRESS state. After all blocks belonging to that datanode have been fully replicated elsewhere based on each block’s replication factor. the datanode will be transitioned to DECOMMISSIONED state. After that, the administrator can shutdown the node to perform long-term repair and maintenance that could take days or weeks. After the machine has been repaired, the machine can be recommissioned back to the cluster.

Sometimes administrators only need to take datanodes down for minutes/hours to perform short-term repair/maintenance. In such scenario, the HDFS block replication overhead incurred by decommission might not be necessary and a light-weight process is desirable. And that is what maintenance state is used for. When an administrator put a datanode in maintenance state, the datanode will first be transitioned to ENTERING_MAINTENANCE state. As long as all blocks belonging to that datanode is minimally replicated elsewhere, the datanode will immediately be transitioned to IN_MAINTENANCE state. After the maintenance has completed, the administrator can take the datanode out of the maintenance state. In addition, maintenance state supports timeout that allows administrators to config the maximum duration in which a datanode is allowed to stay in maintenance state. After the timeout, the datanode will be transitioned out of maintenance state automatically by HDFS without human intervention.

In summary, datanode admin operations include the followings:

### Hostname-only configuration

This is the default configuration used by the namenode. It only supports node decommission and recommission; it doesn’t support admin operations related to maintenance state. Use dfs.hosts and dfs.hosts.exclude as explained in [hdfs-default.xml](./hdfs-default.xml).

In the following example, host1 and host2 need to be in service. host3 and host4 need to be in decommissioned state.

dfs.hosts file
    
    
    host1
    host2
    host3
    host4
    

dfs.hosts.exclude file
    
    
    host3
    host4
    

### JSON-based configuration

JSON-based format is the new configuration format that supports generic properties on datanodes. Set the following configurations to enable JSON-based format as explained in [hdfs-default.xml](./hdfs-default.xml).

Setting  |  Value   
---|---  
dfs.namenode.hosts.provider.classname |  org.apache.hadoop.hdfs.server.blockmanagement.CombinedHostFileManager  
dfs.hosts |  the path of the json hosts file   
  
Here is the list of currently supported properties by HDFS.

Property  |  Description   
---|---  
hostName |  Required. The host name of the datanode.   
upgradeDomain |  Optional. The upgrade domain id of the datanode.   
adminState |  Optional. The expected admin state. The default value is NORMAL; DECOMMISSIONED for decommission; IN_MAINTENANCE for maintenance state.   
port |  Optional. the port number of the datanode   
maintenanceExpireTimeInMS |  Optional. The epoch time in milliseconds until which the datanode will remain in maintenance state. The default value is forever.   
  
In the following example, host1 and host2 need to in service. host3 need to be in decommissioned state. host4 need to be in in maintenance state.

dfs.hosts file
    
    
    [
      {
        "hostName": "host1"
      },
      {
        "hostName": "host2",
        "upgradeDomain": "ud0"
      },
      {
        "hostName": "host3",
        "adminState": "DECOMMISSIONED"
      },
      {
        "hostName": "host4",
        "upgradeDomain": "ud2",
        "adminState": "IN_MAINTENANCE"
      }
    ]
    

## Cluster-level settings

There are several cluster-level settings related to datanode administration. For common use cases, you should rely on the default values. Please refer to [hdfs-default.xml](./hdfs-default.xml) for descriptions and default values.
    
    
    dfs.namenode.maintenance.replication.min
    dfs.namenode.decommission.interval
    dfs.namenode.decommission.blocks.per.interval
    dfs.namenode.decommission.max.concurrent.tracked.nodes
    

## Metrics

Admin states are part of the namenode’s webUI and JMX. As explained in [HDFSCommands.html](./HDFSCommands.html), you can also verify admin states using the following commands.

Use dfsadmin to check admin states at the cluster level.

hdfs dfsadmin -report

Use fsck to check admin states of datanodes storing data at a specific path. For backward compatibility, a special flag is required to return maintenance states.
    
    
    hdfs fsck <path> // only show decommission state
    hdfs fsck <path> -maintenance // include maintenance state
    
