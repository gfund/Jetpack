
import json
import os
import platform

class LearningPlatform:

    name=""
    uid=0
    apiurl=""
    apikey=""
    issetup=0
     
    def __init__(self, name,uid,apiurl, apikey,issetup):
        self.name=name
        self.uid=uid
        self.apiurl=apiurl
        self.apikey=apikey
        self.issetup=issetup
    def serialize(self):
        return f"{self.name},{self.uid},{self.apiurl},{self.apikey},{self.issetup}"
     
class User:
    name=""
    
    os=""
    email=""
    school=""
    connections=[]
    lplatform=LearningPlatform("",0,"","",0)
    folderpath=""
    
        
    def __init__(self, name, email,school,strlplatform):
     self.name = name
    
     self.email = email
     self.school=school
     self.connections=[]
     self.folderpath=os.getcwd()
     try:
  
      
      self.lplatform=LearningPlatform(strlplatform.split(",")[0],int(strlplatform.split(",")[1]),strlplatform.split(",")[2],strlplatform.split(",")[3],int(strlplatform.split(",")[4])) #initialize learning platform
      #print(self.lplatform.serialize())
     except Exception as e:
        print(e)
        print("Oops you did not put a comma between the Learning Platform Name, API URL and your API Key :(, Installation will now restart")
        self.name="Error"

    def store(self):
        
        uservars ={ 
  "name": self.name, 
  "email": self.email,
  "school":self.school,
  "connections":self.connections,
  "folderpath":self.folderpath,
  "lplatform":self.lplatform.serialize()} 
        try:
          storagefile=open("userfile.json", "w+")
          json.dump(uservars, storagefile)
          return 1
        except Exception as e:
          pass
          # print(e)
         

    def userdataread(self,query):
        filepathseparator= "\\" if(platform.system()=="Windows") else "/"
        filesep=filepathseparator
        userfile = open(f"{self.folderpath+filesep}userfile.json")
        data = json.load(userfile)
        return data[query]
   
    def getuser():
        folderpath=os.getcwd()
        filepathseparator= "\\" if(platform.system()=="Windows") else "/"
        filesep=filepathseparator
        userfile = open(f"{folderpath+filesep}userfile.json")
        data = json.load(userfile)
        u=User(data['name'],data['email'],data['school'],data['lplatform'])
        return u
