#coding:utf-8
#socket_progs.py
#Christian Göhler
#14.11.2017
#Socket-Server für die Remote Steuerung über Computer oder Handy
#from __future__ import print_function
import socket
import threading
import os
from queue import Queue 

NUMBER_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_adresses = []


#Create Connection
def create_socket():
    try:
        global host
        global port
        global s        
        host = ''
        port = 9999     
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print ('Fehler beim Erzeugen eines Sockets: ' + str (msg))

# Binding den Socket und auf Verbindungen hören
def bind_socket():
    try:
        global host
        global port
        global s        
        print('Binding auf Port: ' + str(port))
        s.bind((host,port))
        s.listen (5)     
    except socket.error as msg:
        print('Fehler beim Bind eines Sockets: ' + str (msg) + '/n' + 'neuer Verbindungsversuch..')
        bind_socket()
#1. Thread
def accepting_connections():
    for c in all_connections:# Liste leeren/initialisieren
        c.close()
        
    del all_connections[:]
    del all_adresses[:]
    while True:
        try:
            conn.adress = s.accept()
            s.setblocking(1) #prevent timeout
            
            all_connections.append(con)
            all_adresses.append(adress)
            
            print ("Verbindung wurde unter "+ adress[0] + "aufgebaut")
        except:
            print ("Fehler beim Aufbau der Verbindung")
#2. Thread Senden von Daten
def start_turtle():
    
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
            
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
                
            else:
                print ("Befehl nicht erkannt:" + cmd)

def list_connections():
    results = ''
    
 
    for i.conn in enumerate(all_connections):
        try:
            conn.send(str.encode(''))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_adresses[i]
            continue
        
        results = str[i] + "  " + str(all_adresses[i][0]) + "  " + str(all_adresses[i][1]) + "\n"
        
    print("--------Clients------" + "\n" + results)
    
    def get_target(cmd):
        try:
            target = cmd.replace('select', '')
            target = int(target)
            conn = all_connections(tar)
            print ("Du bist mit " + str(all_adresses[target][0])+" verbunden")
            print (str(all_adresses[target][0]) + ">", end="")
            return conn
        except:
            print ("Treffen Sie eine gültige Auswahl")
            return None

def send_target_commands(conn):          
    while True: #unendliche Schleife um das Schließen des Sockets zu verhindern
        try:
            ser_response = 'Hier ist der Socket-Server vom Berry-Car' 
            cmd = input()
            if cmd == 'quit':#Beenden
                break
            if len(str.encode(cmd)) > 0: #Verwandelt String in Byte
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print (client_response, end="")
        except:
            print("Fehler beim Senden von Befehlen")
            break
        
def create_workers():
    for _ in range(NUMBER_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True # Damit Speicher beim Beenden des Programm wieder freigegeben wird
        t.start()
        
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle()
       
        queue.task_done()
            
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    
    queue.join()

create_workers()
create_jobs()