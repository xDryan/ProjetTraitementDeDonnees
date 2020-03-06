# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:16:51 2020

@author: bryan
"""

class Menu():
    
    def __init__(self, options, titre, donnees):
        self.options = options
        self.titre = titre
    
    def afficher(self, donnees):
        nombreOptions = len(self.options)
        choixValide = False
        choix = 0
        
        while not choixValide:
            # Affichage du texte de départ
            print(self.titre)
            
            # Affichage des options
            for i in range(nombreOptions):
                print("[{numeroChoix}] {libelle}".format(numeroChoix = i, libelle = self.options[i].libelle))
                
            # Vérification de la validité du choix de l'utilisateur
            choixValide = True
            choix = input(">")
            try:
                choix = int(choix)
            except ValueError:
                choix = -1
                choixValide = False
            
            if not(choix >= 0 and choix <= nombreOptions):
                print("Vous devez entrer un entier compris entre 0 et %" % nombreOptions)
                choixValide = False
            
            return self.options[choix].choix(donnees)