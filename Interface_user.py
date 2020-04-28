# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:31:06 2020

@author: Supernova
"""
from tkinter import *
import tkinter as tk

from City import City
from TSP_Alg_Gen import *

class Zone(Canvas):
    def __init__(self, window, w, h):
        Canvas.__init__(self, window, width =  w, height = h, background = 'white', relief=RAISED)
        self.bind("<Button-1>", self.click)
        
        self.cities = []
        pass
    
    def click(self, event, rayon = 10, outline = "black", fill = "blue"):
        print("(x, y)", event.x, event.y)
        city = City(event.x, event.y)
        if( city != None):
            self.cities.append(city)
            rayon = rayon
            cx = city.getX()
            cy = city.getY()
            self.create_oval(cx - rayon, cy - rayon,
                                 cx + rayon, cy + rayon,
                                 outline=outline, fill=fill)
            pass
        pass
    
    
    def getCities(self):
        return self.cities
    



class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #propreties of the application
        self.geometry("1200x600")
        self.title(" TSP ")
        self.resizable(width = False, height = False)
        self.configure(background = 'gray')
        self.iconbitmap(r'icon.ico')
        
        self.cities = []
        
        #menu to add configuration element 
        self.menu = tk.Menu(self)
        self.menu.add_command(label = "Fichier")
        self.menu.add_command(label = "Edit")
        self.menu.add_command(label = "Aide")
        
        self.config( menu = self.menu)
        #canvas to creat cities and tours
        self.canvas = Zone(self, 650, 500)
        self.canvas.pack( side = RIGHT, padx = 50, pady = 50)
                
        self.frame1 = tk.Frame(self, width = 800, height = 600, bg = 'dim gray', relief=SUNKEN)
        self.frame1.pack( side = LEFT )
        # label, button and entry
        self.l1 = tk.Label(self.frame1,font=('arial',10,'bold'), text = 'Generation', fg="black", bd=10, anchor='center')
        self.l1.grid(padx = 50, pady = 20, row = 0, column = 0) 
        
        self.e1 = tk.Entry(self.frame1, font=('arial',10,'bold'), fg="gray", bd=5)
        self.e1.grid(padx = 50, pady = 20, row =0, column = 1)
        
        self.l2   = tk.Label(self.frame1, font=('arial',10,'bold'), text = 'Population', fg="black", bd=10, anchor='center')
        self.l2.grid(padx = 50, pady = 20, row = 1, column = 0)
        
        self.e2 = tk.Entry(self.frame1, font=('arial',10,'bold'), fg="gray", bd=5)
        self.e2.grid(padx = 50, pady = 20, row =1, column = 1)
        
        self.l3  = tk.Label(self.frame1, font=('arial',10,'bold'), text = 'Reproduction', fg="black", bd=10, anchor='center')
        self.l3.grid(padx = 50, pady = 20, row = 2, column = 0)
        
        self.e3 = tk.Entry(self.frame1, font=('arial',10,'bold'), fg="gray", bd=5)
        self.e3.grid(padx = 50, pady = 20, row =2, column = 1)
        
        self.l4      = tk.Label(self.frame1, font=('arial',10,'bold'), text = 'Mutation', fg="black", bd=10, anchor='center')
        self.l4.grid(padx = 10, pady = 20, row = 3, column = 0)
        
        self.e4 = tk.Entry(self.frame1, font=('arial',10,'bold'), fg="gray", bd=5)
        self.e4.grid(padx = 50, pady = 20, row = 3, column = 1)
        
        self.b1 = tk.Button(self.frame1, font=('arial',10,'bold'), bg  = "seashell4", text = " Save ", command = self.getcities)
        self.b1.grid(padx = 50, pady = 50, row = 4, column = 0 )
        
        self.b2 = tk.Button(self.frame1, font=('arial',10,'bold'), bg  = "seashell4", text = " Evolution ", command = lambda : self.canvas.Initilize_popualtion(int(self.e2.get())))
        self.b2.grid(padx = 50, pady = 50, row = 4, column = 1 )
        
        self.b3 = tk.Button(self.frame1, font=('arial',10,'bold'), bg  = "seashell4", text = " show plot ")
        self.b3.grid(padx = 50, pady = 50, row = 4, column = 2 )
        pass
    
    def getcities(self):
        self.cities = self.canvas.getCities()
        print(*self.cities, sep = '\n')
 

Interface().mainloop()