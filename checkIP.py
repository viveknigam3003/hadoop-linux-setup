import os
import subprocess

connectedIP = []

print("Enter IP of all Machines Separated with commas(,): ", end=' ')
IPs = input()
IPList = IPs.split(',')

print("\nSTATUS:")
print("--------")

for i in IPList:
    x = subprocess.getstatusoutput("ping -c 2 {}".format(i))
    if x[0]==0 :
        os.system('tput setaf 2')
        print("{} Connected".format(i))
        connectedIP.append(i)
        os.system('tput setaf 7')
    else:
        os.system('tput setaf 1')
        print("{} Not Connected".format(i))
        os.system('tput setaf 7')