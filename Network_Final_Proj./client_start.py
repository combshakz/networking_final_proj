import sys
import urllib.request
import subprocess
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from client_ui import Ui_Client_UI_Mainwindow

external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')

class Client_Window(QtWidgets.QMainWindow):
    def __init__(self):#Qt Stuff..
        super(Client_Window, self).__init__()
        self.ui = Ui_Client_UI_Mainwindow()
        self.ui.setupUi(self)

        self.ui.msg_to_send.setText('TYPE YOUR MESSAGE HERE')

        self.setup_control()

    def setup_control(self):
        # button clicked
        self.ui.server_connect_button.clicked.connect(self.server_connect)
        self.ui.send_msg_button.clicked.connect(self.msgsend)
        self.ui.send_pics_button.clicked.connect(self.picsend)
        self.ui.send_videos_button.clicked.connect(self.videosend)
        self.ui.leave.clicked.connect(self.leave)

    def server_connect(self):
        subprocess.Popen(['python3','client.py'])
        print(external_ip)


    def msgsend(self):
        unsent_msg = self.ui.msg_to_send.text()
        display_text = 'Me : ' + unsent_msg
        self.ui.text_msg_display.append(display_text)
        #TODO


        print(unsent_msg)

    def picsend(self):
        pics_file , filetype = QFileDialog.getOpenFileName(self,'Choose Image',filter="Images (*.jpg);;Images (*.png)")
        #TODO


        print(pics_file)

    def videosend(self):
        video_file , file_type = QFileDialog.getOpenFileName(self,'Choose Video',filter="Video (*.mp4);;Video (*.mov)")
        #TODO


        print(video_file)

    def leave(self):
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Client_Window()
    MainWindow.show()
    sys.exit(app.exec_())