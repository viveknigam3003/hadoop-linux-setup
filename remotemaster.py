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

def sethostname(ip):
    print ("Enter Desired Hostname (ex. X.master.com): ", end=' ')
    x = input()
    os.system('ssh {} hostnameclt set-hostname {}'.format(ip, x))
    print("Hostname Set as : {}".format(os.system('ssh {} hostname'.format(ip))))    

def makeNameDir(ip):
    os.system('ssh {} mkdir /name'.format(ip))

def formatMaster(ip):
    x = subprocess.getstatusoutput("ssh {} hadoop namenode -format".format(ip))
    if x[0] == 0:
        os.system('ssh {} tput setaf 2'.format(ip))
        print("Master Node Formatted Successfully!")
        os.system('ssh {} tput setaf 7'.format(ip))
    else:
        os.system('ssh {} tput setaf 1'.format(ip))
        print("ALERT: Master Node Formatting Error!")
        os.system('ssh {} tput setaf 7'.format(ip)) 

def start(ip):
    os.system("ssh {} iptables -F".format(ip))
    x = subprocess.getstatusoutput("ssh {} hadoop-daemon.sh start namenode".format(ip))
    if x[0] == 0:
        os.system('ssh {} tput setaf 2'.format(ip))
        print("Master Node Started")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system('ssh {} jps'.format(ip))
    else:
        os.system('ssh {} tput setaf 1'.format(ip))
        print("ALERT: Master Node Failed to Start!")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system('ssh {} jps'.format(ip))

def stop(ip):
    x = subprocess.getstatusoutput("ssh {} hadoop-daemon.sh stop namenode".format(ip))
    if x[0] == 0:
        os.system('ssh {} tput setaf 2'.format(ip))
        print("Master Node Stopped")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system('ssh {} jps'.format(ip))
    else:
        os.system('ssh {} tput setaf 1'.format(ip))
        print("ALERT: Master Node Failed to Stop!")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system("ssh {} jps".format(ip))

def report(ip):
    os.system("hadoop dfsadmin -report")