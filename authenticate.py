import os
import subprocess

def checkIP(x):

	print("\nSTATUS:")
	print("--------")

	k = subprocess.getstatusoutput("ping -c 2 {}".format(x))
	if k[0]==0 :
		os.system('tput setaf 2')
		print("{} Connected".format(x))
		os.system('tput setaf 7')
		return True
	else:
		os.system('tput setaf 1')
		print("{} Not Connected".format(x))
		os.system('tput setaf 7')
		return False
	

def copyKeygen(x):
	print("Connecting via SSH to {}".format(x))
	k = subprocess.getstatusoutput("ssh-copy-id {}".format(x))
	if k[0] == 0:
		os.system('tput setaf 2')
		print("Connected to {}".format(x))
		os.system('tput setaf 7')
		return True
	else:
		os.system('tput setaf 1')
		print("\nNo SSH Key Found!")
		print("Generating SSH Key...\n")
		os.system('tput setaf 7')

		os.system('ssh-keygen -f id_rsa -t rsa -N ""')
		newK = subprocess.getstatusoutput("ssh-copy-id {}".format(x))
		if newK[0]==0:
			os.system('tput setaf 2')
			print("Connected to {}".format(x))
			os.system('tput setaf 7')
			return True
		else:
			return False

def getssh(x):
	c = copyKeygen(x)
	if c==True:
		return True
	else:
		return False
