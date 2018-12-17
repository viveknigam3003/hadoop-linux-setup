import os
import subprocess

def sethostname(ip):
    print ("Enter Desired Hostname (ex. X.slave.com): ", end=' ')
    x = input()
    os.system('ssh {} hostnamectl set-hostname {}'.format(ip, x))
    print("Hostname Set as : ", end=' ')
    os.system('ssh {} hostname'.format(ip))    

def makeDataDir(ip):
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

def report(ip):
    os.system("ssh {} hadoop dfsadmin -report".format(ip))