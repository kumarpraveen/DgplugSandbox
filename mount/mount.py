#!/usr/bin/env/python
import sys

def mount_file_read():
	""" This function will read content
	from mounts file and handle exception
	if file is not present.
	"""
	try:
		file_object = open("/proc/mounts")
		for line in file_object:
			# mount output doesn't contain rootfs details
			# so we have to ignore it
			if "rootfs" in line:
				continue
			else:
				manipulate_output(line)
		file_object.close()
	except IOError:
		print "file doesn't exist"

def manipulate_output(line):
	"""
	This funtion will read line content 
	and manipulate it as per desire output.
	"""
	m_name, m_path, m_type, m_info, _, _  = line.split(" ")
	print m_name + " on " + m_path + " type " + m_type + " (" + m_info +")"

if __name__ == "__main__":
	mount_file_read()
	sys.exit(0)
