import os
import subprocess
import authenticate

print("\t\t\tWelcome to Hadoop Setup Tool")
print("\t\t\t----------------------------")

print("""
	First we need to set Authentication

	Authentication Setup Started...
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

print("Enter IP of the machine to set up: ", end=' ')
thisip = input()

print("""
		This Machine will be used as?
		1. NameNode (Master Node)
		2. DataNode (SlaveNode)
		3. Client
	 """)

print("\n[M-Master/D-Slave/C-Client]? ", end=' ')
machine = input()

if machine == 'M':
	print("A")
elif machine == 'D':
	print("A")
elif machine == 'C':
	print("A")
else:
	os.system('tput setaf 1')
	print("Invalid Choice! Retry")
	os.system('tput setaf 7')