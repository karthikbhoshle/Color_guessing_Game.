
from tkinter import *
import time
import random
colour=['Red','blue','Green','Pink','Yellow','Orange','Purple','Brown']
score1=0
timeleft=60
global st



def startgame(event):

    if timeleft==60:

        countdown()
    if timeleft!=0:
       nextcolour()
def nextcolour():
    global score1
    global timeleft
    if timeleft==0:
        pass
    e.focus_set()

    if e.get().lower()==colour[1].lower():
        score1+=1#+1
    e.delete(0,END)
    random.shuffle(colour)
    l2.config(text=str(colour[0]),fg=str(colour[1]),font=('Helventica',20))
    score.config(text="Score:"+str(score1))
def fun():
    sys.exit()
def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        time.config(text="Time left:"+str(timeleft))
    if timeleft==0:
        score.config(text="your total score is:"+str(score1))
        l2.destroy()
        time.destroy()

        e.destroy()
        start = Button(root, text="Enter to Quit", font=('Helventica', 20), command=fun)
        start.grid(row=4, padx=20, pady=20)
    else:
        time.after(1000,countdown)
root=Tk()
root.title("COLOUR-GAME")
root.geometry("500x500")
l1=Label(root,fg='red',text="Type the colour of word not colour of text",font=('Helventica',18))
l1.grid(row=1, padx=20, pady=20)
l2=Label(root)
l2.grid(row=5, padx=20, pady=20)
score=Label(root,fg='blue',text="Press enter to start",font=('Helventica',20))
score.grid(row=3, padx=20, pady=20)
time=Label(root,text="Time left",font=('Helventica',20))
time.grid(row=2, padx=20, pady=20)

e=Entry(root)
root.bind('<Return>',startgame)
e.focus_set()

e.grid(row=6, padx=20, pady=20)

root.mainloop()

