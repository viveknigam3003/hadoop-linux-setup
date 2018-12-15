import os
import subprocess
import xml.etree.ElementTree as ET

def hdfs():
    hdfsfile = ET.parse('/etc/hadoop/hdfs-site.xml')
    root = hdfsfile.getroot()
    a = ET.SubElement(root, "property")
    b = ET.SubElement(a, "name")
    b.text = "dfs.name.dir"
    c = ET.SubElement(a, "value")
    c.text = "/name"
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
    print ("Enter Desired Hostname (ex. X.master.com):", end=' ')
    x = input()
    os.system('hostnameclt set-hostname {}'.format(x))
    print("Hostname Set as : {}".format(os.system('hostname')), end=' ')
    os.system('hostname')    

def makeNameDir():
    os.system('mkdir /name')

def formatMaster():
    x = subprocess.getstatusoutput("hadoop namenode -format")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Master Node Formatted Successfully!")
        os.system('tput setaf 7')
    else:
        os.system('tput setaf 1')
        print("ALERT: Master Node Formatting Error!")
        os.system('tput setaf 7') 

def start():
    os.system("iptables -F")
    x = subprocess.getstatusoutput("hadoop-daemon.sh start namenode")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Master Node Started")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Master Node Failed to Start!")
        os.system('tput setaf 7') 
        os.system('jps')

def stop():
    x = subprocess.getstatusoutput("hadoop-daemon.sh stop namenode")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Master Node Stopped")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Master Node Failed to Stop!")
        os.system('tput setaf 7') 
        os.system('jps')

def report():
    os.system("hadoop dfsadmin -report")