#!/usr/bin/env/python
import sys

def mountFileRead():
""" This function will read content
	from mounts file and handle exception
	if file is not present.
"""
	try:
		fileObject = open("/proc/mounts")
		for line in fileObject:
			# mount output doesn't contain rootfs details
			# so we have to ignore it
			if "rootfs" in line:
				continue
			else:
				manipulateOutput(line)
		fileObject.close()
	except IOError:
		print "file doesn't exist"

def manipulateOutput(line):
"""
	This funtion will read line content 
	and manipulate it as per desire output.
"""
	 mName, mPath, mType, mInfo, _, _  = line.split(" ")
	 print mName + " on " + mPath + " type " + mType + " (" + mInfo +")"

if __name__ == "__main__":
	mountFileRead()
	sys.exit(0)
