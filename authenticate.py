import subprocess
import os

def checkIP():
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
			os.system('tput setaf 7')
		else:
			os.system('tput setaf 1')
			print("{} Not Connected".format(i))
			os.system('tput setaf 7')

def copyKeygen(x):
	print("Connecting via SSH to {}".format(x))
	subprocess.getstatusoutput("ssh-copy-id {}".format(x))
	if x[0] == 0:
		os.system('tput setaf 2')
		print("Connected to {}".format(x))
		os.system('tput setaf 7')
	else:
		os.system('tput setaf 1')
		print("No SSH Key Found!")
		print("Generating SSH Key...\n")
		os.system('tput setaf 7')

		os.system('ssh-keygen -f id_rsa -t rsa -N ""')
		subprocess.getstatusoutput("ssh-copy-id {}".format(x))

def getssh():


