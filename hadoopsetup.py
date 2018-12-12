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
