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
    if(u.lplatform.name=="Cavnvas"):
        util.packageinstall("canvas")
    util.fancytyping(f"Hello {u.name} \n")
    print("\n")
    programselection()
    
else:
    
   install.installloop()
   print("\n")
   programselection()


