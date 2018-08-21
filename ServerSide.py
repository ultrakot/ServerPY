# -*- coding: utf-8 -*-
import random
import sys
import os
import socket

HOST = '127.0.0.1'    #standard loopback
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST. PORT)
    s.listen()
    (conn, address) = s.accept()
    with conn:
        print('connected by ', address)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)



# def main():
#     """
#     Add Documentation here
#     """
#     pass  # Replace Pass with Your Code
#
#
# if __name__ == '__main__':
#     main()