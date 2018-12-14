import os
import subprocess


def hdfs():
    hdfsFile = open("/etc/hadoop/hdfs-site.xml", "a")
    hdfsFile.seek()

def core():
    return 0

def sethostname(ip):
    print ("Enter Desired Hostname (ex. X.slave.com): ", end=' ')
    x = input()
    os.system('ssh {} hostnameclt set-hostname {}'.format(ip, x))
    print("Hostname Set as : {}".format(os.system('ssh {} hostname'.format(ip))))    

def makeNameDir(ip):
    os.system('ssh {} mkdir /data'.format(ip))

def start(ip):
    os.system("ssh {} iptables -F".format(ip))
    x = subprocess.getstatusoutput("ssh {} hadoop-daemon.sh start datanode".format(ip))
    if x[0] == 0:
        os.system('ssh {} tput setaf 2'.format(ip))
        print("Data Node Started")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system('ssh {} jps'.format(ip))
    else:
        os.system('ssh {} tput setaf 1'.format(ip))
        print("ALERT: Data Node Failed to Start!")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system('ssh {} jps'.format(ip))

def stop(ip):
    x = subprocess.getstatusoutput("ssh {} hadoop-daemon.sh stop datanode".format(ip))
    if x[0] == 0:
        os.system('ssh {} tput setaf 2'.format(ip))
        print("Data Node Stopped")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system('ssh {} jps'.format(ip))
    else:
        os.system('ssh {} tput setaf 1'.format(ip))
        print("ALERT: Data Node Failed to Stop!")
        os.system('ssh {} tput setaf 7'.format(ip)) 
        os.system("ssh {} jps".format(ip))

def report(ip):
    os.system("ssh {} hadoop dfsadmin -report".format(ip))