

# Hadoop: YARN-UI V2

## Prerequisites

Please make sure Hadoop is built by passing -Pyarn-ui to Maven (reference to BUILDING.txt for more details)

## Configurations

In yarn-site.xml

Configuration Property  |  Description   
---|---  
yarn.webapp.ui2.enable  |  (Required) In the server side it indicates whether the new YARN-UI v2 is enabled or not. Defaults to false.   
yarn.webapp.ui2.war-file-path  |  (Optional) WAR file path for launching yarn UI2 web application. By default this is empty and YARN will lookup required war file from classpath   
  
Please note that, If you run YARN daemons locally in your machine for test purpose, you need the following configurations added to yarn-site.xml to enable cross origin (CORS) support.

Configuration Property  |  Value  |  Description   
---|---|---  
yarn.timeline-service.http-cross-origin.enabled  |  true  |  Enable CORS support for Timeline Server   
yarn.resourcemanager.webapp.cross-origin.enabled  |  true  |  Enable CORS support for Resource Manager   
yarn.nodemanager.webapp.cross-origin.enabled  |  true  |  Enable CORS support for Node Manager   
  
Also please ensure that CORS related configurations are enabled in core-site.xml. Kindly refer [here](../../hadoop-project-dist/hadoop-common/HttpAuthentication.html)

## Use it

Open your browser, go to rm-address:8088/ui2 and try it!

## Notes

This UI framework is verified under security environment as well.
