import socket
import sys
import cv2
import pickle
import numpy as np
import struct
# from capture import Camera
class Server:
    def __init__(self):
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 9898
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print('server.py : socket has been created.')

        s.bind((HOST, PORT))

        print('server.py : socket bind complete.')

        s.listen(10)

        print(f'main.py : server is listening on : {HOST}--------(localhost/ipv4)')
        while 1:
            client_socket, addr = s.accept()
            print(f'server.py : got connection from {addr}')
            if client_socket:
                self.cap = cv2.VideoCapture(0)
                while self.cap.isOpened():
                    img, frame = self.cap.read()
                    a = pickle.dumps(frame)
                    message = struct.pack("Q", len(a)+a)
                    cv2.imshow('TRANSMITTED', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'): break





