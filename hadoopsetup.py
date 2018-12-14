import os
import subprocess
import authenticate
import master
import slave

print("\t\t\tWelcome to Hadoop Setup Tool")
print("\t\t\t----------------------------")

print("Enter IP of the machine to set up: ", end=' ')
thisip = input()
localip = subprocess.getoutput("ifconfig enp0s3 | grep -w inet | awk '{ print $2}'")
if thisip != localip:
	print("\nThe current machine IP is: {}".format(localip))
	print("Do you wish to setup Hadoop remotely on {} ? [y/n]: ".format(thisip), end=' ')
	rem = input()
	if rem == "n":
		print("\nContinue with current machine? [y/n]: ", end =' ')
		cont = input()
		if cont == 'n':
			exit()

	else:
		print("Setting up {} remotely.".format(thisip))
		print("""
				\nFirst we need to set Authentication
				Authentication Process Started...
			 """)

		authenticate.checkIP()
		print("\nDo You wish to Continue [y/n]?")
		ch = input()

		if ch == 'y':
			authenticate.getssh()
		else:
			exit()

		os.system('tput setaf 2')
		print("Authentication is complete!")
		os.system('tput setaf 7')

print("""
		This Machine will be used as?
		1. NameNode (Master Node)
		2. DataNode (SlaveNode)
		3. Client
		4. Abort Setup
	 """)

print("\nEnter Choice: ? ", end=' ')
machine = input()

if machine == '1':
	master.hdfs()
	master.makeNameDir()
	master.core()
	master.formatMaster()
	master.sethostname()
	os.system('tput setaf 2')
	print("Master Node Initialized Successfully!")
	os.system('tput setaf 7')

elif machine == '2':
	slave.hdfs()
	slave.makeDataDir()
	slave.core()
	slave.sethostname()
	os.system('tput setaf 2')
	print("Data Node Initialized Successfully!")
	os.system('tput setaf 7')	

elif machine == '3':
	print("A")

elif machine == '4':
	exit()

else:
	os.system('tput setaf 1')
	print("Invalid Choice! Retry")
	os.system('tput setaf 7')
