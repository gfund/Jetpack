import install
import util
import classes
installdone=util.checkinstall()
exitterms=["exit","quit","q","stop"]
def programselection():
   selection=""
   while selection not in exitterms:
    selection=input(">")
    util.switch("apps",selection)
   util.fancytyping("Goodbye for now!")
   

if(installdone):
    u=classes.User.getuser()
    if(u.lplatform.name=="Canvas"):
        if(not u.lplatform.issetup):
         util.packageinstall(["canvasapi"])
         u.lplatform.issetup=1
         u.store()
    util.fancytyping(f"Hello {u.name} \n")
    print("\n")
    programselection()
    
else:
    
   install.installloop()
   print("\n")
   programselection()


