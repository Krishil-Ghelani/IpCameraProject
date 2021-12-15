import socket
import sys
import cv2
import pickle
import numpy as np
import struct
# import server
class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((socket.gethostbyname(socket.gethostname(

        ),9898)))

        while 1:
            ret, frame = self.cap.read()
            data = pickle.dumps(frame)
            self.client_socket.sendall(struct.pack("L", len(data))+data)
            cv2.imshow("Frame", frame)
            print(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): break


        self.cap.release()

        cv2.destroyAllWindows()