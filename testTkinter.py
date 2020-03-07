# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 00:36:31 2020

@author: bryan
"""

from tkinter import *
from option import *

def test(donnees):
    return 0

class Menu(Frame):
    
    def __init__(self, fenetre, options, titre, donnees, **kwargs):
        Frame.__init__(self, fenetre, width=700, height=500, **kwargs)
        self.pack(fill=BOTH)
        
        self.options = options
        self.titre = Label(self, text=titre)
        self.titre.pack()
        self.testEntry = Entry(self, textVariable=StringVar(), width=30)
        self.donnes = donnees
        
        nombreOptions = len(self.options)
        
        for i in range(nombreOptions):
            
            boutonOption = Button(self, text=self.options[i].libelle, command=self.options[i].choix)
            boutonOption.pack()
    
    
    def afficher(self):
        self.mainloop()
        self.destroy()


if __name__ == "__main__":
    fenetre = Tk()
    options = [Option("Consultant", test, []),
               Option("Professionnel", test, []),
               Option("Quitter", test, [])]
    menu = Menu(fenetre, options, "Quel est votre statut ?", [])
    
    menu.afficher()

