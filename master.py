import os
import subprocess

def hdfs():
    return 0

def core():
    return 0

def sethostname():
    print ("""
    Setting Up Hostname as (X.master.com)
    Enter Machine name (X):
    """)
    x = input()
    os.system('hostnameclt set-hostname {}.master.com'.format(x))
    print("Hostname Set as : {}".format(os.system('hostname')))
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