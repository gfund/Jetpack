import install
import util
import classes
installdone=util.checkinstall()
def programselection():
   whatdoyouwant=""
   while whatdoyouwant!="quit":
    whatdoyouwant=input(">")
    util.switch("apps",whatdoyouwant)
   

if(installdone):
    classes.User.getuser()
    programselection()
    
else:
    
   install.installloop()
   print("\n")
   programselection()


