

# YARN Service Registry

The Service registry is a service which can be deployed in a Hadoop cluster to allow deployed applications to register themselves and the means of communicating with them. Client applications can then locate services and use the binding information to connect with the services’s network-accessible endpoints, be they REST, IPC, Web UI, Zookeeper quorum+path or some other protocol. Currently, all the registry data is stored in a zookeeper cluster.

  * [Architecture](yarn-registry.html)
  * [Configuration](registry-configuration.html)
  * [Using the YARN Service registry](using-the-yarn-service-registry.html)
  * [Security](registry-security.html)


