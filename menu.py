# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:16:51 2020

@author: bryan
"""

from tkinter import *


class MenuFenetre(Frame):
    
    def __init__(self, fenetre, options, titre, donnees, **kwargs):
        for widget in fenetre.winfo_children():
            widget.destroy()
        
        Frame.__init__(self, fenetre, width=700, height=500, **kwargs)
        self.pack(fill=BOTH)
        
        self.options = options
        self.titre = Label(self, text=titre)
        self.titre.pack()
        self.donnes = donnees
        
        nombreOptions = len(self.options)
        
        for i in range(nombreOptions):
            
            boutonOption = Button(self, text=self.options[i].libelle, command=self.options[i].choix)
            boutonOption.pack()
    
    
    def afficher(self):
        self.mainloop()
        