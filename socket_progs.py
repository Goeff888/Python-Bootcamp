#coding:utf-8
#socket_progs.py
#Christian Göhler
#14.11.2017
#Socket-Server für die Remote Steuerung über Computer oder Handy
#from __future__ import print_function
import socket
import sys

#print '....SOCKET START!!!...'

#Create Socket
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
         
        print ('Binding auf Port: ' + str(port))
        s.bind((host,port))
        s.listen (5)
     
    except socket.error as msg:
        print ('Fehler beim Bind eines Sockets: ' + str (msg) + '/n' + 'neuer Verbindungsversuch..')
        bind_socket()

#Verbindung mit Client aufbauen
def socket_accept():
    print ("Socket accept")
    conn,address = s.accept()
    #print (conn)
    #print (adress)
    print ('Verbindung wurde aufgebaut unter IP:' + address[0] + ' Port:' + str (address[1]))
    send_command(conn)
    conn.close()

#Senden von Befehlen an den Client
def send_command(conn):  
    while True: #unendliche Schleife um das Schließen des Sockets zu verhindern
        ser_response = 'Hier ist der Socket-Server vom Berry-Car' 
        cmd = input()
        if cmd == 'quit':#Beenden
            print ('verbindung wird beendet')
            conn.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print (client_response, end="")
            
        #client_response = str(conn.recv(1024)).encode("utf-8")
        #if (len(str.encode(client_response)) >0): #Prüfen, ob eine Antwort gekommen ist'
         #   if (client_response=='for'):
          #       print (client_response)
           # elif (client_response=='bac'):
            #     print (client_response)
            #elif (client_response != '' ):
             #   print (client_response)
        #elif (client_response == 'quit'):#Beenden
         #   print ('verbindung wird beendet')
          #  conn.close()
           # sys.exit()

        #if (len(str.encode(client_response)) >0): #nur daten auswerten wenn  größer null)
            #conn.send(str.encode(cmd))
         #   client_response = str(conn.recv(1024)).encode("utf-8")# Python 3.6: str(conn.recv(1024),"utf-8") #konvertiert von byte zu string, 1 junk = 1024; 
            
          #  print (client_response)
def main():
    create_socket()
    bind_socket()
    socket_accept()
   

main()
            