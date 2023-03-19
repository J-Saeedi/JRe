# -*- coding: utf-8 -*-

import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QGroupBox, QTableWidget,\
    QTableWidgetItem, QComboBox, QDateEdit,\
    QTextBrowser, QDialog, QLineEdit, QRadioButton, \
    QPushButton, QDialogButtonBox
from time import sleep, time
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton

class ReviewMethods():
    current_methods={}
    def __init__(self, name):
        self.status_dict = {}
        self.name = name
        self.stages = [] # [0,1,2,4,8,16,32,64] # for standard method
        ReviewMethods.current_methods[self.name] = self

    

class JReMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("JRe_v1.ui", self)
        self.show()
        
        self.table = self.findChild(QTableWidget, "tableWidget")
        self.table_data = {}

        self.from_date_groupbox = self.findChild(QGroupBox, "GroupFromDate")
        self.until_date_groupbox = self.findChild(QGroupBox, "GroupUntilDate")

        self.combo_from_date = self.findChild(QComboBox, "ComboFromDate")
        self.combo_until_date = self.findChild(QComboBox, "CombUntilDate")

        self.date_edit_from = self.findChild(QDateEdit, "DateEditFrom")
        self.date_edit_until = self.findChild(QDateEdit, "DateEditUntil")
        self.date_edit_from.setEnabled(False)
        self.date_edit_until.setEnabled(False)

        self.description = self.findChild(QTextBrowser, "DescriptionText")
        self.add_new_program = self.findChild(QPushButton, "NewProgram")
        self.add_new_program.clicked.connect(self.double_clicked)

        self.update_table()
        self.activate_slots()
        self.adjust_date(self.date_edit_from, 4)
        self.adjust_date(self.date_edit_until, 1)

    def save_data(self, new_data, root_dir=".", file_name="data.txt"):
        with open(root_dir+'/'+file_name, 'a', encoding="utf-8") as f:
            f.write("\n"+new_data)

    # load data.txt
    def load_data(self, root_dir=".", file_name="data.txt"):
        # if data exists, then load them
        if os.path.exists(root_dir+'/'+file_name):
            data = []
            with open(root_dir+'/'+file_name, 'r', encoding="utf-8") as f:
                for this_line in f.readlines():
                    if this_line.strip():
                        data.append(this_line.strip())
            data.sort(key=lambda x:x.split("*|*")[2])
            return data
        else:
            # if data not exists, then 
            # create a data file and 
            # call the func. again
            with open(root_dir+'/'+file_name, 'w', encoding="utf-8") as f:
                f.write('\n')
                self.load_data(root_dir=root_dir, file_name=file_name)

    def adjust_date(self, target_dateedit, combo_index):
        index_dict = {0:+7, 1:+1, 2:0, 3:0, 4:-1, 5:-7}
        new_date = QtCore.QDate.currentDate().addDays(index_dict[combo_index]) 
        target_dateedit.setDate(new_date)
        

    def activate_slots(self):
        sleep(0.1)
        self.from_date_groupbox.toggled.connect(self.update_table)
        self.until_date_groupbox.toggled.connect(self.update_table)
        #-----
        self.combo_from_date.currentIndexChanged.connect(self.update_table)
        self.combo_from_date.currentIndexChanged.connect(lambda x: self.adjust_date(self.date_edit_from, x))
        self.combo_from_date.currentIndexChanged.connect(lambda x: self.date_edit_from.setEnabled(False) \
                                                         if x!=3 else self.date_edit_from.setEnabled(True) )
        #-----                                
        self.combo_until_date.currentIndexChanged.connect(self.update_table)
        self.combo_until_date.currentIndexChanged.connect(lambda x: self.adjust_date(self.date_edit_until, x))
        self.combo_until_date.currentIndexChanged.connect(lambda x: self.date_edit_until.setEnabled(False) \
                                                         if x!=3 else self.date_edit_until.setEnabled(True) )        
        #-----
        self.date_edit_from.dateChanged.connect(self.update_table)
        self.date_edit_until.dateChanged.connect(self.update_table)
        #-----
        self.table.cellDoubleClicked.connect(self.double_clicked)
        self.table.cellClicked.connect(lambda x,y: self.description.setText(self.table_data[x].split("#|")[1]))

    def update_table(self):
        #print('hola')
        table = self.table
        table.setRowCount(0)
        rowPosition = table.rowCount()
        for this_row in self.load_data():
            data, description = this_row[2:].split("#|")
            data = data.split("*|*")
            name = data[0]
            integer_date = int(data[1])
            date = data[1][:4]+'/'+data[1][4:6]+'/'+data[1][6:] # use integer date as filter
            method = data[3].split(":")[0]
            status = ReviewMethods.current_methods[method].status_dict[data[2]]

            if self.until_date_groupbox.isChecked(): # for until checkbox
                filter_date = self.date_edit_until.date()
                filter_date = str(filter_date.year()).zfill(4)+\
                    str(filter_date.month()).zfill(2)+str(filter_date.day()).zfill(2)
                filter_date = int(filter_date)
                if integer_date > filter_date: continue

            if self.from_date_groupbox.isChecked(): # for from checkbox
                filter_date = self.date_edit_from.date()
                filter_date = str(filter_date.year()).zfill(4)+\
                    str(filter_date.month()).zfill(2)+str(filter_date.day()).zfill(2)
                filter_date = int(filter_date) 
                if integer_date < filter_date: continue           

            table.insertRow(rowPosition)
            self.table_data[rowPosition] = this_row
            for index,this_item in enumerate([name, date, status]):
                table.setItem(rowPosition, index,\
                     QTableWidgetItem(str(this_item)))
                if index==2: break
            rowPosition += 1

    def double_clicked(self, item):
        if item :
            #print(self.table_data[item])
            dlg = CustomDialog(parent=self, form_data=self.table_data[item])
            button = dlg.exec()
            if button: # user applied the dialog box
                #print(f"this is your stage: {dlg.stage}")
                #print(f"this data gained: {dlg.output_data}")
                self.save_data(dlg.output_data)
        else:
            dlg = CustomDialog(parent=self)
            button = dlg.exec()
            if button: # user applied the dialog box
                #print(f"this is your stage: {dlg.stage}")
                #print(f"this data gained: {dlg.output_data}")
                self.save_data(dlg.output_data)
                self.update_table()




