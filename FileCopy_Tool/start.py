import os
def WriteEntry(entry):
   print("WriteEntry")
 
def compareAndCopy(savedFiles, source, dest):
    sourceFiles = []
    for destFolder in os.listdir(dest):
      print (destFolder)  

def createBackUp(filelist,souce,dest):
      print ("***********Schleife:Quellverzeichnis durchsuchen***********")
      print ("***********Aenderungsdatum vergleichen***********")
       for destFolder in os.listdir(dest):
         print (destFolder)

print ("+++++++++File-Copy Tool+++++++++")
print ("Menu1:Was willst Du machen?")
print ("A-Neuer Konfig-Eintrag")
print ("B-Neuer Datenbank-Eintrag")
print ("C-Verzeichnis aus Konfig-Eintrag kopieren")
print ("D-Verzeichnis aus Datenbank-Eintrag kopieren")
menu1 = input()
if menu1 == "A":
   print ("Neuer Konfig-Eintrag")
   print ("------------Konfigdatei einlesen------------")
   configIn = open('test.txt')
   filelist = []
   lineNumber =0
   for zeile in configIn:
      option = zeile.split(":")
      if option[0] == "Ende":
         print (zeile)
      elif option[0] == "Quellverzeichnis":
         source = option[1]
      else:
         print ("Noch keine Eintrag vorhanden")
      lineNumber = lineNumber + 1
   configIn.close()
   print ( lineNumber)
   configOut = open('test.txt')
   configOut.write()   
   # Name des Eintrags vom benutzer abfragen
   print ("Name des Eintrags:")
   entry =[]
   entry.append(input())
   # Quellverzeichnis des Eintrags vom benutzer abfragen
   print ("Quellverzeichnis")
   entry.append(input())
   # Dateien einlesen
   # Zielverzeichnis des Eintrags vom benutzer abfragen
   print ("Quellverzeichnis")
   entry.append(input())
   # Zielverzeichni anlegen
   # Anzahl der Eintr?ge ermitteln/ ans Ende der Datei springen
   error =  WriteEntry(entry)
   # Name vom benutzer schreiben
   # Quellverzeichnis vom benutzer schreiben
   # Zielverzeichnis vom benutzer schreiben
   # Dateien ans ende der Datei schreiben
   print ("Funktion noch nicht implementiert")
elif menu1=="B":
   print ("Zielverzeichnis aktualisieren")
   print ("Funktion noch nicht implementiert")
elif menu1=="C":
   print ("Dateien kopieren")
   print ("------------Konfigdatei einlesen------------")
   config = open('test.txt')
   filelist = []
   for zeile in config:
      option = zeile.split(":")
      if option[0] == "Eintrag":
         entry = option[1]
      elif option[0] == "Quellverzeichnis":
         print ("***********Quellverzeichnis ermitteln***********")
         source = option[1]
      elif option[0] == "Zielverzeichnis":
         dest = option[1]
      elif option[0] == "Dateiliste": 
         print ("Dateiliste mit geaenderten Dateien einlesen")
         if option[0] != "Ende":
            filelist.append(option[1])
      print ("***********Datei kopieren und Konfig aktualisieren***********")      
      createBackUp(filelist,souce,dest)
      print (filelist)
      
      
   
   


elif menu1=="D":
   print ("neuen Eintrag anlegen")
   print ("***********Quellverzeichnis ermitteln***********")
   print ("------------Datenbankeintrag einlesen------------")
   print ("***********Schleife:Quellverzeichnis durchsuchen***********")
   print ("***********Aenderungsdatum vergleichen***********")
   print ("***********Datei kopieren und Konfig aktualisieren***********")
else:
    print ("unbekannte Eingabe")
print ("+++++++++Programmende+++++++++")
