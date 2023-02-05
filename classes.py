
import json
import util
class LearningPlatform:

    name=""
    apikey=""
     
    def __init__(self, name, apikey):
        self.name=name
        self.apikey=apikey
    def serialize(self):
        return f"{self.name},{self.apikey}"
     
class User:
    name=""
    os=""
    email=""
    school=""
    connections=[]
    lplatform=LearningPlatform("","")
    
        
    def __init__(self, name, email,school,strlplatform):
     self.name = name
     self.os=util.getplatform()
     self.email = email
     self.school=school
     self.connections=[]
     try:
  
      self.lplatform=LearningPlatform(strlplatform.split(",")[0],strlplatform.split(",")[1]) #initialize learning platform
     except Exception as e:
        
        print("Oops you did not put a comma between the Learning Platform Name and your API Key :(, Installation will now restart")
        self.name="Error"

    def store(self):
        
        uservars ={ 
  "name": self.name, 
  "os": self.os, 
  "email": self.email,
  "school":self.school,
  "connections":self.connections,
  "lplatform":self.lplatform.serialize()} 
        try:
          storagefile=open("userfile.json", "w+")
          json.dump(uservars, storagefile)
          return 1
        except Exception as e:
          print(e)
          util.fancytyping("Well thats unfortunate! Something went wrong with storing your data :(")