class CustomDialog(QDialog):
    def __init__(self, parent=None, form_data=""):
        super().__init__(parent)
        uic.loadUi("dia_v1.ui", self)

        self.pressed_time = 0

        self.name = self.findChild(QLineEdit, "Name")
        self.date = self.findChild(QDateEdit, "Date")
        self.good = self.findChild(QRadioButton, "Good")
        self.hard = self.findChild(QRadioButton, "Hard")
        self.forgot = self.findChild(QRadioButton, "Forgot")
        self.combo_method = self.findChild(QComboBox, "Method")
        self.commit = self.findChild(QPushButton, "Commit")
        self.commit.pressed.connect(self.tic)
        self.commit.released.connect(self.toc)
        self.description = self.findChild(QTextBrowser, "Description")
        self.button_box = self.findChild(QDialogButtonBox, "buttonBox")

        if form_data:
            #print('form data inserted')
            form_data, description = form_data[2:].split("#|")
            form_data = form_data.split("*|*")
            name = form_data[0]
            date = form_data[1]
            method = form_data[3]
            method, stage = method.split(":")
            self.stage = int(stage)
            self.method = ReviewMethods.current_methods[method]

            #-----
            self.name.setText(name)
            self.date.setDate(QtCore.QDate.currentDate())
            for index,this_method in enumerate(ReviewMethods.current_methods.keys()):
                self.combo_method.addItem(this_method)
                if method == this_method: 
                    self.combo_method.setCurrentIndex(index)
            self.description.setText(description)
            #self.date.setDate
            #new_date = QtCore.QDate.currentDate().addDays(method.stages[stage+self.correction_factor])

        else:
            #print("=============================")
            self.stage = 0
            for index,this_method in enumerate(ReviewMethods.current_methods.keys()):
                self.combo_method.addItem(this_method)
            self.method = ReviewMethods.current_methods[this_method]
            self.date.setDate(QtCore.QDate.currentDate())



    def tic(self):
        self.pressed_time=time()
    def toc(self):
        delta_time = time()-self.pressed_time       
        if delta_time >= 1.2:
            self.pressed_time = 0
            self.commit_data()

    def commit_data(self):
        status = 0
        if not (self.good.isChecked() | self.hard.isChecked() | \
            self.forgot.isChecked()):
            return None
        self.commit.setStyleSheet("background-color:rgb(90, 212, 45);")
        self.button_box.setEnabled(True)
        if self.good.isChecked():
            status = 1
            self.stage = self.stage+1
        elif self.hard.isChecked():
            status = 2
            self.stage = self.stage # LOL           
        elif self.forgot.isChecked():
            status = 3
            self.stage = 1
        #-----
        if len(self.method.stages)-1 < self.stage:
            self.stage = len(self.method.stages)-1
        #print("stage is:", self.stage)

        #------------
        # output data
        result = "$-" + self.name.text() + "*|*"
        new_date = self.date.date().addDays(self.method.stages[self.stage])
        result += str(new_date.year()).zfill(4)
        result += str(new_date.month()).zfill(2)
        result += str(new_date.day()).zfill(2)
        result += "*|*0*|*"
        result += self.combo_method.currentText()
        result += ":" + str(self.stage) + "#|"
        result += self.description.toPlainText()
        self.output_data = result

if __name__ == "__main__":
    R1 = ReviewMethods("R1")
    R1.status_dict = {"0":"ToDo", "1":"Good", "2":"Hard", "3":"Forgot"}
    R1.stages = [0,1,2,4,8,16,32,64]
    app = QtWidgets.QApplication(sys.argv)
    JRe_window = JReMainWindow()
    #JRe_window.show()
    sys.exit(app.exec_())