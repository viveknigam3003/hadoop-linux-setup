import os
import subprocess

os.system('cd /root/Desktop/hadoop-linux-setup/')
os.system('chmod +x mapredxml.py')

print("\t\t\tWelcome to Hadoop Setup Tool")
print("\t\t\t----------------------------")

print("""
1. Setup HADOOP MapReduce Cluster on this machine.
2. Start JobTracker (Master)
3. Start TaskTracker
6. EXIT
""")

print("Enter Choice: ", end=' ')
option = input()

if option == '1':
    os.system('mapredxml.py')

elif option == '2':
    os.system("iptables -F")
    x = subprocess.getstatusoutput("hadoop-daemon.sh start jobtracker")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Job Tracker Started")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Job Tracker Failed to Start!")
        os.system('tput setaf 7') 
        os.system('jps')

elif option == '3':
    os.system("iptables -F")
    x = subprocess.getstatusoutput("hadoop-daemon.sh start tasktracker")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Task Tracker Started")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Task Tracker Failed to Start!")
        os.system('tput setaf 7') 
        os.system('jps')

elif option == '4':
    exit()

else:
    os.system('tput setaf 1')
    print("Invalid Choice! Retry")
    os.system('tput setaf 7')
    exit()
