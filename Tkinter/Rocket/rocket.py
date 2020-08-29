# this is example of moving rocket using tkinter module
# by KD-03
from tkinter import *
import tkinter as tk

class rocket():
    def __init__(self,master=None):
        self.master = master 
          
        # to take care movement in x direction 
        self.x = 0
        # to take care movement in y direction 
        self.y = -1
  
        # canvas object to create car
        self.canvas = Canvas( master, bg="black", height=1600, width=1000) 
        self.o=self.canvas.create_oval(800,100,900,200,fill = "white",width = 1)
        self.p=self.canvas.create_polygon( 300,1000,400,800,500,1000,fill="green")
        self.r=self.canvas.create_rectangle(300,1000,500,1300,fill="blue")
        self.p1=self.canvas.create_polygon(300,1000,300,1050,250,1050,fill="red")
        self.p2=self.canvas.create_polygon(500,1000,500,1050,550,1050,fill="red")
        self.p3=self.canvas.create_polygon(300,1150,300,1250,250,1250,fill="red")
        self.p4=self.canvas.create_polygon(500,1150,500,1250,550,1250,fill="red")
        self.p5=self.canvas.create_polygon(300,1300,500,1300,575,1400,400,1550,225,1400,fill="orange")
        self.p6=self.canvas.create_polygon(300,1300,500,1300,515,1350,400,1450,285,1350,300,1300,fill="yellow")
        self.i1=self.canvas.create_text(400,1030,text="I",fill="white",font=("Helvectica","12"))
        self.i2=self.canvas.create_text(400,1090,text="N",fill="white",font=("Helvectica","12"))
        self.i3=self.canvas.create_text(400,1150,text="D",fill="white",font=("Helvectica","12"))
        self.i4=self.canvas.create_text(400,1210,text="I",fill="white",font=("Helvectica","12"))
        self.i5=self.canvas.create_text(400,1270,text="A",fill="white",font=("Helvectica","12"))
        self.canvas.pack()
        self.movement() 
  
    def movement(self): 
  
        # This is where the move() method is called 
        # This moves the car to x, y coordinates 
        self.canvas.move(self.p, self.x, self.y) 
        self.canvas.move(self.r,self.x,self.y)
        self.canvas.move(self.p1,self.x,self.y)
        self.canvas.move(self.p2,self.x,self.y)
        self.canvas.move(self.p3,self.x,self.y)
        self.canvas.move(self.p4,self.x,self.y)
        self.canvas.move(self.p5,self.x,self.y)
        self.canvas.move(self.p6,self.x,self.y)
        self.canvas.move(self.i1,self.x,self.y)
        self.canvas.move(self.i2,self.x,self.y)
        self.canvas.move(self.i3,self.x,self.y)
        self.canvas.move(self.i4,self.x,self.y)
        self.canvas.move(self.i5,self.x,self.y)
  
        self.canvas.after(10, self.movement) 

master = Tk() 
rock= rocket(master)
mainloop() 
