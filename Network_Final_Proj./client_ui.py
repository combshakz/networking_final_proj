# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Client_UI_Mainwindow(object):
    def setupUi(self, Client_UI_Mainwindow):
        Client_UI_Mainwindow.setObjectName("Client_UI_Mainwindow")
        Client_UI_Mainwindow.resize(772, 560)
        self.centralwidget = QtWidgets.QWidget(Client_UI_Mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_msg_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_msg_display.setGeometry(QtCore.QRect(30, 60, 511, 391))
        self.text_msg_display.setObjectName("text_msg_display")
        self.send_msg_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_msg_button.setGeometry(QtCore.QRect(440, 484, 89, 31))
        self.send_msg_button.setObjectName("send_msg_button")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(610, 120, 111, 41))
        self.connect_button.setObjectName("connect_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 60, 67, 17))
        self.label.setObjectName("label")
        self.send_pics_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_pics_button.setGeometry(QtCore.QRect(580, 290, 161, 41))
        self.send_pics_button.setObjectName("send_pics_button")
        self.send_videos_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_videos_button.setGeometry(QtCore.QRect(580, 360, 161, 41))
        self.send_videos_button.setObjectName("send_videos_button")
        self.leave = QtWidgets.QPushButton(self.centralwidget)
        self.leave.setGeometry(QtCore.QRect(580, 470, 161, 51))
        self.leave.setObjectName("leave")
        self.server_ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.server_ip_input.setGeometry(QtCore.QRect(570, 80, 181, 31))
        self.server_ip_input.setObjectName("server_ip_input")
        self.msg_to_send = QtWidgets.QLineEdit(self.centralwidget)
        self.msg_to_send.setGeometry(QtCore.QRect(30, 470, 511, 61))
        self.msg_to_send.setObjectName("msg_to_send")
        self.msg_to_send.raise_()
        self.text_msg_display.raise_()
        self.send_msg_button.raise_()
        self.connect_button.raise_()
        self.label.raise_()
        self.send_pics_button.raise_()
        self.send_videos_button.raise_()
        self.leave.raise_()
        self.server_ip_input.raise_()
        Client_UI_Mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Client_UI_Mainwindow)
        self.statusbar.setObjectName("statusbar")
        Client_UI_Mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Client_UI_Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Client_UI_Mainwindow)

    def retranslateUi(self, Client_UI_Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Client_UI_Mainwindow.setWindowTitle(_translate("Client_UI_Mainwindow", "Client"))
        self.send_msg_button.setText(_translate("Client_UI_Mainwindow", "SEND MSG"))
        self.connect_button.setText(_translate("Client_UI_Mainwindow", "CONNECT"))
        self.label.setText(_translate("Client_UI_Mainwindow", "Server IP"))
        self.send_pics_button.setText(_translate("Client_UI_Mainwindow", "Send Pics"))
        self.send_videos_button.setText(_translate("Client_UI_Mainwindow", "Send Videos"))
        self.leave.setText(_translate("Client_UI_Mainwindow", "Leave Chat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Client_UI_Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_Client_UI_Mainwindow()
    ui.setupUi(Client_UI_Mainwindow)
    Client_UI_Mainwindow.show()
    sys.exit(app.exec_())

