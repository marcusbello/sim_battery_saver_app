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

Windows

macOS

FreeBSD, OpenBSD, NetBSD

Sun Solaris

AIX**


_…works for both 32-bit and 64-bit architectures. Supported Python versions are 2.6, 2.7 and 3.4+. PyPy is also known to work._

Inside the main.py script, I used this module to create a function that returns the list of running process running with above 0.0% cpu usage. 

Read more about psutil >> http://psutil.readthedocs.io/ .

2. Selected processes will be closed when the app user clicks the 
run button.
  
  When a process is running on a machine, it has a unique number called pid i.e process identification number, this pid can be used to
to manage a process, since this is a windows app, using windows command prompt or powershell, if you know a process pid, you can close it by running this command `taskkill /f /t /pid <replace with the pid you want>` this will close the process using the specified pid. The /f means to force kill and /t means to kill all threads, you can decide to remove any of the options this. So, I integrated this command in the app using python powerful OS module.

**OS Module**

  OS module is a very big module, because you can use it for a large variety of stuffs and works almost the same 
  on all types of OS, e.g windows, mac, linux etc. its the official module used to communicate directly with the OS of any machine. 
  While working with this OS module, I used os.system() to run the taskkill command, as what the os.system() does is 
  that, it will run any argument you put there like you're running it inside a commandline. 
    
This snippet was included in the class MyForm() running the user interface, see the kill_pid() function inside the `battery_saver.py` to get a hang of how I used the this os.system() to call a taskkill on all the selected processes.


3. Lastly, the app also reduces the screen brightness to 20% 
immediately you click the run button.

I was able to tweak the brightness with the use of WMI Module, but what is WMI ?

Windows Management Instrumentation (WMI) is Microsoft’s implementation of Web-Based Enterprise Management (WBEM), an industry initiative to provide a Common Information Model (CIM) for pretty much any information about a computer system.

But talking about the Python WMI module, it's a lightweight wrapper on top of the pywin32 extensions, and hides some of the messy plumbing needed to get Python to talk to the WMI API. It’s pure Python and should work with any version of Python from 2.1 onwards (list comprehensions) and any recent version of pywin32.

I used this module to reduce the screen brightness, since the app was for windows, I can easily use the WMI API to control the screen brightness, the function called in the reduce_brigtness() in the MyForm() class handles this, check battery_saver.py  


Learn more about wmi module here https://pypi.org/project/WMI/_



**Let's talk about the GUI**  

It's a simple GUI, designed with PyQt5, named finalbat.py, the finalbat.py was included in the battery_saver.py as its the main script that runs the app.

PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.

Inside this script simple GUI, we have different elements like :-

    Dialog - houses all the GUI items in the app with the class name `Ui_Dialog` which has the `Setup_Ui` function defined in it, the Setup_Ui function setups our elements inside the Dialog.
    
So, inside the Dialog, we have all these items and they have a unique object name:-    

    Label - this a used as the text part which says, Battery Saver when you launch the app, its ordinary and can only be static, default object name for this item is `label`.
    
    TextEdit - this element is the one with instructions and note, it can be dynamic or set to static, the object name for this is `textEdit`.
    
    TableWidget - this table was integrated with the `main.py` file after importing it into the `battery_saver.py` , see list_process() function inside the battery_saver.py script. The table item is always used for dynamic purposes, but can be static and has it's default objectname as `tableWidget`.
    
    PushButton -  the pushbutton is the button with run when you open the app, it's default objectname is pushButton, and it's connected to a function.


**Little breakdown**

Lets look at the class running the script - MyForm() inside the battery_saver.py

A Class can have many or one function, but using OOP, 
lets look at the class's __init__() function :- 

1. we called a super() on it, to overwrite any other arguement from the old Dialog, since our class has the QDialog from the finalbat.py script in other to always run the battery_saver.py script over the finalbat.py.

2. Now setup the new Dialog with setting `ui = Ui_Dialog`

3. Cleared the tableWidget contents  `tableWidget.clearContents()`

4. Since I imported the main.py file into the battery_saver.py , then I set a variable to capture the list of apps `proc = get_apps()`

5. called a show on the dialog variable, to make it load the page immediately I run the app. 

6. connected the pushButton to the `run_app()` function

7. Show list of apps in the tableWidget, the table widget has just to two main function in this script, to select apps and filter the apps when user click each column header i.e sort by pid or the percentage usage or name of the process, which is displayed as the column header.

About the run_app() function inside the MyForm() class. 

1. run kill_pid() function 

2. run the reduce_brightness() function

These functions were connected to pushButton so immediately you click the run button on the app, both the kill the selected app and reduce the screen brightness.



To use as script, clone and run the `battery_saver.py` file.

The .exe file can found inside 


