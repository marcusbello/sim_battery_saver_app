**Simple Battery Saver App**

This app was developed using python programming language, with the
intention of using it to reduce the overall battery usage on a 
windows machine. 

How it works:-

1. Get the list of processes running on the cpu percentage 
above 0.0% .

_Used the python psutil module , read more about it here https://psutil.readthedocs.io/_

2. Selected processes will be closed when the app user clicks the 
run button.

_With the help of the os module , I used os.system() to call a taskkill on all the selected processes pid._

3. Lastly, the app also reduces the screen brightness to 20% 
immediately you click the run button.

_tweaked the brightness with WMI , learn more about wmi module here https://pypi.org/project/WMI/_

The GUI was designed using pyqt5 and to run this script , clone and 
run the `callFinalUi.pyw` file.


