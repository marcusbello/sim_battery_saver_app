import os
import sys
from wmi import WMI
from PyQt5.QtWidgets import QDialog, QApplication
from finalbat import *
from main import *

WMI_CONNECTION = WMI(moniker='root/wmi')

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.clearContents()
        self.proc = get_apps()
        self.show()
        self.ui.pushButton.clicked.connect(self.run_app)
        self.list_process()

    def run_app(self):
        self.kill_pid()
        self.reduce_brigtness()

    def list_process(self):
        row = -1
        for proc in self.proc:
            row += 1
            self.ui.tableWidget.setRowCount(row+1)
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(row, 0, item)
            item.setText(str(proc['pid']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(row, 1, item)
            item.setText(proc['name'])
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(row, 2, item)
            item.setText(str(proc['cpu_percent']))
            # item = QtWidgets.QTableWidgetItem()
            # self.ui.tableWidget.setItem(row, 3, item)
            # item.setText(str(proc['num of threads']))

    def reduce_brigtness(self):
        try:
            WMI_CONNECTION.WmiMonitorBrightnessMethods()[0].WmiSetBrightness(20, 0)
        except Exception as e:
            print(e)

    def stop_fan(self):
        pass

    def kill_pid(self):
        kills = []
        for i in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.item(i, 0).isSelected():
                get_pid = self.ui.tableWidget.item(i, 0).text()
                print(get_pid)
                kills.append(get_pid)
                # killerapp(kills)
                os.system("taskkill /f /t /pid " +get_pid)
                # kill_proc_tree(get_pid)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
