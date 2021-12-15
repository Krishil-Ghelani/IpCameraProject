import socket
import sys
import cv2
import pickle
import numpy as np
import struct

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9898
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('server.py : socket has been created.')

s.bind((HOST, PORT))

print('server.py : socket bind complete.')

s.listen(10)

print(f'main.py : server is listening on : {HOST}--------(localhost/ipv4)')

conn, addr = s.accept()

data = b''

payload_size = struct.calcsize("L")
while 1:
    while len(data) < payload_size:
        data+=conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data=data[payload_size:]
    msg_size=struct.unpack('L', packed_msg_size)[0]
    while len(data)<msg_size:
        data += conn.recv(4096)
    frame_data= data[:msg_size]
    data= data[msg_size:]



