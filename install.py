import sys
#Class Files
from classes import *
from util import *
global installationsuccessful
installationsuccessful=False
logo="""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⣿⡟⠻⢶⣤⣀⣀ ⣀⣿⣿⣿⡿⠛⢿⣿⣿⣿⣿
⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⣸⡿⠛⠉⠻⣿⡁⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⡁⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⣼⠏⠀⠀⠀⠀⢸⣷⣄⡀⠀ ⣿⣿⣿⣿
⣿⣿⣿⣷⣶⣤⣄⣀⣼⠋⠀⠀⠀⢰⡿⠀⠀⠀⠀⢀⣾⠃⠉⠻⢶⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠸⣷⡀⠀⢀⣤⡾⠃⠀⠀⢀⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠿⣦⣄⡀⠀⠀⣽⠟⠟⠛⠉⠀⠀⠀⢠⡾⠃⠘⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠉⣿⣶⣾⡏⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀⠈⢿⣿⣿
⣿⣿⣿⣿⡿⠛⣷⣦⣄⠀⠀⣿⣿⡿⠟⠳⢦⣄⡀⠀⣰⡟⠁⠀⠀⠀⠀⠈⢻⣿
⣿⣿⣿⡿⢁⣾⠏⢠⣿⠻⣶⣿⡋⠀⠀⠀⠀⠙⣿⣶⣿⣿⣦⣄⠀⠀⠀⢀⣾⣿
⣿⣿⡟⢡⣿⠃⣠⡿⠃⣰⣿⠋⣻⣷⣤⣀⠀⢠⣿⣿⣿⣿⣿⣿⣷⣦⣠⣿⣿⣿
⣿⠟⢠⣿⠃⣰⡿⠁⣼⡿⠃⣼⡟⢀⣾⠟⢿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣠⡿⠁⣼⡟⢀⣾⡿⠁⣼⡟⢀⣾⠋⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣥⣼⣯⣤⣿⣿⣥⣼⣿⣤⣿⣧⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""


#look for user file and if not present, do intro
def install(): 

 
 global installationsuccessful


 print(f"\n {logo}")
 fancytyping("Jetpack V1\nWelcome New User! \n")
 userfields=multiinput(4,["What is your name?","What is your email? (For notification purposes)","What school do you attend?(Relevant Content)","If you wish to hook up your Learning Platform to Jetpack,insert the name of the platform ie Canvas and the API Key."])
 
 u=User(userfields[0],userfields[1],userfields[2],userfields[3]) #create new instance of user 
 if(u.name=="Error"):
    #stop
    return
 rtrn=u.store()
 
 if(rtrn):
  fancytyping(f"Hello {userfields[0]}, glad to have you!")
  installationsuccessful=True
  makedirectory()
  return
 else:
     fancytyping(f"There was an error during the install :(.Trying again!")
def installloop():
 global installationsuccessful
 #print(util.checkinstall()) 
 if(not checkinstall()):
  while (not installationsuccessful):
   install()