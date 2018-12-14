import os
import subprocess

ip=''
def initialize (init):
    ip = init

def hdfs():
    return 0

def core():
    return 0

def sethostname():
    print ("Enter Desired Hostname (ex. X.master.com): ", end=' ')
    x = input()
    os.system('ssh {} hostnameclt set-hostname {}'.format(ip, x))
    print("Hostname Set as : {}".format(os.system('ssh {} hostname'.format(ip))))    

def makeNameDir():
    os.system('ssh {} mkdir /name'.format(ip))

def formatMaster():
    x = subprocess.getstatusoutput("ssh {} hadoop namenode -format".format(ip))
    if x[0] == 0:
        os.system('ssh {} tput setaf 2'.format(ip))
        print("Master Node Formatted Successfully!")
        os.system('ssh {} tput setaf 7'.format(ip))
    else:
        os.system('ssh {} tput setaf 1'.format(ip))
        print("ALERT: Master Node Formatting Error!")
        os.system('ssh {} tput setaf 7'.format(ip)) 

def start():
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

def stop():
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
        os.system('ssh {} jps'format(ip))

def report():
    os.system("hadoop dfsadmin -report")