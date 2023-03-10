

# import everything from tkinter module
from tkinter import *
import datetime
import os
from canvasapi import Canvas
# globally declare the expression variable
expression = ""

global equation
equation=""

# Function to update expression
# in the text entry box
def press(num):
    global equation
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


    # Function to evaluate the final expression
def equalpress():
    global equation
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:
    
     global expression

    # eval function evaluate the expression
    # and str function convert the result
    # into string
     total = str(eval(expression))

     equation.set(total)

    # initialize the expression variable
    # by empty string
     expression = ""

    # if error is generate then handle
    # by the except block
    except:

     equation.set(" error ")
     expression = ""


# Function to clear the contents
# of text entry box

def clear():
 global equation
 global expression
 expression = ""
 equation.set("")



# Driver code
def calculator():
    gui = Tk() 
    global equation
    equation=StringVar()



    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Jetcalc")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the gui window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
    command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
    command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
    command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clearbtn = Button(gui, text='Clear', fg='black', bg='red',
     command=clear, height=1, width=7)
    clearbtn.grid(row=5, column='1')
    
 
    Decimal= Button(gui, text='.', fg='black', bg='red',
    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
def filesave():
    pass
def wordprocessor():
    gui = Tk() 
    global equation
    equation=StringVar()



    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Jetink")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    T = Text(gui, height = 5, width = 80)
 
    # Create label
    l = Label(gui, text = "File.txt")
    l.config(font =("Courier", 14))
    
    
    # Create button for next text.
    b1 = Button(gui, text = "save",command=filesave() )
    
    # Create an Exit button.
   
    
    l.pack()
    T.pack()
    b1.pack()
   
    
  
    
    gui.mainloop()


def classnotes():
      subject=input("What subject>")
      curddir=os.getcwd()
      os.chdir("Files")
      date=datetime.date.today().strftime("%B %d, %Y")
      filedate=datetime.date.today().strftime("%m%d%Y")
      if(filedate[0]=='0'):
        filedate=filedate[1:len(filedate)]
      file=open(f"{subject} {filedate}notes.md","w+")
      file.write(f"# {subject} {date} Notes\n")
      file.close()
      os.chdir(curddir)
      print("File made! :)")
def terminalbrowser():
    query=input("Google >")
    from search import search as google
    google(query)
    
def canvasfunction(apiurl,apikey,userid):     
  action=input("Canvas>")
  API_URL = apiurl
  # Canvas API key
  API_KEY = apikey
  canvas = Canvas(API_URL, API_KEY)
 
  user = canvas.get_user(userid)

  # Initialize a new Canvas object
  if(action=="get courses"):
     

      courses = user.get_courses()
      for i in courses:
       print(i)
      return courses
  if(action=="get assignments"):
       assignments=user.get_assignments()
       for i in assignments:
        print(i)
       return assignments


