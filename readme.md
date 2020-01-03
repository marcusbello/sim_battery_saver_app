**Simple Battery Saver App**

This app was developed using python version 3.7.2 programming language, with the
intention of using it to reduce the overall battery usage on a 
windows machine. It is normal that this type of app is best coded with languages like C++ or C, but I decided to use python to make it more challenging and it came through easily with the use of some python modules.

**A module is a Python object with arbitrarily named attributes that you can bind and reference. Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.**
 
 _to use a module, goto pypi.org , search and run the pip install command in your terminal / cmd e.g `pip install psutil` to install the psutil module_
 
This is what makes python great, python has unlimited modules, almost all the modules can found on the official PYPI.ORG website. I'll be talking about some modules in the later part of this documentation. 


How it works:-

1. Get the list of processes running on the cpu that is using more than 0.0% percentage 
above 0.0% .

Used the python psutil module , lets talk about this psutil module a litte.

**PSUTIL MODULE**

   psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. It implements many functionalities offered by classic UNIX command line tools such as ps, top, iotop, lsof, netstat, ifconfig, free and others. psutil currently supports the following platforms:

Linux
**Windows**
macOS
FreeBSD, OpenBSD, NetBSD
Sun Solaris
AIX**


_…works for both 32-bit and 64-bit architectures. Supported Python versions are 2.6, 2.7 and 3.4+. PyPy is also known to work._

Inside the main.py script, I used this module to create a function that returns the list of running process running with above 0.0% cpu usage. 



2. Selected processes will be closed when the app user clicks the 
run button.

_With the help of the os module , I used os.system() to call a taskkill on all the selected processes pid._

3. Lastly, the app also reduces the screen brightness to 20% 
immediately you click the run button.

_tweaked the brightness with WMI , learn more about wmi module here https://pypi.org/project/WMI/_



The GUI was designed using pyqt5 and to run this script , clone and 
run the `battery_saver.py` file.


