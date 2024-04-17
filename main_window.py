# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 583)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(parent=self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_file = QtWidgets.QToolButton(parent=self.widget)
        self.add_file.setObjectName("add_file")
        self.horizontalLayout_4.addWidget(self.add_file)
        self.remove_file = QtWidgets.QToolButton(parent=self.widget)
        self.remove_file.setObjectName("remove_file")
        self.horizontalLayout_4.addWidget(self.remove_file)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.file_explorer = QtWidgets.QListWidget(parent=self.widget)
        self.file_explorer.setObjectName("file_explorer")
        self.verticalLayout_3.addWidget(self.file_explorer)
        self.splitter = QtWidgets.QSplitter(parent=self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(parent=self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.methodsSelect = QtWidgets.QComboBox(parent=self.widget1)
        self.methodsSelect.setObjectName("methodsSelect")
        self.methodsSelect.addItem("")
        self.methodsSelect.addItem("")
        self.methodsSelect.addItem("")
        self.methodsSelect.addItem("")
        self.methodsSelect.addItem("")
        self.methodsSelect.addItem("")
        self.methodsSelect.addItem("")
        self.horizontalLayout.addWidget(self.methodsSelect)
        self.urlIn = QtWidgets.QLineEdit(parent=self.widget1)
        self.urlIn.setObjectName("urlIn")
        self.horizontalLayout.addWidget(self.urlIn)
        self.send = QtWidgets.QPushButton(parent=self.widget1)
        self.send.setObjectName("send")
        self.horizontalLayout.addWidget(self.send)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.widget1)
        self.tabWidget.setObjectName("tabWidget")
        self.params_tab = QtWidgets.QWidget()
        self.params_tab.setObjectName("params_tab")
        self.tabWidget.addTab(self.params_tab, "")
        self.headers_tab = QtWidgets.QWidget()
        self.headers_tab.setObjectName("headers_tab")
        self.tabWidget.addTab(self.headers_tab, "")
        self.auth_tab = QtWidgets.QWidget()
        self.auth_tab.setObjectName("auth_tab")
        self.tabWidget.addTab(self.auth_tab, "")
        self.body_tab = QtWidgets.QWidget()
        self.body_tab.setObjectName("body_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.body_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.format_body_in = QtWidgets.QToolButton(parent=self.body_tab)
        self.format_body_in.setObjectName("format_body_in")
        self.horizontalLayout_3.addWidget(self.format_body_in)
        self.toolButton_3 = QtWidgets.QToolButton(parent=self.body_tab)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.body_in = QtWidgets.QTextEdit(parent=self.body_tab)
        self.body_in.setObjectName("body_in")
        self.verticalLayout_6.addWidget(self.body_in)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.body_tab, "")
        self.curl_tab = QtWidgets.QWidget()
        self.curl_tab.setObjectName("curl_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.curl_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.curl = QtWidgets.QTextEdit(parent=self.curl_tab)
        self.curl.setObjectName("curl")
        self.verticalLayout.addWidget(self.curl)
        self.tabWidget.addTab(self.curl_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.splitter)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.response_tab = QtWidgets.QWidget()
        self.response_tab.setObjectName("response_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.response_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.format_response = QtWidgets.QToolButton(parent=self.response_tab)
        self.format_response.setObjectName("format_response")
        self.horizontalLayout_2.addWidget(self.format_response)
        self.toolButton_2 = QtWidgets.QToolButton(parent=self.response_tab)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.response_out = QtWidgets.QTextEdit(parent=self.response_tab)
        self.response_out.setObjectName("response_out")
        self.verticalLayout_4.addWidget(self.response_out)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget_2.addTab(self.response_tab, "")
        self.response_tab1 = QtWidgets.QWidget()
        self.response_tab1.setObjectName("response_tab1")
        self.tabWidget_2.addTab(self.response_tab1, "")
        self.verticalLayout_8.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_file.setText(_translate("MainWindow", "..."))
        self.remove_file.setText(_translate("MainWindow", "..."))
        self.methodsSelect.setItemText(0, _translate("MainWindow", "GET"))
        self.methodsSelect.setItemText(1, _translate("MainWindow", "HEAD"))
        self.methodsSelect.setItemText(2, _translate("MainWindow", "POST"))
        self.methodsSelect.setItemText(3, _translate("MainWindow", "PUT"))
        self.methodsSelect.setItemText(4, _translate("MainWindow", "PATCH"))
        self.methodsSelect.setItemText(5, _translate("MainWindow", "DELETE"))
        self.methodsSelect.setItemText(6, _translate("MainWindow", "OPTIONS"))
        self.send.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.params_tab), _translate("MainWindow", "Params"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.headers_tab), _translate("MainWindow", "Headers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.auth_tab), _translate("MainWindow", "Auth"))
        self.format_body_in.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.body_tab), _translate("MainWindow", "Body"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.curl_tab), _translate("MainWindow", "cURL"))
        self.format_response.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.response_tab), _translate("MainWindow", "Response"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.response_tab1), _translate("MainWindow", "Response"))