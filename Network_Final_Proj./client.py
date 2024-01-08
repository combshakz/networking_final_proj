import cv2, imutils, socket
import numpy as np
import time
import base64

# host_name = socket.gethostname()
host_ip = '140.116.215.120'#  socket.gethostbyname(host_name)
print(host_ip)
port = 7800
BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
client_socket.connect((host_ip,port))