# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JRe_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(693, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1.sizePolicy().hasHeightForWidth())
        self.tab1.setSizePolicy(sizePolicy)
        self.tab1.setObjectName("tab1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 97))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GroupFromDate = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupFromDate.sizePolicy().hasHeightForWidth())
        self.GroupFromDate.setSizePolicy(sizePolicy)
        self.GroupFromDate.setMaximumSize(QtCore.QSize(16777215, 85))
        self.GroupFromDate.setFlat(False)
        self.GroupFromDate.setCheckable(True)
        self.GroupFromDate.setChecked(True)
        self.GroupFromDate.setObjectName("GroupFromDate")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.GroupFromDate)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.dateEdit = QtWidgets.QDateEdit(self.GroupFromDate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2023, 3, 18))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_8.addWidget(self.dateEdit)
        self.horizontalLayout_2.addWidget(self.GroupFromDate)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.GroupUntilDate = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupUntilDate.sizePolicy().hasHeightForWidth())
        self.GroupUntilDate.setSizePolicy(sizePolicy)
        self.GroupUntilDate.setMaximumSize(QtCore.QSize(16777215, 85))
        self.GroupUntilDate.setCheckable(True)
        self.GroupUntilDate.setObjectName("GroupUntilDate")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.GroupUntilDate)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.GroupUntilDate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setDate(QtCore.QDate(2023, 3, 18))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_6.addWidget(self.dateEdit_2)
        self.horizontalLayout_2.addWidget(self.GroupUntilDate)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DescriptionText = QtWidgets.QTextBrowser(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionText.sizePolicy().hasHeightForWidth())
        self.DescriptionText.setSizePolicy(sizePolicy)
        self.DescriptionText.setMinimumSize(QtCore.QSize(0, 8))
        self.DescriptionText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.DescriptionText.setFrameShape(QtWidgets.QFrame.Box)
        self.DescriptionText.setLineWidth(0)
        self.DescriptionText.setMidLineWidth(1)
        self.DescriptionText.setOpenExternalLinks(True)
        self.DescriptionText.setObjectName("DescriptionText")
        self.verticalLayout.addWidget(self.DescriptionText)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(160, 165))
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable|QtWidgets.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_9.addWidget(self.tableWidget)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_2)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JRe!"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Filters"))
        self.GroupFromDate.setTitle(_translate("MainWindow", "From Date:"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.GroupUntilDate.setTitle(_translate("MainWindow", "Until Date:"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.groupBox.setTitle(_translate("MainWindow", "Description"))
        self.DescriptionText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Review Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Table of Reviews"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Table of Reviews"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Due Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
