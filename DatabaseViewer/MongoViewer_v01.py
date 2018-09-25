print ("+++++++++Mongo-Viewer+++++++++")
print ("Menu1:Was willst Du machen?")
print ("1-Neuer Konfig-Eintrag")
print ("2-Neuer Datenbank-Eintrag")
print ("3-Eintraege anzeigen")
print ("4-Eintraege anzeigen")
menu1 = input()
if menu1:
   print ("Neuer Konfig-Eintrag")
   print ("Funktion noch nicht implementiert")
elif menu2:
   print ("Neuer Datenbank-Eintrag")
   print ("Funktion noch nicht implementiert")
elif menu3:
   print ("Verzeichnis aus Konfig-Eintrag kopieren")
   
   print ("***********Quellverzeichnis ermitteln***********")
   print ("------------Konfigdatei einlesen------------")
   print ("***********Schleife:Quellverzeichnis durchsuchen***********")
   print ("***********Aenderungsdatum vergleichen***********")
   print ("***********Datei kopieren und Konfig aktualisieren***********")
elif menu4:
   print ("Verzeichnis aus Datenbank-Eintrag kopieren")
   print ("***********Quellverzeichnis ermitteln***********")
   print ("------------Datenbankeintrag einlesen------------")
   print ("***********Schleife:Quellverzeichnis durchsuchen***********")
   print ("***********Aenderungsdatum vergleichen***********")
   print ("***********Datei kopieren und Konfig aktualisieren***********")
else:
    print ("unbekannte Eingabe")
print ("+++++++++Programmende+++++++++")
