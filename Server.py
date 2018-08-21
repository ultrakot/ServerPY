## -*- coding: utf-8 -*-
import random
import sys
import os
import socket
import time
import random
import datetime
from PIL import ImageGrab
from scapy.all import *

valid_commands = ["go", "delete", "jump"]

ip_address = '0.0.0.0'
port = 8820


def connect():
    pass


def send_file():
    some_file = open('stuff.txt', 'r')
    im = ImageGrab.grab()
    im.save(r'C:\screen.jpg')


def main():
    send_file()




#connection
# server_socket = socket.socket()
# server_socket.bind(('0.0.0.0', 8820))
# server_socket.listen(1)
#
# (client_socket, client_address) = server_socket.accept()
# #blocking
#
#
# ##list of commands
# commands = ["time", "name", "rand", "exit", "destroy"]
#
# #commands.append("take_screenshot")
# #del commands[3:]
# #commands[0] = none
# # for command in range(1997, 2000, 1):
# #     print command
#
# imageData = []
#
# return_value = ""
# user_input = client_socket.recv(1024)


# while user_input != "Exit" and user_input != "exit":
#     if user_input == "time":
#         return_value = str(datetime.datetime.now().time())
#
#     elif user_input == "take_screenshot":
#         im = ImageGrab.grab()
#         im.save(r'C:\screen.jpg')
#         return_value = "image saved as screen.jpg"
#
#     # elif user_input == "send_file":
#     #     #while True:
#     #      #   pass
#     #     imageData.append(sys.getsizeof(im.getim()))
#     #
#     #     client_socket.send(str(sys.getsizeof(im.getim())))
#
#     else:
#         return_value = "INCORRECT INPUT"
#
#     if return_value != "" and return_value is not None:
#         client_socket.send(return_value)
#         (client_socket, client_address) = server_socket.accept()
#         user_input = client_socket.recv(1024)
#         #take input from user again

# client_socket.close()
# server_socket.close()


