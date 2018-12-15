import os
import subprocess
import xml.etree.ElementTree as ET

def hdfs():
    hdfsfile = ET.parse('/etc/hadoop/hdfs-site.xml')
    root = hdfsfile.getroot()
    a = ET.SubElement(root, "property")
    b = ET.SubElement(a, "name")
    b.text = "dfs.data.dir"
    c = ET.SubElement(a, "value")
    c.text = "/data"
    tree = ET.ElementTree(root)
    tree.write('/etc/hadoop/hdfs-site.xml')

def core():
    print("Enter Master Hostname: ", end=' ')
    host = input()

    corefile = ET.parse('/etc/hadoop/core-site.xml')
    root = corefile.getroot()
    a = ET.SubElement(root, "property")
    b = ET.SubElement(a, "name")
    b.text = "fs.default.name"
    c = ET.SubElement(a, "value")
    c.text = "hdfs://{}:9001".format(host)
    tree = ET.ElementTree(root)
    tree.write('/etc/hadoop/core-site.xml')

def sethostname():
    print ("Enter Desired Hostname (ex. X.slave.com): ", end=' ')
    x = input()
    os.system('hostnameclt set-hostname {}'.format(x))
    print("Hostname Set as : {}".format(os.system('hostname')))
    os.system('hostname')    

def makeDataDir():
    os.system('mkdir /data')

def start():
    os.system("iptables -F")
    x = subprocess.getstatusoutput("hadoop-daemon.sh start datanode")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Data Node Started")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Data Node Failed to Start!")
        os.system('tput setaf 7') 
        os.system('jps')

def stop():
    x = subprocess.getstatusoutput("hadoop-daemon.sh stop datanode")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Data Node Stopped")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Data Node Failed to Stop!")
        os.system('tput setaf 7') 
        os.system('jps')

def report():
    os.system("hadoop dfsadmin -report")