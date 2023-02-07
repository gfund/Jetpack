import time
import sys
import subprocess 
import os
import platform
import apps
import json
import classes




def makedirectory():
    #Lazy Implementation So Far
    try:
     os.mkdir("Files")
    except:
        pass
#do fancy character by character typing
def fancytyping(message:str):

    for i in message:
        sys.stdout.write(i+ " ")
        sys.stdout.flush()
        time.sleep(0.1)

#take multiple lines of input with one function
def multiinput(numfieldstoexpect,questions):
   answers=[]
   for i in range(0,numfieldstoexpect):
   
    if(i<numfieldstoexpect):
     answers.append(input(questions[i]+" "))
  
    
   return answers

#install packages during runtime 
def packageinstall(packages):
    for package in packages:
        subprocess.call(['pip', 'install',package])
        print(f"Installing {package}")
def getcurrentdir():
    return os.getcwd()
def getplatform():
    return platform.system()
def getfilesep():
     #              Windows                                Linux and Mac
     filepathseparator= "\\" if(getplatform()=="Windows") else "/"
     return filepathseparator
def checkinstall():
    cwd=os.getcwd()
    #get file path separator by system
   
    filepathseparator= getfilesep()

    
    fpath=cwd+filepathseparator+"userfile.json"
    
    return os.path.isfile(fpath)
    
def switch(category,option):
    if(category=="apps"):
        if(option=="calculator"):
            apps.calculator()
        elif(option=="word"):
            apps.wordprocessor()
        elif(option=="notes"):
            apps.classnotes()
        elif(option=="google"):
            apps.terminalbrowser()
        elif(option=="canvas"):
            
            apps.canvasfunction(classes.User.getuser().lplatform.apiurl,classes.User.getuser().lplatform.apikey,classes.User.getuser().lplatform.uid)

def filesave(fname):
    installpath=2
    try:
     os.chdir("Files")
    except:
        print("Oops, file save did not work :(")

    