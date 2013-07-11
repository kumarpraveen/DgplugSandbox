----------
Assignment
----------

Execute the mount command in your system. Check the output. You have
to write a python script using functions and file operation to get
exact output.

Sample File Content
~~~~~~~~~~~~~~~~~~~

::

    rootfs / rootfs rw 0 0
    proc /proc proc rw,nosuid,nodev,noexec,relatime 0 0
    sysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0
    devtmpfs /dev devtmpfs rw,nosuid,size=977140k,nr_inodes=244285,mode=755 0 0

Sample Output
~~~~~~~~~~~~~

::

    proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
    sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
    devtmpfs on /dev type devtmpfs (rw,nosuid,size=977140k,nr_inodes=244285,mode=755)

Solution
~~~~~~~~

.. code:: python
   :number-lines:

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
