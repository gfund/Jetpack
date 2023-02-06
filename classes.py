
import json
import os
import platform

class LearningPlatform:

    name=""
    apiurl=""
    apikey=""
     
    def __init__(self, name,apiurl, apikey):
        self.name=name
        self.apiurl=apiurl
        self.apikey=apikey
    def serialize(self):
        return f"{self.name},{self.apiurl},{self.apikey}"
     
class User:
    name=""
    
    os=""
    email=""
    school=""
    connections=[]
    lplatform=LearningPlatform("","")
    folderpath=""
    
        
    def __init__(self, name, email,school,strlplatform):
     self.name = name
    
     self.email = email
     self.school=school
     self.connections=[]
     self.folderpath=os.getcwd()
     try:
  
      self.lplatform=LearningPlatform(strlplatform.split(",")[0],strlplatform.split(",")[1],strlplatform.split(",")[2]) #initialize learning platform
     except Exception as e:
        
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
