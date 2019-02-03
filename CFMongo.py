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
    for filename in os.listdir(setting["source"]):#[:len(source)-1]
        for fileToCompare in setting["ignoredFiles"]:
           if (filename != fileToCompare):
            #if (filename[0:1] != "." or filename != fileToCompare):
                #print(filename[0:1])
                print(filename)
                print(fileToCompare)
                print("_____________")
                break
    
    collection = {"name": "Homepage",
            "filePathName": "Pfadname",
            "lastUpdated":"D:\Programmieren\GitHub\Homepage\MSIExtreme",
            "status":"D:\Programmieren\GitHub\Homepage\server"}
    result = dbProjectFiles.insert_one(collection)
    print (result)

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


