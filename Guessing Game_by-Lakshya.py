#by Lakshya 219 words 2,958 characters 121 lines 
#(Created on: )
    #Created on:     10 June 2021 1:26pm
    #Last update on:  4  May 2023 5:53pm 

from tkinter import *
import time
import random

root=Tk()

root.geometry("640x360")
root.minsize(320,180)
root.maxsize(1280,720)

root.config(bg="white")

root.title("Guessing Game -By Lakshya")
root.wm_iconbitmap("Workshop Project\Guessing Game_by-Lakshya\game.ico")

x=random.randint(0,100)

i=IntVar()
i.set(0)

r=StringVar()
r.set("Enter Your Number")

d=0


def ret():
    print("You Win!!!")

def reset():
    global x , r , i , but , d
    x=random.randint(0,100)
    r.set("Number Reset")
    i.set(0)
    d=0
    root.update()
    time.sleep(1)
    r.set("Enter Your Number")
    but.configure(text="Let's Check",command=check)
    root.update()

def check(f=0):
    global d , r , i , but
    d+=1
    if i.get()==x:
        but.configure(text="Congratulations",command=ret)
        root.update()
        r.set(f"You Are Correct in {d} Turns...")
        for j in range(3):
            root.config(bg="red")
            s1.config(bg="red")
            s2.config(bg="red")
            l1.config(bg="red")
            l2.config(bg="red")
            root.update()
            time.sleep(0.5)

            root.config(bg="yellow")
            s1.config(bg="yellow")
            s2.config(bg="yellow")
            l1.config(bg="yellow")
            l2.config(bg="yellow")
            root.update()
            time.sleep(0.5)

            root.config(bg="blue")
            s1.config(bg="blue")
            s2.config(bg="blue")
            l1.config(bg="blue")
            l2.config(bg="blue")
            root.update()
            time.sleep(0.5)

            root.config(bg="green")
            s1.config(bg="green")
            s2.config(bg="green")
            l1.config(bg="green")
            l2.config(bg="green")
            root.update()
            time.sleep(0.5)
        
        root.config(bg="White")
        s1.config(bg="white")
        s2.config(bg="white")
        l1.config(bg="white")
        l2.config(bg="white")
        root.update()
        but.configure(text="Reset Number?",command=reset)
        root.update()
        

    elif i.get()>x:
        r.set("Your Number is Greater")
    else:
        r.set("Your Number is Smaller")

c=Label(root,textvariable=r,font=("",15,"bold"),background="Black",foreground="white",relief=RAISED)
c.pack(fill=X)

s1=Label(root,text="",font=("",5,"bold"),background="white")
s1.pack(pady=5,fill=X)

l1=Label(root,text="I guess a random Number between 0 to 100.",font=("",20,"bold"),background="white")
l1.pack(pady=5)

l2=Label(root,text="Let's See will You guess or not...",font=("",15,"bold","italic"),background="white")
l2.pack()

s2=Label(root,text="",font=("",5,"bold"),background="white")
s2.pack(pady=15,fill=X)


Entry(root,textvariable=i,font=("",15,"bold"),background="white",bd=5,justify="center").pack(pady=15,fill=X,padx=10)

but=Button(root,text="Let's Check",relief=RAISED,command=check,font=("",15,"bold"),background="red",fg="yellow",bd=10)
but.pack(side=BOTTOM,fill=X)

root.bind("<Return>",check)

root.mainloop()