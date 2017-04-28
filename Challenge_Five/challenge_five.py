#!/usr/bin/python           
import socket             

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 

s.connect(("https://52.49.91.111:8443/ghost" , 80))
print s.recv(4096)
s.close  