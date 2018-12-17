# hadoop-linux-setup
Python scripts to assist setting up Hadoop v1 HDFS in Linux and starting a NameNode, DataNodes and Client.

## INTRODUCTION
A Hadoop v1 cluster consists of a `master` or `namenode`, along with some `slaves` or `datanodes` and a `client` to dictate the storage of data in the *Hadoop Distributed File System*. However setting up Hadoop Cluster in Linux everytime is tedious task which can be easily achieved by this easy to use Hadoop Setup Tool.

## Python3 scripts for HADOOP© v1 HDFS
It uses python scripts to set up a `NameNode`, format it and start it. It configures the all the DataNodes and all the Clients to work collectively in an HDFS. The Main file is `hadoopsetup.py`, the rest are supporting files. To make the tasks easier it also uses `ssh` to gain authorization and all the machines connected have easy access to each other while the setup is being done. `ssh-keygen` command is automated as required.

## Notes
* Clone/Download the repository on your desktop on the local system you want to set up.
* Run the `hadoopsetup.py` from terminal or command line on a Python3 installed Linux System.
* Make sure that Oracle© JAVA is installed and `JAVA_HOME` and `PATH` is set.
* Hadoop v1 should be installed on the system which needs to be set up.

## Changelog
**17.12.18** <br>
* MapReduce Automation Menu Added.
* `MapReduce.py` and `mapredxml.py` files added.
