import time
import sys
import subprocess 
import os
import platform

def makedirectory():
    os.mkdir("Files")
#do fancy character by character typing
def fancytyping(message:str):

    for i in message:
        sys.stdout.write(i+ " ")
        sys.stdout.flush()
        time.sleep(0.15)

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

def getplatform():
    return platform.system()
def checkinstall():
    cwd=os.getcwd()
    #get file path separator by system
    #              Windows                                Linux and Mac
    filepathseparator= "\\" if(getplatform()=="Windows") else "/"

    
    fpath=cwd+filepathseparator+"userfile.json"
    
    return os.path.isfile(fpath)
    
