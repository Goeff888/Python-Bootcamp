#Model fuer settings
#"name": "Homepage",
#"about": "Dateien von Arbeitsverzeichnis fuer Server aufbereieten und kopieren ",
#"source":"Quelle",
#"dest":"Ziel"}
#fileid:objectId von model files

###########IMPORTS
import os
from pymongo import MongoClient

###########FUNKTIONEN
def createNewSettingsDB():
    print('Neues Datenbankprojekt anlegen')
    setting1 = {"name": "Homepage",
            "about": "Dateien von Arbeitsverzeichnis fuer Server aufbereieten und kopieren ",
            "source":"D:\Programmieren\GitHub\Homepage\MSIExtreme",
            "dest":"D:\Programmieren\GitHub\Homepage\server",
            "ignoredFiles":["package.json","package-lock.json"],
            "ignoredFolder":["node_modules"],
            "created": "now"}
    result = dBproject.insert_one(setting1)
    createNewFileDB(setting1)
    print (result)
 
def createNewFileDB(setting):
    print('Neues Dateisammlung fuer ein Projekt anlegen')
    for filename in os.listdir(setting["source"]):
        tempFileStatus = 0
        if (filename[0:1] == "."):
            print("Datei beginnt mit einem Punkt .")
            tempFileStatus = 1    
        elif(os.path.isdir(setting["source"] + "\\" + filename)):
            print("Datei ist ein Verzeichnis und wird hier mit ignored folders verglichen")
            tempFileStatus = 2
        else:
            for fileToCompare in setting["ignoredFiles"]:
                if (filename == fileToCompare):
                    break
                else:
                    tempFileStatus = 3
        print(tempFileStatus)
            #collection = {"name": "Homepage",
                   # "filePathName": "Pfadname",
                    #"lastUpdated":"D:\Programmieren\GitHub\Homepage\MSIExtreme",
                    #"status":"D:\Programmieren\GitHub\Homepage\server"}
                #result = dbProjectFiles.insert_one(collection)
            #print (collection)
        #if ("Entweder Datei aus obiger Abfrage"):
         #   print("Datei mit Status neu anlegen")
        #elif("Verzeichnis aus obiger Abfrage"):
         #    print("Verzeichnis mit Status neu anlegen")
        #else:
         #   print("Nichts machen")
            
            
def deleteDatabases(entry):
    dBproject.delete_one(settings)
###########CODE      
# connect to MongoDB
client = MongoClient('localhost', 27017)
db=client.homepage
dBproject = db.projects
dbProjectFiles = db.projectFiles
settings = dBproject.find_one({"name": "Homepage"})

#deleteDatabases(settings)
print (settings)
#if (dBproject.find_one({"name": "Homepage"})):
#if (settings["name"] == "Homepage"):
if(settings):
    print ("Datenbank existiert")
    source = settings["source"]
    dest = settings["dest"]
    print (source,dest)
    for filename in os.listdir(source):#[:len(source)-1]
            print(filename)
else:
    createNewSettingsDB()
    print ("Datenbank existiert nicht")


