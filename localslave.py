import os
import subprocess

def sethostname():
    print ("Enter Desired Hostname (ex. X.slave.com): ", end=' ')
    x = input()
    os.system('hostnamectl set-hostname {}'.format(x))
    print("Hostname Set as : ", end=' ')
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
        o1 = subprocess.getstatusoutput("jps | grep Datanode")
        if o1[0] == '0':
            print("Jps Running Successfully")
        else:
            subprocess.getstatusoutput("hadoop-daemon.sh start datanode")

    else:
        os.system('tput setaf 1')
        print("ALERT: Data Node Failed to Start!")
        os.system('tput setaf 7') 

def stop():
    x = subprocess.getstatusoutput("hadoop-daemon.sh stop datanode")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Data Node Stopped")
        os.system('tput setaf 7') 
        o1 = subprocess.getstatusoutput("jps | grep Datanode")
        if o1[0] == '0':
            print("Jps Running Successfully")
        else:
            subprocess.getstatusoutput("hadoop-daemon.sh start datanode")
    else:
        os.system('tput setaf 1')
        print("ALERT: Data Node Failed to Stop!")
        os.system('tput setaf 7') 

def report():
    os.system("hadoop dfsadmin -report")