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

