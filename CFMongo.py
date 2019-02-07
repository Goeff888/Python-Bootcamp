#status
#0 = file new
#1 = file copied and updated
#2 = folder new
#3 = folder copied and updated
#4 = file deleted
###########IMPORTS
import os
import shutil
from datetime import datetime
from pymongo import MongoClient

#print(os.path.isdir("/home/el"))
#print(os.path.exists("/home/el/myfile.txt"))
###########FUNKTIONEN
def createNewSettingsDB():
    print('Neues Datenbankprojekt anlegen')
    modelProject = {"name": "Homepage",
            "about": "Dateien von Arbeitsverzeichnis fuer Server aufbereieten und kopieren ",
            "source":"D:\Programmieren\GitHub\Homepage\MSIExtreme",
            "dest":"D:\Programmieren\GitHub\Homepage\server",
            "ignoredFiles":["package.json","package-lock.json"],
            "ignoredFolder":["node_modules"],
            "created": "now"}
    result = dBproject.insert_one(modelProject)
    createNewFileDB(modelProject)
    print (result)
 
def createNewFileDB(setting):
    print('Neues Dateisammlung fuer ein Projekt anlegen')
    for filename in os.listdir(setting["source"]):
        tempFileStatus = 0
        if (filename[0:1] == "."):
            #print("Datei" + filename +" beginnt mit einem Punkt .")
            tempFileStatus = 1    
        elif(os.path.isdir(setting["source"] + "\\" + filename)):
            #print(filename +" ist ein Verzeichnis und wird hier mit ignored folders verglichen")
            for folderToCompare in setting["ignoredFolder"]:
                if (filename == folderToCompare):
                    tempFileStatus = 0
                    break
                else:
                    tempFileStatus = 2
        else:
            for fileToCompare in setting["ignoredFiles"]:
                if (filename == fileToCompare):
                    tempFileStatus = 3
                    break
                else:
                    tempFileStatus = 4
        if (tempFileStatus==4):
            #print(filename+" mit Status neu anlegen")
            entry = {"name": filename,
                    "filePathName":setting["source"],
                    "lastUpdated": datetime.now(),
                    "status":4,
                    "change":[],
                    "projectID": setting["_id"]}
            dbProjectFiles.insert_one(entry)
        elif(tempFileStatus == 2):
            print(filename+" mit Status neu anlegen")
            entry = {"name": filename,
                    "filePathName":setting["source"],
                    "lastUpdated": datetime.now(),
                    "status":2,
                    "change":[],
                    "projectID": setting["_id"]}
            dbProjectFiles.insert_one(entry)
        #else:
            #print("Nichts machen")
    addChanges("app.js")
    copyFiles(setting["_id"],setting)        
  
def copyFiles(id, project):
    filesToCopy = dbProjectFiles.find({"projectID":id})
    for file in filesToCopy:
        if (file["status"] == 4):
            if (file['change']):
                addChangesToFile(file,project["dest"])
            else:
                shutil.copy2(file["filePathName"] + "\\" + file["name"], project["dest"] + "\\" + file["name"])
        elif (file["status"] == 2):
            if(os.path.isdir(project["dest"] + "\\" + file["name"])):
                print ("Path exists")
            else:
                print ("Path will be created)")
                os.makedirs(project["dest"] + "\\" + file["name"])

def addChangesToFile(colFile,dest):
    print ("Aenderung schreiben")
    sourceFile = open(colFile["filePathName"] + "\\" + colFile["name"])
    destFile =  open(dest + "\\" + colFile["name"],"w")
    #sourceFile.read()
    for zeile in sourceFile:#hier schreiben (Algorithmus aus alter Datei  pruefen, um Suche abzukuerzen)
        changes = colFile["change"]
        print(changes[0]["changeString"])
        print(zeile[:40])
        if (changes[0]["changeString"] == zeile[:40]):
            destFile.write(changes[0]["newString"])
            print("zeile umschreiben")
            #print("+++++++++++++++++++++++++++++++++++++++++++Zeile in app.js gefunden++++++++++++++++++++++++++++")
        else:
            print("nur zeile kopieren")
            destFile.write(zeile) 
    sourceFile.close
    destFile.close

def addChanges(name):
    changeArray = {"changeString" : 'app.listen(8888,"127.0.0.1", function(){',"newString" : 'app.listen(8080,"http://192.168.0.104", function(){'}
    result = dbProjectFiles.find_one({'name': name})
    dbProjectFiles.update({'_id': result['_id']}, {'$push':{'change': changeArray}})


def deleteDatabases():
    print ("Datenbanken loeschen")
    dBproject.drop
    dbProjectFiles.drop


###########CODE      
# connect to MongoDB
client = MongoClient('localhost', 27017)
db=client.homepage
dBproject = db.projects
dbProjectFiles = db.projectFiles
dBproject.drop()
dbProjectFiles.drop()
settings = dBproject.find_one({"name": "Homepage"})

#deleteDatabases(settings)
print (settings)
#if (dBproject.find_one({"name": "Homepage"})):
#if (settings["name"] == "Homepage"):
if(settings):
    #print ("Datenbank existiert")
    source = settings["source"]
    dest = settings["dest"]
    #print (source,dest)
    for filename in os.listdir(source):#[:len(source)-1]
            print(filename)
else:
    createNewSettingsDB()
    
    #print ("Datenbank existiert nicht")


