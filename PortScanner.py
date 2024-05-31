#!/usr/bin/python3

import socket #the socket lib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

#host = "137.74.187.104"  #Ping the site you want IP address

host = input("Enter IP to scan: ")
port = int(input("Enter port to scan: "))

#port = 22, should return false (ssh port)




def portScanner(port):
    if s.connect_ex((host, port)):
        print("port is closed")
    else:
        print("port is open")
    

portScanner(port)