import time
import sys
#do fancy character by character typing
def fancytyping(message:str):

    for i in message:
        sys.stdout.write(i+ " ")
        sys.stdout.flush()
        time.sleep(0.25)
#take multiple lines of input with one function
def multiinput(numfieldstoexpect,questions):
   answers=[]
   for i in range(0,numfieldstoexpect):
   
    if(i<numfieldstoexpect):
     answers.append(input(questions[i]+" "))
  
    
   return answers
      
