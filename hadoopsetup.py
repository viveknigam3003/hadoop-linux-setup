import os
import subprocess
import authenticate
import localmaster
import localslave
import remotemaster
import remoteslave

#SETTING PARAMETER MODULES AS EXECUTABLES
os.system('cd /root/Desktop/hadoop-linux-setup/')
os.system('chmod +x sethdfsmaster.py')
os.system('chmod +x sethdfsslave.py')
os.system('chmod +x setcoreparam.py')

print("\t\t\tWelcome to Hadoop Setup Tool")
print("\t\t\t----------------------------")

print("""
1. Setup HADOOP HDFS Cluster
2. Start NameNode (Master)
3. Start Data Node
4. Upload Files (for Client Machines)
5. List of all files (for Client Machines)
6. EXIT
""")

print("Enter Choice: ", end=' ')
option = input()

if option == '1':
	print("Enter IP of the machine to set up: ", end=' ')
	thisip = input()
	localip = subprocess.getoutput("ifconfig enp0s3 | grep -w inet | awk '{ print $2}'")

	if thisip != localip:
		print("\nThe current machine IP is: {}".format(localip))
		print("Do you wish to setup Hadoop remotely on {} ? [y/n]: ".format(thisip), end=' ')
		rem = input()

		#ACCEPTED FOR REMOTE SETUP
		if rem == "y":
			print("Setting up {} remotely.".format(thisip))
			print("First we need to authenticate the IP")
			print("Authentication Process Started")

			connect = authenticate.checkIP(thisip)

			if connect == True:
				auth = authenticate.getssh(thisip)
			else:
				exit()

			if auth == True:
				os.system('tput setaf 2')
				print("Authentication is complete!")
				os.system('tput setaf 7')
			else:
				os.system('tput setaf 1')
				print("Authentication Failed!")
				os.system('tput setaf 7')

			print("""
					REMOTE MACHINE SETUP
					--------------------
					This Machine will be used as?
					1. NameNode (Master Node)
					2. DataNode (SlaveNode)
					3. Client
					4. Abort Setup
				""")

			print("\nEnter Choice: ? ", end=' ')
			machine = input()

			if machine == '1':
				os.system('ssh {} sethdfsmaster.py'.format(thisip))
				remotemaster.makeNameDir(thisip)
				os.system('ssh {} setcoreparam.py'.format(thisip))
				remotemaster.formatMaster(thisip)
				remotemaster.sethostname(thisip)
				os.system('tput setaf 2')
				print("Master Node Initialized Successfully!")
				os.system('tput setaf 7')

			elif machine == '2':
				os.system('ssh {} sethdfsslave.py'.format(thisip))
				remoteslave.makeDataDir(thisip)
				os.system('ssh {} setcoreparam.py'.format(thisip))
				remoteslave.sethostname(thisip)
				os.system('tput setaf 2')
				print("Data Node Initialized Successfully!")
				os.system('tput setaf 7')	

			elif machine == '3':
				os.system('setcoreparam.py')

			elif machine == '4':
				exit()

			else:
				os.system('tput setaf 1')
				print("Invalid Choice! Retry")
				os.system('tput setaf 7')

		else:
			exit()

	#PROCEEDING WITH LOCAL SETUP
	else:
		print("""

			LOCAL MACHINE SETUP
			-----------
			This Machine will be used as?
			1. NameNode (Master Node)
			2. DataNode (SlaveNode)
			3. Client
			4. Abort Setup
		""")

		print("\nEnter Choice: ? ", end=' ')
		machine = input()

		if machine == '1':
			os.system('sethdfsmaster.py')
			localmaster.makeNameDir()
			os.system('setcoreparam.py')
			localmaster.formatMaster()
			localmaster.sethostname()
			os.system('tput setaf 2')
			print("Master Node Initialized Successfully!")
			os.system('tput setaf 7')

		elif machine == '2':
			os.system('sethdfsslave.py')
			localslave.makeDataDir()
			os.system('setcoreparam.py')
			localslave.sethostname()
			os.system('tput setaf 2')
			print("Data Node Initialized Successfully!")
			os.system('tput setaf 7')	

		elif machine == '3':
			os.system('setcoreparam.py')

		elif machine == '4':
			exit()

		else:
			os.system('tput setaf 1')
			print("Invalid Choice! Retry")
			os.system('tput setaf 7')
elif option == '2':
	print("""1. Local
	2. Remote""")
	lr = input()
	if lr == '1':
		localmaster.start()
	else:
		print("Enter Remote Master IP: ", end =' ')
		ip_mas = input() 
		remotemaster.start(ip_mas)

elif option == '3':
	print("""1. Local
	2. Remote""")
	lr = input()
	if lr == '1':
		localslave.start()
	else:
		print("Enter Remote DataNode IP: ", end =' ')
		ip_mas = input() 
		remoteslave.start(ip_mas)

elif option == '4':
	print("Enter File Path: ", end=' ')
	path = input()
	os.system('hadoop fs -put {} /'.format(path))

elif option == '5':
	os.system('hadoop fs -ls /')

elif option == '6':
	exit()

else:
	os.system('tput setaf 1')
	print("Invalid Choice! Retry")
	os.system('tput setaf 7')
