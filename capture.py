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
        self.client_socket.connect(('192.168.1.15', 9898)), print('worked')

        data = b''

        payload_size = struct.calcsize("Q")
        while 1:
            while len(data) < payload_size:
                packet = self.client_socket.recv(4096)
                if not packet: break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack('Q', packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.client_socket.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow("RECEIVED", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'): break

        self.client_socket.close()


        self.cap.release()

        cv2.destroyAllWindows()