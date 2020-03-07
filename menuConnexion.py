# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:08:06 2020

@author: bryan
"""
from tkinter import *
from actions import connexion
import manager

class MenuConnexion():
    """
        Cette fonction sert de page de connexion à l'utilisateur.
        Elle vérifie que ses identifiants sont corrects et le laisse
        accéder au menu d'actions si c'est le cas.
        parametres:
            donnees : dict
        sortie:
            menuActions : Menu
            ou
            menuPrincipal : Menu
    """
    def __init__(self, donnees):
        
        self.donnees = donnees
        fenetre = self.donnees["fenetre"]
            
        for widget in fenetre.winfo_children():
            widget.destroy()
                
        self.labelPseudo = Label(fenetre, text="Pseudo :")
        self.labelPseudo.pack()
            
        self.var_pseudo = StringVar()
        self.entryPseudo = Entry(fenetre, textvariable=self.var_pseudo, width=30)
        self.entryPseudo.pack()
            
        self.labelMotDePasse = Label(fenetre, text="Mot de passe :")
        self.labelMotDePasse.pack()
            
        self.var_motDePasse = StringVar()
        self.entryMotDePasse = Entry(fenetre, textvariable=self.var_motDePasse, width=30)
        self.entryMotDePasse.pack()
        
        self.texteAvertissement = Label(fenetre, text="")
        self.texteAvertissement.pack()
        
        self.boutonConnexion = Button(fenetre, text="Connexion", command=self.tentativeConnexion)
        self.boutonConnexion.pack()
        
        self.boutonRetour = Button(fenetre, text="Retour", command=self.retour)
        self.boutonRetour.pack(side="left")
        
    def tentativeConnexion(self):
        
        pseudo = self.var_pseudo.get()
        motDePasse = self.var_motDePasse.get()
        
        utilisateur = connexion(pseudo, motDePasse)
        if utilisateur != None:
            self.donnees["utilisateurCourant"] = utilisateur
            menuActions = manager.pageActions(self.donnees)
            return menuActions
        else:
            self.texteAvertissement["text"] = "Aucun utilisateur ne possède ces identifiants"
            
    def retour(self):
        
        manager.start(self.donnees["fenetre"], self.donnees)