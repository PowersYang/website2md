# Apache Hadoop 3.2.1

Apache Hadoop 3.2.1 incorporates a number of significant enhancements over the previous major release line (hadoop-3.2).

This release is generally available (GA), meaning that it represents a point of API stability and quality that we consider production-ready.

# Overview

Users are encouraged to read the full set of release notes. This page provides an overview of the major changes.

## Node Attributes Support in YARN

Node Attributes helps to tag multiple labels on the nodes based on its attributes and supports placing the containers based on expression of these labels.

More details are available in the [Node Attributes](./hadoop-yarn/hadoop-yarn-site/NodeAttributes.html) documentation.

## Hadoop Submarine on YARN

Hadoop Submarine enables data engineers to easily develop, train and deploy deep learning models (in TensorFlow) on very same Hadoop YARN cluster where data resides.

More details are available in the [Hadoop Submarine](./hadoop-yarn/hadoop-yarn-applications/hadoop-yarn-submarine/Index.html) documentation.

## Storage Policy Satisfier

Supports HDFS (Hadoop Distributed File System) applications to move the blocks between storage types as they set the storage policies on files/directories.

More details are available in the [Storage Policy Satisfier](./hadoop-project-dist/hadoop-hdfs/ArchivalStorage.html) documentation.

## ABFS Filesystem connector

Supports the latest Azure Datalake Gen2 Storage.

## Enhanced S3A connector

Support of an enhanced S3A connector, including better resilience to throttled AWS S3 and DynamoDB IO.

## Upgrades for YARN long running services

Supports in-place seamless upgrades of long running containers via YARN Native Service API and CLI.

More details are available in the [YARN Service Upgrade](./hadoop-yarn/hadoop-yarn-site/yarn-service/ServiceUpgrade.html) documentation.

# Getting Started

The Hadoop documentation includes the information you need to get started using Hadoop. Begin with the [Single Node Setup](./hadoop-project-dist/hadoop-common/SingleCluster.html) which shows you how to set up a single-node Hadoop installation. Then move on to the [Cluster Setup](./hadoop-project-dist/hadoop-common/ClusterSetup.html) to learn how to set up a multi-node Hadoop installation.
