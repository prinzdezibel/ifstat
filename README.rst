ifstat
======

Display simple throughput statistics for network interface controllers.
Requires Linux kernel >= 2.6

Output can be viewed in terminal. Additionally you’ll find the output in
a file suitable for parsing from within your application. The program
can be executed as daemon to provide you reliable network throughput
numbers at any given time.

Example output
--------------

::

    eth0 thruput [bytes/s]                      total               1s               5s              15s  
    Receiving                                 1982418              416              416              412  
    Transmitting                              4029588             1296             1296             1287 

Installation
------------

Method 1: Packaged installation

::

    $ # make sure easy_install it there (debian): 
    $ sudo apt-get install python-setuptools
    $ sudo easy_install ifstat  

Method 2: Source installation

::

    $ git clone https://github.com/prinzdezibel/ifstat  
    $ cd ifstat  
    $ python setup.py develop  

Run program
-----------

::

    $ ifstat --help

File based program output
-------------------------

Start program as foreground or daemon process. Throughput numbers will
be written to a file periodically:

::

    $ cat /var/lib/ifstat/thruput.txt

Parse this file to retrieve relevant data for your application.
