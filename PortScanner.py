#!/usr/bin/python3

import socket #the socket lib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = "137.74.187.104"  #Ping the site
port = 443

def portScanner(port):
    if s.connect_ex((host, port)):
        print("port is closed")
    else:
        print("port is open")
    