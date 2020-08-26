# this is example of moving car using tkinter module
# by KD-03
from tkinter import *
import tkinter as tk

class moving_car():
    def __init__(self,master=None):
        self.master = master 
          
        # to take care movement in x direction 
        self.x = 1
        # to take care movement in y direction 
        self.y = 0
  
        # canvas object to create car
        self.canvas = Canvas(master) 
        self.p=self.canvas.create_polygon( 50,50,100,50,125,75,25,75,fill="green")
        self.r=self.canvas.create_rectangle(10,75,140,100,fill="red")
        self.o1=self.canvas.create_oval(20,95,45,125,fill="black")
        self.o2=self.canvas.create_oval(105,95,130,125,fill="black")
        self.canvas.pack()
        self.movement() 
    def movement(self): 
  
        # This is where the move() method is called 
        # This moves the car to x, y coordinates 
        self.canvas.move(self.p, self.x, self.y) 
        self.canvas.move(self.r,self.x,self.y)
        self.canvas.move(self.o1,self.x,self.y)
        self.canvas.move(self.o2,self.x,self.y)
  
        self.canvas.after(10, self.movement) 

if __name__=="__main__":
    master = Tk() 
    gfg = moving_car(master)
    mainloop() 
