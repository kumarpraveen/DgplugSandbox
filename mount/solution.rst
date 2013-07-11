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
